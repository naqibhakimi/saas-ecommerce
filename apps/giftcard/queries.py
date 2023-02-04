import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
        GiftCardNode,
        GiftCardTransactionNode,
)


class GiftCardQuery:
        gift_cards = DjangoConnectionField(GiftCardNode)
        gift_card= graphene.Field(GiftCardNode, id = graphene.ID())
class GiftCardTransactionQuery:
        gift_card_transactions= DjangoConnectionField(GiftCardTransactionNode)
        gift_card_transaction = graphene.Field(GiftCardTransactionNode, id = graphene.ID())
