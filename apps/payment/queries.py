import graphene
from graphene_django.fields import DjangoConnectionField

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
        payments = DjangoConnectionField(PaymentNode)
        payment = graphene.Field(PaymentNode, id=graphene.ID())
        
class PaymentSessionQuery:
        payment_sessions = DjangoConnectionField(PaymentSessionNode)
        payment_session = graphene.Field(PaymentSessionNode, id=graphene.ID())
        
        
class CurrencyQuery:
        currencys = DjangoConnectionField(CurrencyNode)
        currency = graphene.Field(CurrencyNode, id=graphene.ID())
        
        
class IdempotencyKeyQuery:
        idempotency_keys = DjangoConnectionField(IdempotencyKeyNode)
        idempotency_key = graphene.Field(IdempotencyKeyNode, id=graphene.ID())
        
        
class PaymentCollectionQuery:
        payment_collections = DjangoConnectionField(PaymentCollectionNode)
        payment_collection = graphene.Field(PaymentCollectionNode, id=graphene.ID())
        
class PaymentProviderQuery:
        payment_providers = DjangoConnectionField(PaymentProviderNode)
        payment_provider = graphene.Field(PaymentProviderNode, id=graphene.ID())
        
class RefundQuery:
        refunds = DjangoConnectionField(RefundNode)
        refund = graphene.Field(RefundNode, id=graphene.ID())