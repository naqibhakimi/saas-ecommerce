import graphene


class BaseConnection(graphene.Connection):
    class Meta:
        abstract = True


class PriceListConnection(BaseConnection):
    class Meta:
        abstract = True


class MoneyAmountConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductTypeConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductTagConnection(BaseConnection):
    class Meta:
        abstract = True


class ImageConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductCategoryConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductCollectionConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductOptionConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductOptionValueConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductTaxRateConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductTypeTaxRateConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductVariantInventoryItemConnection(BaseConnection):
    class Meta:
        abstract = True


class ProductVariantConnection(BaseConnection):
    class Meta:
        abstract = True
