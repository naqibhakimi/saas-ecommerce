from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node
from apps.core.permissions import (
    AllowAuthenticated, 
    AllowOwner, 
    AllowUpdateBy,
    AllowStaff,
    AllowSuperuser,
)
from apps.core.permissions import PermissionNode

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
        filterset_class = PriceListFilter
        interfaces = (graphene.Node,)
        connection_class = PriceListConnection


class MoneyAmountNode(PermissionNode ,Node, DjangoObjectType):
    # permission_classes = (AllowOwner, AllowUpdateBy, AllowStaff, AllowSuperuser)
    permission_classes = (AllowOwner, AllowUpdateBy)

    class Meta:
        model = MoneyAmount
        filterset_class = MoneyAmountFilter
        interfaces = (graphene.Node,)
        connection_class = MoneyAmountConnection


class ProductTypeNode(Node, DjangoObjectType):
    class Meta:
        model = ProductType
        filterset_class = ProductTypeFilter
        interfaces = (graphene.Node,)
        connection_class = ProductTypeConnection


class ProductTagNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTag
        filterset_class = ProductTagFilter
        interfaces = (graphene.Node,)
        connection_class = ProductTagConnection


class ImageNode(PermissionNode ,Node, DjangoObjectType):
    permission_classes = (AllowOwner, AllowUpdateBy)
    class Meta:
        model = Image
        filterset_class = ImageFilter
        interfaces = (graphene.Node,)
        connection_class = ImageConnection


class ProductNode(PermissionNode, Node, DjangoObjectType):
    permission_classes = (AllowOwner, AllowUpdateBy)
    
    class Meta:
        model = Product
        filterset_class = ProductFilter
        interfaces = (graphene.Node,)
        connection_class = ProductConnection


class ProductCategoryNode(Node, DjangoObjectType):
    class Meta:
        model = ProductCategory
        filterset_class = ProductCategoryFilter
        interfaces = (graphene.Node,)
        connection_class = ProductCategoryConnection


class ProductCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = ProductCollection
        filterset_class = ProductCollectionFilter
        interfaces = (graphene.Node,)
        connection_class = ProductCollectionConnection


class ProductOptionNode(Node, DjangoObjectType):
    class Meta:
        model = ProductOption
        filterset_class = ProductOptionFilter
        interfaces = (graphene.Node,)
        connection_class = ProductOptionConnection


class ProductOptionValueNode(Node, DjangoObjectType):
    class Meta:
        model = ProductOptionValue
        filterset_class = ProductOptionValueFilter
        interfaces = (graphene.Node,)
        connection_class = ProductOptionValueConnection


class ProductTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTaxRate
        filterset_class = ProductTaxRateFilter
        interfaces = (graphene.Node,)
        connection_class = ProductTaxRateConnection


class ProductTypeTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTypeTaxRate
        filterset_class = ProductTypeTaxRateFilter
        interfaces = (graphene.Node,)
        connection_class = ProductTypeTaxRateConnection


class ProductVariantInventoryItemNode(Node, DjangoObjectType):
    class Meta:
        model = ProductVariantInventoryItem
        filterset_class = ProductVariantInventoryItemFilter
        interfaces = (graphene.Node,)
        connection_class = ProductVariantInventoryItemConnection


class ProductVariantNode(Node, DjangoObjectType):
    class Meta:
        model = ProductVariant
        filterset_class = ProductVariantFilter
        interfaces = (graphene.Node,)
        connection_class = ProductVariantConnection
