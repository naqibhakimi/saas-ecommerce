import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

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
        order_discounts = DjangoFilterConnectionField(OrderDiscountNode)
        order_discount = graphene.Field(OrderDiscountNode, id=graphene.ID())
        
class OrderGiftCardQuery:
        order_gift_cards = DjangoFilterConnectionField(OrderGiftCardNode)
        order_gift_card = graphene.Field(OrderGiftCardNode, id=graphene.ID())
        
class OrderQuery:
        orders = DjangoFilterConnectionField(OrderNode)
        order = graphene.Field(OrderNode, id=graphene.ID())
        
class ClaimTagQuery:
        claim_tags = DjangoFilterConnectionField(ClaimTagNode)
        claim_tag = graphene.Field(ClaimTagNode, id=graphene.ID())
        
class ClaimItemQuery:
        claim_items = DjangoFilterConnectionField(ClaimItemNode)
        claim_item = graphene.Field(ClaimItemNode, id=graphene.ID())
        
class ClaimImageQuery:
        claim_images = DjangoFilterConnectionField(ClaimImageNode)
        claim_image = graphene.Field(ClaimImageNode, id=graphene.ID())
        
class ClaimOrderQuery:
        claim_orders = DjangoFilterConnectionField(ClaimOrderNode)
        claim_order = graphene.Field(ClaimOrderNode, id=graphene.ID())
        
class ReturnQuery:
        returns = DjangoFilterConnectionField(ReturnNode)
        return_ = graphene.Field(ReturnNode, id=graphene.ID())
        
class DraftOrderQuery:
        draft_orders = DjangoFilterConnectionField(DraftOrderNode)
        draft_order = graphene.Field(DraftOrderNode, id=graphene.ID())
        
class OrderEditQuery:
        order_edits = DjangoFilterConnectionField(OrderEditNode)
        order_edit = graphene.Field(OrderEditNode, id=graphene.ID())
        
class OrderItemChangeQuery:
        order_item_changes = DjangoFilterConnectionField(OrderItemChangeNode)
        order_item_change = graphene.Field(OrderItemChangeNode, id=graphene.ID())
  
class ReturnItemQuery:
        return_items = DjangoFilterConnectionField(ReturnItemNode)
        return_item = graphene.Field(ReturnItemNode, id=graphene.ID())
        
class ReturnReasonQuery:
        return_reasons = DjangoFilterConnectionField(ReturnReasonNode)
        return_reason = graphene.Field(ReturnReasonNode, id=graphene.ID())
        