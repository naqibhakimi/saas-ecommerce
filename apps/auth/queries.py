import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import UserNode, UserStatusNode

import graphene
from django.db.models import Q
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from apps.auth.types import UserNode


# class Query:
#     users = DjangoFilterConnectionField(UserNode, 'users')


class UserQuery:
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)


class UserStatusQuery:
    user_status = graphene.relay.Node.Field(UserStatusNode)
    user_statuses = DjangoFilterConnectionField(UserStatusNode)


class MeQuery(graphene.ObjectType):
    me = graphene.Field(UserNode)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            user.owner = user.employee.first()
            return user
        return None
