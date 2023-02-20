import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
    CustomerNode,
    CustomerGroupNode,
    CountryNode,
    AddressNode,
    RegionNode,
)


class CustomerQuery:
    customers = DjangoFilterConnectionField(CustomerNode)
    customer = graphene.Field(CustomerNode, id=graphene.ID())


class CountryQuery:
    countrys = DjangoFilterConnectionField(CountryNode)
    country = graphene.Field(CountryNode, id=graphene.ID())


class AddressQuery:
    addresss = DjangoFilterConnectionField(AddressNode)
    address = graphene.Field(AddressNode, id=graphene.ID())


class CustomerGroupQuery:
    customer_groups = DjangoFilterConnectionField(CustomerGroupNode)
    customer_group = graphene.Field(CustomerGroupNode, id=graphene.ID())


class RegionQuery:
    regions = DjangoFilterConnectionField(RegionNode)
    region = graphene.Field(RegionNode, id=graphene.ID())
