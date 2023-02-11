import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from apps.core.types import Node

from .connections import UserConnection
from .filters import UserFilter,SEUserFilter


class UserNode(DjangoObjectType):
    class Meta:
        model= User
        interfaces= (graphene.Node,)
        filterset_class = UserFilter 
        connection_class = UserConnection


import graphene
from graphene_django import DjangoObjectType
from graphene_django.utils import camelize

from apps.core.mutations import Node
# from apps.auth.filters import (CompanyFilter, LogAttemptsFilter,
#                                  ProfileFilter, SecureUserFilter,
#                                  UserEmailLogFilter)
from apps.auth.filters import ( LogAttemptsFilter,
                                 UserEmailLogFilter)

from .exceptions import WrongUsage
from .models import Company, LogAttempts, Profile, SecureUser, UserEmailLog
from .settings import graphql_auth_settings as app_settings


# class CompanyNode(Node, DjangoObjectType):
#     company_logo = graphene.String(source = 'company_logo_url')
#     class Meta:
#         model = Company
#         filterset_class = CompanyFilter
#         interfaces = (graphene.Node,)



class UserNode(DjangoObjectType):
    class Meta:
        model = SecureUser
        filterset_class = SEUserFilter
        interfaces = (graphene.relay.Node,)
        skip_registry = True

    pk = graphene.Int()
    archived = graphene.Boolean()
    verified = graphene.Boolean()
    secondary_email = graphene.String()

    def resolve_pk(self, info):
        return self.pk

    def resolve_archived(self, info):
        return self.status.archived

    def resolve_verified(self, info):
        return self.status.verified

    def resolve_secondary_email(self, info):
        return self.status.secondary_email

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related("status")



# class ProfileNode(Node, DjangoObjectType):
#     class Meta:
#         model = Profile
#         filterset_class = ProfileFilter
#         interfaces = (graphene.Node,)


class LogAttemptsNode(Node, DjangoObjectType):
    class Meta:
        model = LogAttempts
        filterset_class = LogAttemptsFilter
        interfaces = (graphene.Node,)


class UserEmailLogNode(Node, DjangoObjectType):
    class Meta:
        model = UserEmailLog
        filterset_class = UserEmailLogFilter
        interfaces = (graphene.Node,)
