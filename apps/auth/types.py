import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from apps.core.types import Node

from .connections import UserConnection
from .filters import UserFilter


class UserNode(DjangoObjectType):
    class Meta:
        model= User
        interfaces= (graphene.Node,)
        filterset_class = UserFilter 
        connection_class = UserConnection