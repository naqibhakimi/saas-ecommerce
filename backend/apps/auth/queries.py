import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import UserNode, UserStatusNode

import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from apps.auth.types import UserNode


class Query:
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)
    me = graphene.Field(UserNode)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            user.owner = user.employee.first()
            return user
        return None
