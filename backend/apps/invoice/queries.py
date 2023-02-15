import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
        LineItemNode,
        LineItemAdjustmentNode,
        LineItemTaxLineNode,
)

class LineItemQuery:
        line_items = DjangoFilterConnectionField(LineItemNode)
        line_item = graphene.Field(LineItemNode, id=graphene.ID())
        
        
class LineItemAdjustmentQuery:
        line_item_adjustments = DjangoFilterConnectionField(LineItemAdjustmentNode)
        line_item_adjustment = graphene.Field(LineItemAdjustmentNode, id=graphene.ID())
        

class LineItemTaxLineQuery:
        line_item_tax_lines = DjangoFilterConnectionField(LineItemTaxLineNode)
        line_item_tax_line = graphene.Field(LineItemTaxLineNode, id=graphene.ID())
    