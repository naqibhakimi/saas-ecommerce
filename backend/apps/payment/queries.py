import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
    IdempotencyKeyNode,
    CurrencyNode,
    PaymentNode,
    PaymentSessionNode,
    PaymentCollectionNode,
    PaymentProviderNode,
    RefundNode,
)


class PaymentQuery:
    payments = DjangoFilterConnectionField(PaymentNode)
    payment = graphene.Field(PaymentNode, id=graphene.ID())


class PaymentSessionQuery:
    payment_sessions = DjangoFilterConnectionField(PaymentSessionNode)
    payment_session = graphene.Field(PaymentSessionNode, id=graphene.ID())


class CurrencyQuery:
    currencys = DjangoFilterConnectionField(CurrencyNode)
    currency = graphene.Field(CurrencyNode, id=graphene.ID())


class IdempotencyKeyQuery:
    idempotency_keys = DjangoFilterConnectionField(IdempotencyKeyNode)
    idempotency_key = graphene.Field(IdempotencyKeyNode, id=graphene.ID())


class PaymentCollectionQuery:
    payment_collections = DjangoFilterConnectionField(PaymentCollectionNode)
    payment_collection = graphene.Field(PaymentCollectionNode, id=graphene.ID())


class PaymentProviderQuery:
    payment_providers = DjangoFilterConnectionField(PaymentProviderNode)
    payment_provider = graphene.Field(PaymentProviderNode, id=graphene.ID())


class RefundQuery:
    refunds = DjangoFilterConnectionField(RefundNode)
    refund = graphene.Field(RefundNode, id=graphene.ID())
