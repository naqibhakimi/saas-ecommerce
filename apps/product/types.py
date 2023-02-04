from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

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
from .filters import (
    PriceListFilter,
    MoneyAmountFilter,
    ProductTypeFilter,
    ProductTagFilter,
    ImageFilter,
    ProductFilter,
    ProductCategoryFilter,
    ProductCollectionFilter,
    ProductOptionFilter,
    ProductOptionValueFilter,
    ProductTaxRateFilter,
    ProductTypeTaxRateFilter,
    ProductVariantInventoryItemFilter,
    ProductVariantFilter,
)
from .connections import (
    PriceListConnection,
    MoneyAmountConnection,
    ProductTypeConnection,
    ProductTagConnection,
    ImageConnection,
    ProductConnection,
    ProductCategoryConnection,
    ProductCollectionConnection,
    ProductOptionConnection,
    ProductOptionValueConnection,
    ProductTaxRateConnection,
    ProductTypeTaxRateConnection,
    ProductVariantInventoryItemConnection,
    ProductVariantConnection,
)



class PriceListNode(Node, DjangoObjectType):
    class Meta:
        model = PriceList
        filter_class = PriceListFilter 
        interfaces = (graphene.Node,)
        connection_class = PriceListConnection 


class MoneyAmountNode(Node, DjangoObjectType):
    class Meta:
        model = MoneyAmount
        filter_class = MoneyAmountFilter 
        interfaces = (graphene.Node,)
        connection_class = MoneyAmountConnection 


class ProductTypeNode(Node, DjangoObjectType):
    class Meta:
        model = ProductType
        filter_class = ProductTypeFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductTypeConnection 


class ProductTagNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTag
        filter_class = ProductTagFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductTagConnection 


class ImageNode(Node, DjangoObjectType):
    class Meta:
        model = Image
        filter_class = ImageFilter 
        interfaces = (graphene.Node,)
        connection_class = ImageConnection 


class ProductNode(Node, DjangoObjectType):
    class Meta:
        model = Product
        filter_class = ProductFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductConnection 


class ProductCategoryNode(Node, DjangoObjectType):
    class Meta:
        model = ProductCategory
        filter_class = ProductCategoryFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductCategoryConnection 


class ProductCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = ProductCollection
        filter_class = ProductCollectionFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductCollectionConnection 


class ProductOptionNode(Node, DjangoObjectType):
    class Meta:
        model = ProductOption
        filter_class = ProductOptionFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductOptionConnection 


class ProductOptionValueNode(Node, DjangoObjectType):
    class Meta:
        model = ProductOptionValue
        filter_class = ProductOptionValueFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductOptionValueConnection 


class ProductTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTaxRate
        filter_class = ProductTaxRateFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductTaxRateConnection 


class ProductTypeTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTypeTaxRate
        filter_class = ProductTypeTaxRateFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductTypeTaxRateConnection 


class ProductVariantInventoryItemNode(Node, DjangoObjectType):
    class Meta:
        model = ProductVariantInventoryItem
        filter_class = ProductVariantInventoryItemFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductVariantInventoryItemConnection 


class ProductVariantNode(Node, DjangoObjectType):
    class Meta:
        model = ProductVariant
        filter_class = ProductVariantFilter 
        interfaces = (graphene.Node,)
        connection_class = ProductVariantConnection 

