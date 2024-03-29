from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    ShippingProfile,
    ShippingOption,
    ShippingMethod,
    CustomShippingOption,
    ShippingMethodTaxLine,
    ShippingOptionRequirement,
    ShippingTaxRate,
)
from .filters import (
    ShippingProfileFilter,
    ShippingOptionFilter,
    ShippingMethodFilter,
    CustomShippingOptionFilter,
    ShippingMethodTaxLineFilter,
    ShippingOptionRequirementFilter,
    ShippingTaxRateFilter,
)
from .connections import (
    ShippingProfileConnection,
    ShippingOptionConnection,
    ShippingMethodConnection,
    CustomShippingOptionConnection,
    ShippingMethodTaxLineConnection,
    ShippingOptionRequirementConnection,
    ShippingTaxRateConnection,
)


class ShippingProfileNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingProfile
        interfaces = (graphene.Node,)
        filterset_class = ShippingProfileFilter
        connection_class = ShippingProfileConnection


class ShippingOptionNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingOption
        interfaces = (graphene.Node,)
        filterset_class = ShippingOptionFilter
        connection_class = ShippingOptionConnection


class ShippingMethodNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingMethod
        interfaces = (graphene.Node,)
        filterset_class = ShippingMethodFilter
        connection_class = ShippingMethodConnection


class CustomShippingOptionNode(Node, DjangoObjectType):
    class Meta:
        model = CustomShippingOption
        interfaces = (graphene.Node,)
        filterset_class = CustomShippingOptionFilter
        connection_class = CustomShippingOptionConnection


class ShippingMethodTaxLineNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingMethodTaxLine
        interfaces = (graphene.Node,)
        filterset_class = ShippingMethodTaxLineFilter
        connection_class = ShippingMethodTaxLineConnection


class ShippingOptionRequirementNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingOptionRequirement
        interfaces = (graphene.Node,)
        filterset_class = ShippingOptionRequirementFilter
        connection_class = ShippingOptionRequirementConnection


class ShippingTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingTaxRate
        interfaces = (graphene.Node,)
        filterset_class = ShippingTaxRateFilter
        connection_class = ShippingTaxRateConnection
