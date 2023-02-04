import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
        TaxLineNode,
        TaxRateNode,
        TaxProviderNode,
)

class TaxLineQuery:
        tax_lines = DjangoConnectionField(TaxLineNode)
        tax_line = graphene.Field(TaxLineNode, id=graphene.ID())
       
class TaxRateQuery:
        tax_rates = DjangoConnectionField(TaxRateNode)
        tax_rate = graphene.Field(TaxRateNode, id=graphene.ID())
        
class TaxProviderQuery:
        tax_providers = DjangoConnectionField(TaxProviderNode)
        tax_provider = graphene.Field(TaxProviderNode, id=graphene.ID())
        
