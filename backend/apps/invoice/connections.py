import graphene


class BaseConnection(graphene.Connection):
    class Meta:
        abstract = True


class LineItemConnection(BaseConnection):
    class Meta:
        abstract = True


class LineItemAdjustmentConnection(BaseConnection):
    class Meta:
        abstract = True


class LineItemTaxLineConnection(BaseConnection):
    class Meta:
        abstract = True
