from graphene_django import DjangoObjectType
import graphene

from core.types import Node

from .models import Address
from .filters import AddressFilter
from .connections import AddressConnection

class AddressNode(Node, DjangoObjectType):
    class Meta:
        model = Address
        filterset_class = AddressFilter
        interfaces = (graphene.Node)
        connection_class = AddressConnection