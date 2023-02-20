import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
    GiftCardNode,
    GiftCardTransactionNode,
)


class GiftCardQuery:
    gift_cards = DjangoFilterConnectionField(GiftCardNode)
    gift_card = graphene.Field(GiftCardNode, id=graphene.ID())


class GiftCardTransactionQuery:
    gift_card_transactions = DjangoFilterConnectionField(GiftCardTransactionNode)
    gift_card_transaction = graphene.Field(GiftCardTransactionNode, id=graphene.ID())
