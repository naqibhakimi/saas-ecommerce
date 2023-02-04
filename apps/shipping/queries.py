import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
    ShippingProfileNode,
    ShippingOptionNode,
    ShippingMethodNode,
    CustomShippingOptionNode,
    ShippingMethodTaxLineNode,
    ShippingOptionRequirementNode,
    ShippingTaxRateNode,
)

class ShippingMethodQuery:
        shipping_methods = DjangoConnectionField(ShippingMethodNode)
        shipping_method = graphene.Field(ShippingMethodNode, id=graphene.ID())
        
class ShippingOptionQuery:
        shipping_options = DjangoConnectionField(ShippingOptionNode)
        shipping_option = graphene.Field(ShippingOptionNode, id=graphene.ID())
        
class CustomShippingOptionQuery:
        custom_shipping_options = DjangoConnectionField(CustomShippingOptionNode)
        custom_shipping_option = graphene.Field(CustomShippingOptionNode, id=graphene.ID())
        
class ShippingMethodTaxLineQuery:
        shipping_method_tax_lines = DjangoConnectionField(ShippingMethodTaxLineNode)
        shipping_method_tax_line = graphene.Field(ShippingMethodTaxLineNode, id=graphene.ID())
        
class ShippingOptionRequirementQuery:
        shipping_option_requirements = DjangoConnectionField(ShippingOptionRequirementNode)
        shipping_option_requirement = graphene.Field(ShippingOptionRequirementNode, id=graphene.ID())
        
class ShippingProfileQuery:
        shipping_profiles = DjangoConnectionField(ShippingProfileNode)
        shipping_profile = graphene.Field(ShippingProfileNode, id=graphene.ID())
        
class ShippingTaxRateQuery:
        shipping_tax_rates = DjangoConnectionField(ShippingTaxRateNode)
        shipping_tax_rate = graphene.Field(ShippingTaxRateNode, id=graphene.ID())
        