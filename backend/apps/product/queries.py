import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from apps.core.permissions import AllowAuthenticatedFilter


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
    price_list = graphene.Field(PriceListNode, id=graphene.ID())


class ProductTypeQuery:
    product_types = DjangoFilterConnectionField(ProductTypeNode)
    product_type = graphene.Field(ProductTypeNode, id=graphene.ID())


class ProductTagQuery:
    product_tags = DjangoFilterConnectionField(ProductTagNode)
    product_tag = graphene.Field(ProductTagNode, id=graphene.ID())


class ProductQuery:
    products = AllowAuthenticatedFilter(ProductNode)
    # product = graphene.Field(ProductNode, id=graphene.ID())
    product = graphene.relay.Node.Field(ProductNode)
    


class ImageQuery:
    images = DjangoFilterConnectionField(ImageNode)
    image = graphene.Field(ImageNode, id=graphene.ID())


class MoneyAmountQuery:
    money_amounts = DjangoFilterConnectionField(MoneyAmountNode)
    money_amount = graphene.Field(MoneyAmountNode, id=graphene.ID())


class ProductCategoryQuery:
    product_categorys = DjangoFilterConnectionField(ProductCategoryNode)
    product_category = graphene.Field(ProductCategoryNode, id=graphene.ID())


class ProductCollectionQuery:
    product_collections = DjangoFilterConnectionField(ProductCollectionNode)
    product_collection = graphene.Field(ProductCollectionNode, id=graphene.ID())


class ProductOptionValueQuery:
    product_option_values = DjangoFilterConnectionField(ProductOptionValueNode)
    product_option_value = graphene.Field(ProductOptionValueNode, id=graphene.ID())


class ProductOptionQuery:
    product_options = DjangoFilterConnectionField(ProductOptionNode)
    product_option = graphene.Field(ProductOptionNode, id=graphene.ID())


class ProductTaxRateQuery:
    product_tax_rates = DjangoFilterConnectionField(ProductTaxRateNode)
    product_tax_rate = graphene.Field(ProductTaxRateNode, id=graphene.ID())


class ProductTypeTaxRateQuery:
    product_type_tax_rates = DjangoFilterConnectionField(ProductTypeTaxRateNode)
    product_type_tax_rate = graphene.Field(ProductTypeTaxRateNode, id=graphene.ID())


class ProductVariantInventoryItemQuery:
    product_variant_inventory_items = DjangoFilterConnectionField(
        ProductVariantInventoryItemNode
    )
    product_variant_inventory_item = graphene.Field(
        ProductVariantInventoryItemNode, id=graphene.ID()
    )


class ProductVariantQuery:
    product_variants = DjangoFilterConnectionField(ProductVariantNode)
    product_variant = graphene.Field(ProductVariantNode, id=graphene.ID())


class Query(PriceListQuery, ProductTypeQuery, ProductTagQuery,
            ProductQuery, ImageQuery, MoneyAmountQuery,
            ProductCategoryQuery, ProductCollectionQuery,
            ProductOptionValueQuery, ProductOptionQuery, ProductTaxRateQuery,
            ProductTypeTaxRateQuery, ProductVariantInventoryItemQuery, ProductVariantQuery,
            ):
    pass
