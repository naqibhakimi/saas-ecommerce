from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    Customer,
    CustomerGroup,
    Country,
    Address,
    Region,
)

from .filters import (
    CustomerFilter,
    CustomerGroupFilter,
    CountryFilter,
    AddressFilter,
    RegionFilter,
)
from .connections import (
    CustomerConnection,
    CustomerGroupConnection,
    CountryConnection,
    AddressConnection,
    RegionConnection,
)


class CustomerNode(Node, DjangoObjectType):
    full_name = graphene.String(source="full_name")
    number_of_orders = graphene.Int(source="number_of_orders")

    class Meta:
        model = Customer
        filterset_class = CustomerFilter
        interfaces = (graphene.Node,)
        connection_class = CustomerConnection


class CustomerGroupNode(Node, DjangoObjectType):
    class Meta:
        model = CustomerGroup
        filterset_class = CustomerGroupFilter
        interfaces = (graphene.Node,)
        connection_class = CustomerGroupConnection


class CountryNode(Node, DjangoObjectType):
    class Meta:
        model = Country
        filterset_class = CountryFilter
        interfaces = (graphene.Node,)
        connection_class = CountryConnection


class AddressNode(Node, DjangoObjectType):
    class Meta:
        model = Address
        filterset_class = AddressFilter
        interfaces = (graphene.Node,)
        connection_class = AddressConnection


class RegionNode(Node, DjangoObjectType):
    class Meta:
        model = Region
        filterset_class = RegionFilter
        interfaces = (graphene.Node,)
        connection_class = RegionConnection
