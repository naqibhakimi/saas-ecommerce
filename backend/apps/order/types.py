from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    OrderDiscount,
    OrderGiftCard,
    Order,
    OrderEdit,
    OrderItemChange,
    DraftOrder,
    ClaimOrder,
    ClaimTag,
    ClaimItem,
    ClaimImage,
    Return,
    ReturnItem,
    ReturnReason,
)

from .connections import (
    OrderDiscountConnection,
    OrderGiftCardConnection,
    OrderConnection,
    OrderEditConnection,
    OrderItemChangeConnection,
    DraftOrderConnection,
    ClaimOrderConnection,
    ClaimTagConnection,
    ClaimItemConnection,
    ClaimImageConnection,
    ReturnConnection,
    ReturnItemConnection,
    ReturnReasonConnection,
)

from .filters import (
    OrderDiscountFilter,
    OrderGiftCardFilter,
    OrderFilter,
    OrderEditFilter,
    OrderItemChangeFilter,
    DraftOrderFilter,
    ClaimOrderFilter,
    ClaimTagFilter,
    ClaimItemFilter,
    ClaimImageFilter,
    ReturnFilter,
    ReturnItemFilter,
    ReturnReasonFilter,
)


class OrderDiscountNode(Node, DjangoObjectType):
    class Meta:
        model = OrderDiscount
        filterset_class = OrderDiscountFilter
        interfaces = (graphene.Node,)
        connection_class = OrderDiscountConnection


class OrderDiscountNode(Node, DjangoObjectType):
    class Meta:
        model = OrderDiscount
        filterset_class = OrderDiscountFilter
        interfaces = (graphene.Node,)
        connection_class = OrderDiscountConnection


class OrderGiftCardNode(Node, DjangoObjectType):
    class Meta:
        model = OrderGiftCard
        filterset_class = OrderGiftCardFilter
        interfaces = (graphene.Node,)
        connection_class = OrderGiftCardConnection


class OrderNode(Node, DjangoObjectType):
    class Meta:
        model = Order
        filterset_class = OrderFilter
        interfaces = (graphene.Node,)
        connection_class = OrderConnection


class OrderEditNode(Node, DjangoObjectType):
    class Meta:
        model = OrderEdit
        filterset_class = OrderEditFilter
        interfaces = (graphene.Node,)
        connection_class = OrderEditConnection


class OrderItemChangeNode(Node, DjangoObjectType):
    class Meta:
        model = OrderItemChange
        filterset_class = OrderItemChangeFilter
        interfaces = (graphene.Node,)
        connection_class = OrderItemChangeConnection


class DraftOrderNode(Node, DjangoObjectType):
    class Meta:
        model = DraftOrder
        filterset_class = DraftOrderFilter
        interfaces = (graphene.Node,)
        connection_class = DraftOrderConnection


class ClaimOrderNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimOrder
        filterset_class = ClaimOrderFilter
        interfaces = (graphene.Node,)
        connection_class = ClaimOrderConnection


class ClaimTagNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimTag
        filterset_class = ClaimTagFilter
        interfaces = (graphene.Node,)
        connection_class = ClaimTagConnection


class ClaimItemNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimItem
        filterset_class = ClaimItemFilter
        interfaces = (graphene.Node,)
        connection_class = ClaimItemConnection


class ClaimImageNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimImage
        filterset_class = ClaimImageFilter
        interfaces = (graphene.Node,)
        connection_class = ClaimImageConnection


class ReturnNode(Node, DjangoObjectType):
    class Meta:
        model = Return
        filterset_class = ReturnFilter
        interfaces = (graphene.Node,)
        connection_class = ReturnConnection


class ReturnItemNode(Node, DjangoObjectType):
    class Meta:
        model = ReturnItem
        filterset_class = ReturnItemFilter
        interfaces = (graphene.Node,)
        connection_class = ReturnItemConnection


class ReturnReasonNode(Node, DjangoObjectType):
    class Meta:
        model = ReturnReason
        filterset_class = ReturnReasonFilter
        interfaces = (graphene.Node,)
        connection_class = ReturnReasonConnection
