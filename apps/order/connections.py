import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True


class OrderDiscountConnection(BaseConnection):
    class Meta:
        abstract = True 
class OrderGiftCardConnection(BaseConnection):
    class Meta:
        abstract = True 
class OrderConnection(BaseConnection):
    class Meta:
        abstract = True 
class OrderEditConnection(BaseConnection):
    class Meta:
        abstract = True 
class OrderItemChangeConnection(BaseConnection):
    class Meta:
        abstract = True 
class DraftOrderConnection(BaseConnection):
    class Meta:
        abstract = True 
class ClaimOrderConnection(BaseConnection):
    class Meta:
        abstract = True 
class ClaimTagConnection(BaseConnection):
    class Meta:
        abstract = True 
class ClaimItemConnection(BaseConnection):
    class Meta:
        abstract = True 
class ClaimImageConnection(BaseConnection):
    class Meta:
        abstract = True 
class ReturnConnection(BaseConnection):
    class Meta:
        abstract = True 
class ReturnItemConnection(BaseConnection):
    class Meta:
        abstract = True 
class ReturnReasonConnection(BaseConnection):
    class Meta:
        abstract = True 