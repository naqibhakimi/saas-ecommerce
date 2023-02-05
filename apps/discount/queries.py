import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

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
        discounts = DjangoFilterConnectionField(DiscountNode)
        discount = graphene.Field(DiscountNode, id=graphene.ID())
        

class DiscountConditionCustomerGroupQuery:
        discount_condition_customer_groups = DjangoFilterConnectionField(DiscountConditionCustomerGroupNode)
        discount_condition_customer_group = graphene.Field(DiscountConditionCustomerGroupNode, id=graphene.ID())
        
class DiscountConditionProductCollectionQuery:
        discount_condition_product_collections = DjangoFilterConnectionField(DiscountConditionProductCollectionNode)
        discount_condition_product_collection = graphene.Field(DiscountConditionProductCollectionNode, id=graphene.ID())
        
class DiscountConditionProductTagQuery:
        discount_condition_product_tags = DjangoFilterConnectionField(DiscountConditionProductTagNode)
        discount_condition_product_tag = graphene.Field(DiscountConditionProductTagNode, id=graphene.ID())
    
class DiscountConditionProductTypeQuery:
        discount_condition_product_types = DjangoFilterConnectionField(DiscountConditionProductTypeNode)
        discount_condition_product_type = graphene.Field(DiscountConditionProductTypeNode, id=graphene.ID())
        
class DiscountConditionProductQuery:
        discount_condition_products = DjangoFilterConnectionField(DiscountConditionProductNode)
        discount_condition_product = graphene.Field(DiscountConditionProductNode, id=graphene.ID())
        
class DiscountConditionQuery:
        discount_conditions = DjangoFilterConnectionField(DiscountConditionNode)
        discount_condition = graphene.Field(DiscountConditionNode, id=graphene.ID())
        
class DiscountRuleQuery:
        discount_rules = DjangoFilterConnectionField(DiscountRuleNode)
        discount_rule = graphene.Field(DiscountRuleNode, id=graphene.ID())
        