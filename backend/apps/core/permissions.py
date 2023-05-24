from graphene import ResolveInfo
# from graphene_permissions.permissions import AllowAuthenticated, AllowStaff, AllowSuperuser, AllowAny
# from graphene_permissions.mixins import AuthNode, AuthFilter
from graphql_jwt.shortcuts import get_user_by_token
from typing import Optional, Any 
from django.db.models import Model


class AllowAny(object):
    """
    Default authentication class.
    Allows any user for any action.
    """
    
    @classmethod
    def has_permission(cls, info: ResolveInfo) -> bool:
        return True
    
    # FIXME: dosn't work
    # @classmethod
    # def has_filter_permission(cls, info: ResolveInfo, queryset) -> bool:
    #     return True

    

class BasePermission:
    """
    Base permission class.
    Subclass it and override methods below.
    """

    @classmethod
    def has_permission(cls, info: ResolveInfo) -> bool:
        """Fallback for other has_..._permission functions.
        Returns False by default, overwrite for custom behaviour.
        """
        return False

    @classmethod
    def has_node_permission(cls, info: ResolveInfo, id: str) -> bool:
        return cls.has_permission(info)

    @classmethod
    def has_mutation_permission(cls, root: Any, info: ResolveInfo, input: dict) -> bool:
        return cls.has_permission(info)

    @classmethod
    def has_filter_permission(cls, info: ResolveInfo) -> bool:
        return cls.has_permission(info)



class PermissionNode:
    """
    Permission mixin for queries (nodes).
    Allows for simple configuration of access to nodes via class system.
    """

    permission_classes = (AllowAny,)
        
    @classmethod
    def get_node(cls, info: ResolveInfo, id: str) -> Optional[Model]:
        queryset = None
        for perm in cls.permission_classes:
            if queryset is None:
                queryset = perm.has_permission(info, cls._meta.model, id)
            else:
                queryset &= perm.has_permission(info, cls._meta.model, id)
        try:
            return queryset[0]
        except IndexError:
            return None
        
    
    @classmethod
    def get_queryset(cls, queryset, info):
        queryset = queryset.filter()
        for perm in cls.permission_classes:
            queryset &= perm.has_filter_permission(info, queryset)
        return queryset


class AllowAuthenticated(object):
    """
    Allows performing action only for logged in users.
    """
    
    @classmethod
    def has_permission(cls, info: ResolveInfo) -> bool:
        return info.context.user.is_authenticated
    
    # FIXME: DO we need to have filter_permission in here and superuser too?
    @classmethod
    def has_filter_permission(cls, info: ResolveInfo, queryset) -> bool:
        return info.context.user.is_authenticated
    
    
    
# class AllowStaffFilter(AuthFilter):
#     permission_classes = (AllowStaff,)
    
class AllowStaff(object):
    """
    Allow performing action only for staff users.
    """
    @classmethod
    def has_permission(cls, info: ResolveInfo) -> bool:
        return info.context.user.is_staff
    
    @classmethod
    def has_filter_permission(cls, info: ResolveInfo, queryset) -> bool:
        return info.context.user.is_staff


    
class AllowSuperuser(object):
    """
    Allow performing action only for superusers.
    """
    
    @classmethod
    def has_permission(cls, info: ResolveInfo) -> bool:
        return info.context.user.is_superuser
    
    @classmethod
    def has_filter_permission(cls, info: ResolveInfo, queryset) -> bool:
        return info.context.user.is_superuser


class AllowOwner(object):
    
    @classmethod
    def has_permission(cls, info: ResolveInfo, model, id) -> bool:
        return model.objects.filter(pk=id, created_by=info.context.user)  # type: ignore
    
    @classmethod
    def has_filter_permission(cls, info: ResolveInfo, queryset) -> bool:
        return queryset.filter(created_by=info.context.user)
    

class AllowUpdateBy:
    
    @classmethod
    def has_permission(cls, info: ResolveInfo, model, id) -> bool:
        return model.objects.filter(pk=id, updated_by=info.context.user)  # type: ignore

    @classmethod
    def has_filter_permission(cls, info: ResolveInfo, queryset) -> bool:
        return queryset.filter(updated_by=info.context.user)
