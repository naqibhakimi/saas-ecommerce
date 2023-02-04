import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
    DiscountConditionNode,
    DiscountRuleNode,
    DiscountNode,
    DiscountConditionCustomerGroupNode,
    DiscountConditionProductCollectionNode,
    DiscountConditionProductTagNode,
    DiscountConditionProductTypeNode,
    DiscountConditionProductNode,
)
        
class DiscountQuery:
        discounts = DjangoConnectionField(DiscountNode)
        discount = graphene.Field(DiscountNode, id=graphene.ID())
        

class DiscountConditionCustomerGroupQuery:
        discount_condition_customer_groups = DjangoConnectionField(DiscountConditionCustomerGroupNode)
        discount_condition_customer_group = graphene.Field(DiscountConditionCustomerGroupNode, id=graphene.ID())
        
class DiscountConditionProductCollectionQuery:
        discount_condition_product_collections = DjangoConnectionField(DiscountConditionProductCollectionNode)
        discount_condition_product_collection = graphene.Field(DiscountConditionProductCollectionNode, id=graphene.ID())
        
class DiscountConditionProductTagQuery:
        discount_condition_product_tags = DjangoConnectionField(DiscountConditionProductTagNode)
        discount_condition_product_tag = graphene.Field(DiscountConditionProductTagNode, id=graphene.ID())
    
class DiscountConditionProductTypeQuery:
        discount_condition_product_types = DjangoConnectionField(DiscountConditionProductTypeNode)
        discount_condition_product_type = graphene.Field(DiscountConditionProductTypeNode, id=graphene.ID())
        
class DiscountConditionProductQuery:
        discount_condition_products = DjangoConnectionField(DiscountConditionProductNode)
        discount_condition_product = graphene.Field(DiscountConditionProductNode, id=graphene.ID())
        
class DiscountConditionQuery:
        discount_conditions = DjangoConnectionField(DiscountConditionNode)
        discount_condition = graphene.Field(DiscountConditionNode, id=graphene.ID())
        
class DiscountRuleQuery:
        discount_rules = DjangoConnectionField(DiscountRuleNode)
        discount_rule = graphene.Field(DiscountRuleNode, id=graphene.ID())
        