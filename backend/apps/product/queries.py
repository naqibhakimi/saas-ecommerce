import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from apps.core.permissions import AllowAuthenticated


from .types import (
    PriceListNode,
    MoneyAmountNode,
    ProductTypeNode,
    ProductTagNode,
    ImageNode,
    ProductNode,
    ProductCategoryNode,
    ProductCollectionNode,
    ProductOptionNode,
    ProductOptionValueNode,
    ProductTaxRateNode,
    ProductTypeTaxRateNode,
    ProductVariantInventoryItemNode,
    ProductVariantNode,
)


class PriceListQuery:
    price_lists = DjangoFilterConnectionField(PriceListNode)
    price_list = graphene.relay.Node.Field(PriceListNode)


class ProductTypeQuery:
    product_types = DjangoFilterConnectionField(ProductTypeNode)
    product_type = graphene.relay.Node.Field(ProductTypeNode)
    


class ProductTagQuery:
    product_tags = DjangoFilterConnectionField(ProductTagNode)
    product_tag = graphene.relay.Node.Field(ProductTagNode)


class ProductQuery:
    products = DjangoFilterConnectionField(ProductNode)
    product = graphene.relay.Node.Field(ProductNode)
    


class ImageQuery:
    images = DjangoFilterConnectionField(ImageNode)
    image = graphene.relay.Node.Field(ImageNode)


class MoneyAmountQuery:
    money_amounts = DjangoFilterConnectionField(MoneyAmountNode)
    money_amount = graphene.relay.Node.Field(MoneyAmountNode)

class ProductCategoryQuery:
    product_categories = DjangoFilterConnectionField(ProductCategoryNode)
    product_category = graphene.relay.Node.Field(ProductCategoryNode)


class ProductCollectionQuery:
    product_collections = DjangoFilterConnectionField(ProductCollectionNode)
    product_collection = graphene.Field(ProductCollectionNode, id=graphene.ID())


class ProductOptionValueQuery:
    product_option_values = DjangoFilterConnectionField(ProductOptionValueNode)
    product_option_value = graphene.relay.Node.Field(ProductOptionValueNode)


class ProductOptionQuery:
    product_options = DjangoFilterConnectionField(ProductOptionNode)
    product_option = graphene.relay.Node.Field(ProductOptionNode)


class ProductTaxRateQuery:
    product_tax_rates = DjangoFilterConnectionField(ProductTaxRateNode)
    product_tax_rate = graphene.relay.Node.Field(ProductTaxRateNode)


class ProductTypeTaxRateQuery:
    product_type_tax_rates = DjangoFilterConnectionField(ProductTypeTaxRateNode)
    product_type_tax_rate = graphene.relay.Node.Field(ProductTypeTaxRateNode)


class ProductVariantInventoryItemQuery:
    product_variant_inventory_items = DjangoFilterConnectionField(
        ProductVariantInventoryItemNode
    )
    product_variant_inventory_item = graphene.relay.Node.Field(ProductVariantInventoryItemNode)


class ProductVariantQuery:
    product_variants = DjangoFilterConnectionField(ProductVariantNode)
    product_variant = graphene.relay.Node.Field(ProductVariantNode)


class Query(PriceListQuery, ProductTypeQuery, ProductTagQuery,
            ProductQuery, ImageQuery, MoneyAmountQuery,
            ProductCategoryQuery, ProductCollectionQuery,
            ProductOptionValueQuery, ProductOptionQuery, ProductTaxRateQuery,
            ProductTypeTaxRateQuery, ProductVariantInventoryItemQuery, ProductVariantQuery,
            ):
    pass
