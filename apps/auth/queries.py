import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import UserNode


class Query:
    users = DjangoFilterConnectionField(UserNode, 'users')


class Mutation:
    pass