import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
        AnalyticsConfigNode,
        BatchJobNode,
        FulfillmentNode,
        FulfillmentItemNode,
        FulfillmentProviderNode,
        TrackingLinkNode,
)

class AnalyticsConfigQuery:
        analytics_configs = DjangoFilterConnectionField(AnalyticsConfigNode)
        analytics_config = graphene.Field(AnalyticsConfigNode, id=graphene.ID())
        
class BatchJobQuery:
        batch_jobs = DjangoFilterConnectionField(BatchJobNode)
        batch_job = graphene.Field(BatchJobNode, id=graphene.ID())
        
        
class FulfillmentQuery:
        fulfillments = DjangoFilterConnectionField(FulfillmentNode)
        fulfillment = graphene.Field(FulfillmentNode, id=graphene.ID())
        
        
class FulfillmentItemQuery:
        fulfillment_items = DjangoFilterConnectionField(FulfillmentItemNode)
        fulfillment_item = graphene.Field(FulfillmentItemNode, id=graphene.ID())
        
class FulfillmentProviderQuery:
        fulfillment_providers = DjangoFilterConnectionField(FulfillmentProviderNode)
        fulfillment_provider = graphene.Field(FulfillmentProviderNode, id=graphene.ID())
        
class TrackingLinkQuery:
        tracking_links = DjangoFilterConnectionField(TrackingLinkNode)
        tracking_link = graphene.Field(TrackingLinkNode, id=graphene.ID())