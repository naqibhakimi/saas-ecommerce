import graphene
from graphene_django.fields import DjangoConnectionField

from .type import AddressNode

class Query:
    addresses = DjangoConnectionField(AddressNode)
    address = graphene.Field(AddressNode, id=graphene.ID())