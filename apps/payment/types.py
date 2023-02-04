from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    IdempotencyKey,
    Currency,
    Payment,
    PaymentSession,
    PaymentCollection,
    PaymentProvider,
    Refund,
)
from .filters import (
    IdempotencyKeyFilter,
    CurrencyFilter,
    PaymentFilter,
    PaymentSessionFilter,
    PaymentCollectionFilter,
    PaymentProviderFilter,
    RefundFilter,
)
from .connections import (
    IdempotencyKeyConnection,
    CurrencyConnection,
    PaymentConnection,
    PaymentSessionConnection,
    PaymentCollectionConnection,
    PaymentProviderConnection,
    RefundConnection,
)


class IdempotencyKeyNode(Node, DjangoObjectType):
    class Meta:
        model = IdempotencyKey 
        filterset_class = IdempotencyKeyFilter 
        interfaces = (graphene.Node,)
        connection_class = IdempotencyKeyConnection 


class CurrencyNode(Node, DjangoObjectType):
    class Meta:
        model = Currency 
        filterset_class = CurrencyFilter 
        interfaces = (graphene.Node,)
        connection_class = CurrencyConnection 


class PaymentNode(Node, DjangoObjectType):
    class Meta:
        model = Payment 
        filterset_class = PaymentFilter 
        interfaces = (graphene.Node,)
        connection_class = PaymentConnection 


class PaymentSessionNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentSession 
        filterset_class = PaymentSessionFilter 
        interfaces = (graphene.Node,)
        connection_class = PaymentSessionConnection 


class PaymentCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentCollection 
        filterset_class = PaymentCollectionFilter 
        interfaces = (graphene.Node,)
        connection_class = PaymentCollectionConnection 


class PaymentProviderNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentProvider 
        filterset_class = PaymentProviderFilter 
        interfaces = (graphene.Node,)
        connection_class = PaymentProviderConnection 


class RefundNode(Node, DjangoObjectType):
    class Meta:
        model = Refund 
        filterset_class = RefundFilter 
        interfaces = (graphene.Node,)
        connection_class = RefundConnection 


