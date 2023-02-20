from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    DiscountCondition,
    DiscountRule,
    Discount,
    DiscountConditionCustomerGroup,
    DiscountConditionProductCollection,
    DiscountConditionProductTag,
    DiscountConditionProductType,
    DiscountConditionProduct,
)
from .filters import (
    DiscountConditionFilter,
    DiscountRuleFilter,
    DiscountFilter,
    DiscountConditionCustomerGroupFilter,
    DiscountConditionProductCollectionFilter,
    DiscountConditionProductTagFilter,
    DiscountConditionProductTypeFilter,
    DiscountConditionProductFilter,
)

from .connections import (
    DiscountConditionConnection,
    DiscountRuleConnection,
    DiscountConnection,
    DiscountConditionCustomerGroupConnection,
    DiscountConditionProductCollectionConnection,
    DiscountConditionProductTagConnection,
    DiscountConditionProductTypeConnection,
    DiscountConditionProductConnection,
)


class DiscountConditionNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountCondition
        filterset_class = DiscountConditionFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConditionConnection


class DiscountRuleNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountRule
        filterset_class = DiscountRuleFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountRuleConnection


class DiscountNode(Node, DjangoObjectType):
    class Meta:
        model = Discount
        filterset_class = DiscountFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConnection


class DiscountConditionCustomerGroupNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionCustomerGroup
        filterset_class = DiscountConditionCustomerGroupFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConditionCustomerGroupConnection


class DiscountConditionProductCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProductCollection
        filterset_class = DiscountConditionProductCollectionFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConditionProductCollectionConnection


class DiscountConditionProductTagNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProductTag
        filterset_class = DiscountConditionProductTagFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConditionProductTagConnection


class DiscountConditionProductTypeNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProductType
        filterset_class = DiscountConditionProductTypeFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConditionProductTypeConnection


class DiscountConditionProductNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProduct
        filterset_class = DiscountConditionProductFilter
        interfaces = (graphene.Node,)
        connection_class = DiscountConditionProductConnection
