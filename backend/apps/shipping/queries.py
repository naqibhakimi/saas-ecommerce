import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

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
    shipping_methods = DjangoFilterConnectionField(ShippingMethodNode)
    shipping_method = graphene.Field(ShippingMethodNode, id=graphene.ID())


class ShippingOptionQuery:
    shipping_options = DjangoFilterConnectionField(ShippingOptionNode)
    shipping_option = graphene.Field(ShippingOptionNode, id=graphene.ID())


class CustomShippingOptionQuery:
    custom_shipping_options = DjangoFilterConnectionField(CustomShippingOptionNode)
    custom_shipping_option = graphene.Field(CustomShippingOptionNode, id=graphene.ID())


class ShippingMethodTaxLineQuery:
    shipping_method_tax_lines = DjangoFilterConnectionField(ShippingMethodTaxLineNode)
    shipping_method_tax_line = graphene.Field(
        ShippingMethodTaxLineNode, id=graphene.ID()
    )


class ShippingOptionRequirementQuery:
    shipping_option_requirements = DjangoFilterConnectionField(
        ShippingOptionRequirementNode
    )
    shipping_option_requirement = graphene.Field(
        ShippingOptionRequirementNode, id=graphene.ID()
    )


class ShippingProfileQuery:
    shipping_profiles = DjangoFilterConnectionField(ShippingProfileNode)
    shipping_profile = graphene.relay.Node.Field(ShippingProfileNode)


class ShippingTaxRateQuery:
    shipping_tax_rates = DjangoFilterConnectionField(ShippingTaxRateNode)
    shipping_tax_rate = graphene.Field(ShippingTaxRateNode, id=graphene.ID())


class Query(ShippingMethodQuery, ShippingOptionQuery,
            CustomShippingOptionQuery, ShippingMethodTaxLineQuery,
            ShippingOptionRequirementQuery,
            ShippingProfileQuery, ShippingTaxRateQuery,
            ):
    pass
