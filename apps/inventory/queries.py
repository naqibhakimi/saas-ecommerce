import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
        AnalyticsConfigNode,
        BatchJobNode,
        FulfillmentNode,
        FulfillmentItemNode,
        FulfillmentProviderNode,
        TrackingLinkNode,
)

class AnalyticsConfigQuery:
        analytics_configs = DjangoConnectionField(AnalyticsConfigNode)
        analytics_config = graphene.Field(AnalyticsConfigNode, id=graphene.ID())
        
class BatchJobQuery:
        batch_jobs = DjangoConnectionField(BatchJobNode)
        batch_job = graphene.Field(BatchJobNode, id=graphene.ID())
        
        
class FulfillmentQuery:
        fulfillments = DjangoConnectionField(FulfillmentNode)
        fulfillment = graphene.Field(FulfillmentNode, id=graphene.ID())
        
        
class FulfillmentItemQuery:
        fulfillment_items = DjangoConnectionField(FulfillmentItemNode)
        fulfillment_item = graphene.Field(FulfillmentItemNode, id=graphene.ID())
        
class FulfillmentProviderQuery:
        fulfillment_providers = DjangoConnectionField(FulfillmentProviderNode)
        fulfillment_provider = graphene.Field(FulfillmentProviderNode, id=graphene.ID())
        
class TrackingLinkQuery:
        tracking_links = DjangoConnectionField(TrackingLinkNode)
        tracking_link = graphene.Field(TrackingLinkNode, id=graphene.ID())