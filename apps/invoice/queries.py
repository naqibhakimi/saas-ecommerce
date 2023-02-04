import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
        LineItemNode,
        LineItemAdjustmentNode,
        LineItemTaxLineNode,
)

class LineItemQuery:
        line_items = DjangoConnectionField(LineItemNode)
        line_item = graphene.Field(LineItemNode, id=graphene.ID())
        
        
class LineItemAdjustmentQuery:
        line_item_adjustments = DjangoConnectionField(LineItemAdjustmentNode)
        line_item_adjustment = graphene.Field(LineItemAdjustmentNode, id=graphene.ID())
        

class LineItemTaxLineQuery:
        line_item_tax_lines = DjangoConnectionField(LineItemTaxLineNode)
        line_item_tax_line = graphene.Field(LineItemTaxLineNode, id=graphene.ID())
    