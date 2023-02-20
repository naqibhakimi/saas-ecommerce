from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    TaxLine,
    TaxRate,
    TaxProvider,
)
from .filters import (
    TaxLineFilter,
    TaxRateFilter,
    TaxProviderFilter,
)
from .connections import (
    TaxLineConnection,
    TaxRateConnection,
    TaxProviderConnection,
)


class TaxLineNode(Node, DjangoObjectType):
    class Meta:
        model = TaxLine
        filterset_class = TaxLineFilter
        interfaces = (graphene.Node,)
        connection_class = TaxLineConnection


class TaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = TaxRate
        filterset_class = TaxRateFilter
        interfaces = (graphene.Node,)
        connection_class = TaxRateConnection


class TaxProviderNode(Node, DjangoObjectType):
    class Meta:
        model = TaxProvider
        filterset_class = TaxProviderFilter
        interfaces = (graphene.Node,)
        connection_class = TaxProviderConnection
