import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
        OrderDiscountNode,
        OrderGiftCardNode,
        OrderNode,
        OrderEditNode,
        OrderItemChangeNode,
        DraftOrderNode,
        ClaimOrderNode,
        ClaimTagNode,
        ClaimItemNode,
        ClaimImageNode,
        ReturnNode,
        ReturnItemNode,
        ReturnReasonNode,
)

class OrderDiscountQuery:
        order_discounts = DjangoConnectionField(OrderDiscountNode)
        order_discount = graphene.Field(OrderDiscountNode, id=graphene.ID())
        
class OrderGiftCardQuery:
        order_gift_cards = DjangoConnectionField(OrderGiftCardNode)
        order_gift_card = graphene.Field(OrderGiftCardNode, id=graphene.ID())
        
class OrderQuery:
        orders = DjangoConnectionField(OrderNode)
        order = graphene.Field(OrderNode, id=graphene.ID())
        
class ClaimTagQuery:
        claim_tags = DjangoConnectionField(ClaimTagNode)
        claim_tag = graphene.Field(ClaimTagNode, id=graphene.ID())
        
class ClaimItemQuery:
        claim_items = DjangoConnectionField(ClaimItemNode)
        claim_item = graphene.Field(ClaimItemNode, id=graphene.ID())
        
class ClaimImageQuery:
        claim_images = DjangoConnectionField(ClaimImageNode)
        claim_image = graphene.Field(ClaimImageNode, id=graphene.ID())
        
class ClaimOrderQuery:
        claim_orders = DjangoConnectionField(ClaimOrderNode)
        claim_order = graphene.Field(ClaimOrderNode, id=graphene.ID())
        
class ReturnQuery:
        returns = DjangoConnectionField(ReturnNode)
        return_ = graphene.Field(ReturnNode, id=graphene.ID())
        
class DraftOrderQuery:
        draft_orders = DjangoConnectionField(DraftOrderNode)
        draft_order = graphene.Field(DraftOrderNode, id=graphene.ID())
        
class OrderEditQuery:
        order_edits = DjangoConnectionField(OrderEditNode)
        order_edit = graphene.Field(OrderEditNode, id=graphene.ID())
        
class OrderItemChangeQuery:
        order_item_changes = DjangoConnectionField(OrderItemChangeNode)
        order_item_change = graphene.Field(OrderItemChangeNode, id=graphene.ID())
  
class ReturnItemQuery:
        return_items = DjangoConnectionField(ReturnItemNode)
        return_item = graphene.Field(ReturnItemNode, id=graphene.ID())
        
class ReturnReasonQuery:
        return_reasons = DjangoConnectionField(ReturnReasonNode)
        return_reason = graphene.Field(ReturnReasonNode, id=graphene.ID())
        