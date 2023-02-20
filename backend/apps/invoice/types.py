from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    LineItem,
    LineItemAdjustment,
    LineItemTaxLine,
)

from .connections import (
    LineItemConnection,
    LineItemAdjustmentConnection,
    LineItemTaxLineConnection,
)

from .filters import (
    LineItemFilter,
    LineItemAdjustmentFilter,
    LineItemTaxLineFilter,
)


class LineItemNode(Node, DjangoObjectType):
    class Meta:
        model = LineItem
        filterset_class = LineItemFilter
        interfaces = (graphene.Node,)
        connection_class = LineItemConnection


class LineItemAdjustmentNode(Node, DjangoObjectType):
    class Meta:
        model = LineItemAdjustment
        filterset_class = LineItemAdjustmentFilter
        interfaces = (graphene.Node,)
        connection_class = LineItemAdjustmentConnection


class LineItemTaxLineNode(Node, DjangoObjectType):
    class Meta:
        model = LineItemTaxLine
        filterset_class = LineItemTaxLineFilter
        interfaces = (graphene.Node,)
        connection_class = LineItemTaxLineConnection
