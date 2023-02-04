import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
    CustomerNode,
    CustomerGroupNode,
    CountryNode,
    AddressNode,
    RegionNode,
)
class CustomerQuery:
        customers = DjangoConnectionField(CustomerNode)
        customer = graphene.Field(CustomerNode, id=graphene.ID())
        
class CountryQuery:
        countrys = DjangoConnectionField(CountryNode)
        country = graphene.Field(CountryNode, id=graphene.ID())
        
class AddressQuery:
        addresss = DjangoConnectionField(AddressNode)
        address = graphene.Field(AddressNode, id=graphene.ID())
        
class CustomerGroupQuery:
        customer_groups = DjangoConnectionField(CustomerGroupNode)
        customer_group = graphene.Field(CustomerGroupNode, id=graphene.ID())
       
        
class RegionQuery:
        regions = DjangoConnectionField(RegionNode)
        region = graphene.Field(RegionNode, id=graphene.ID())
    