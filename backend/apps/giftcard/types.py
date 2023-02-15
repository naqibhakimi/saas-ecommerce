from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    GiftCard,
    GiftCardTransaction,
)

from .connections import (
    GiftCardConnection,
    GiftCardTransactionConnection,
)

from .filters import (
    GiftCardFilter,
    GiftCardTransactionFilter,
)


class GiftCardNode(Node, DjangoObjectType):
    class Meta:
        model = GiftCard
        filterset_class = GiftCardFilter 
        interfaces = (graphene.Node, )
        connection_class = GiftCardConnection 


class GiftCardTransactionNode(Node, DjangoObjectType):
    class Meta:
        model = GiftCardTransaction
        filterset_class = GiftCardTransactionFilter 
        interfaces = (graphene.Node, )
        connection_class = GiftCardTransactionConnection 


