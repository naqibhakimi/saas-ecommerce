import django_filters

from .models import (
    PriceList,
    MoneyAmount,
    ProductType,
    ProductTag,
    Image,
    Product,
    ProductCategory,
    ProductCollection,
    ProductOption,
    ProductOptionValue,
    ProductTaxRate,
    ProductTypeTaxRate,
    ProductVariantInventoryItem,
    ProductVariant,
)


class PriceListFilter(django_filters.FilterSet):
    class Meta:
        model = PriceList
        exclude = "metadata"


class MoneyAmountFilter(django_filters.FilterSet):
    class Meta:
        model = MoneyAmount
        exclude = "metadata"


class ProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ProductType
        exclude = "metadata"


class ProductTagFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTag
        exclude = "metadata"


class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        exclude = ("metadata", "file")


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        exclude = ("metadata", "thumbnail", "images")


class ProductCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCategory
        exclude = "metadata"


class ProductCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCollection
        exclude = "metadata"


class ProductOptionFilter(django_filters.FilterSet):
    class Meta:
        model = ProductOption
        exclude = "metadata"


class ProductOptionValueFilter(django_filters.FilterSet):
    class Meta:
        model = ProductOptionValue
        exclude = "metadata"


class ProductTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTaxRate
        exclude = "metadata"


class ProductTypeTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTypeTaxRate
        exclude = "metadata"


class ProductVariantInventoryItemFilter(django_filters.FilterSet):
    class Meta:
        model = ProductVariantInventoryItem
        exclude = "metadata"


class ProductVariantFilter(django_filters.FilterSet):
    class Meta:
        model = ProductVariant
        exclude = "metadata"
