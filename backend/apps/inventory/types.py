from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    AnalyticsConfig,
    BatchJob,
    Fulfillment,
    FulfillmentItem,
    FulfillmentProvider,
    TrackingLink,
)
from .connections import (
    AnalyticsConfigConnection,
    BatchJobConnection,
    FulfillmentConnection,
    FulfillmentItemConnection,
    FulfillmentProviderConnection,
    TrackingLinkConnection,
)

from .filters import (
    AnalyticsConfigFilter,
    BatchJobFilter,
    FulfillmentFilter,
    FulfillmentItemFilter,
    FulfillmentProviderFilter,
    TrackingLinkFilter,
)


class AnalyticsConfigNode(Node, DjangoObjectType):
    class Meta:
        model = AnalyticsConfig
        filterset_class = AnalyticsConfigFilter
        interfaces = (graphene.Node,)
        connection_class = AnalyticsConfigConnection


class BatchJobNode(Node, DjangoObjectType):
    class Meta:
        model = BatchJob
        filterset_class = BatchJobFilter
        interfaces = (graphene.Node,)
        connection_class = BatchJobConnection


class FulfillmentNode(Node, DjangoObjectType):
    class Meta:
        model = Fulfillment
        filterset_class = FulfillmentFilter
        interfaces = (graphene.Node,)
        connection_class = FulfillmentConnection


class FulfillmentItemNode(Node, DjangoObjectType):
    class Meta:
        model = FulfillmentItem
        filterset_class = FulfillmentItemFilter
        interfaces = (graphene.Node,)
        connection_class = FulfillmentItemConnection


class FulfillmentProviderNode(Node, DjangoObjectType):
    class Meta:
        model = FulfillmentProvider
        filterset_class = FulfillmentProviderFilter
        interfaces = (graphene.Node,)
        connection_class = FulfillmentProviderConnection


class TrackingLinkNode(Node, DjangoObjectType):
    class Meta:
        model = TrackingLink
        filterset_class = TrackingLinkFilter
        interfaces = (graphene.Node,)
        connection_class = TrackingLinkConnection
