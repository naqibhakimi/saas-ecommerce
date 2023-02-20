import graphene


class BaseConnection(graphene.Connection):
    class Meta:
        abstract = True


class GiftCardConnection(BaseConnection):
    class Meta:
        abstract = True


class GiftCardTransactionConnection(BaseConnection):
    class Meta:
        abstract = True
