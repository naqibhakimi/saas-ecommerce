from graphene_permissions.permissions import AllowAuthenticated
from graphene_permissions.mixins import AuthNode, AuthFilter


class AllowAuthenticatedFilter(AuthFilter):
    permission_classes = (AllowAuthenticated,)
