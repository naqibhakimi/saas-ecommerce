import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True


class IdempotencyKeyConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class CurrencyConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class PaymentConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class PaymentSessionConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class PaymentCollectionConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class PaymentProviderConnection(BaseConnection):
    class Meta:
        abstract = True 

        
class RefundConnection(BaseConnection):
    class Meta:
        abstract = True 

        