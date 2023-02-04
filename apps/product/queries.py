import graphene
from graphene_django.fields import DjangoConnectionField

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
        price_lists = DjangoConnectionField(PriceListNode)
        price_list = graphene.Field(PriceListNode, id=graphene.ID())
        
class ProductTypeQuery:
        product_types = DjangoConnectionField(ProductTypeNode)
        product_type = graphene.Field(ProductTypeNode, id=graphene.ID())
        
class ProductTagQuery:
        product_tags = DjangoConnectionField(ProductTagNode)
        product_tag = graphene.Field(ProductTagNode, id=graphene.ID())
        
class ProductQuery:
        products = DjangoConnectionField(ProductNode)
        product = graphene.Field(ProductNode, id=graphene.ID())
        
class ImageQuery:
        images = DjangoConnectionField(ImageNode)
        image = graphene.Field(ImageNode, id=graphene.ID())
        
class MoneyAmountQuery:
        money_amounts = DjangoConnectionField(MoneyAmountNode)
        money_amount = graphene.Field(MoneyAmountNode, id=graphene.ID())
        
class ProductCategoryQuery:
        product_categorys = DjangoConnectionField(ProductCategoryNode)
        product_category = graphene.Field(ProductCategoryNode, id=graphene.ID())
        
class ProductCollectionQuery:
        product_collections = DjangoConnectionField(ProductCollectionNode)
        product_collection = graphene.Field(ProductCollectionNode, id=graphene.ID())
        
class ProductOptionValueQuery:
        product_option_values = DjangoConnectionField(ProductOptionValueNode)
        product_option_value = graphene.Field(ProductOptionValueNode, id=graphene.ID())
        
class ProductOptionQuery:
        product_options = DjangoConnectionField(ProductOptionNode)
        product_option = graphene.Field(ProductOptionNode, id=graphene.ID())
        
class ProductTaxRateQuery:
        product_tax_rates = DjangoConnectionField(ProductTaxRateNode)
        product_tax_rate = graphene.Field(ProductTaxRateNode, id=graphene.ID())
        
class ProductTypeTaxRateQuery:
        product_type_tax_rates = DjangoConnectionField(ProductTypeTaxRateNode)
        product_type_tax_rate = graphene.Field(ProductTypeTaxRateNode, id=graphene.ID())
        
class ProductVariantInventoryItemQuery:
        product_variant_inventory_items = DjangoConnectionField(ProductVariantInventoryItemNode)
        product_variant_inventory_item = graphene.Field(ProductVariantInventoryItemNode, id=graphene.ID())
        
class ProductVariantQuery:
        product_variants = DjangoConnectionField(ProductVariantNode)
        product_variant = graphene.Field(ProductVariantNode, id=graphene.ID())
        