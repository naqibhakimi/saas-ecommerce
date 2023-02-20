import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
    TaxLineNode,
    TaxRateNode,
    TaxProviderNode,
)


class TaxLineQuery:
    tax_lines = DjangoFilterConnectionField(TaxLineNode)
    tax_line = graphene.Field(TaxLineNode, id=graphene.ID())


class TaxRateQuery:
    tax_rates = DjangoFilterConnectionField(TaxRateNode)
    tax_rate = graphene.Field(TaxRateNode, id=graphene.ID())


class TaxProviderQuery:
    tax_providers = DjangoFilterConnectionField(TaxProviderNode)
    tax_provider = graphene.Field(TaxProviderNode, id=graphene.ID())
