import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import (
        SalesChannelNode,
        SalesChannelLocationNode,
        CartNode,
        InviteNode,
        NoteNode,
        NotificationProviderNode,
        NotificationNode,
        StagedJobNode,
        StoreNode,
        SwapNode,
)

class SalesChannelQuery:
        sales_channels = DjangoFilterConnectionField(SalesChannelNode)
        sales_channel = graphene.Field(SalesChannelNode, id=graphene.ID())
        
class CartQuery:
        carts = DjangoFilterConnectionField(CartNode)
        cart = graphene.Field(CartNode, id=graphene.ID())
        

class InviteQuery:
        invites = DjangoFilterConnectionField(InviteNode)
        invite = graphene.Field(InviteNode, id=graphene.ID())
        

class NoteQuery:
        notes = DjangoFilterConnectionField(NoteNode)
        note = graphene.Field(NoteNode, id=graphene.ID())
        
class NotificationProviderQuery:
        notification_providers = DjangoFilterConnectionField(NotificationProviderNode)
        notification_provider = graphene.Field(NotificationProviderNode, id=graphene.ID())
        
class NotificationQuery:
        notifications = DjangoFilterConnectionField(NotificationNode)
        notification = graphene.Field(NotificationNode, id=graphene.ID())

        
class SalesChannelLocationQuery:
        sales_channel_locations = DjangoFilterConnectionField(SalesChannelLocationNode)
        sales_channel_location = graphene.Field(SalesChannelLocationNode, id=graphene.ID())
        

class StagedJobQuery:
        staged_jobs = DjangoFilterConnectionField(StagedJobNode)
        staged_job = graphene.Field(StagedJobNode, id=graphene.ID())
        
class StoreQuery:
        stores = DjangoFilterConnectionField(StoreNode)
        store = graphene.Field(StoreNode, id=graphene.ID())
        
class SwapQuery:
        swaps = DjangoFilterConnectionField(SwapNode)
        swap = graphene.Field(SwapNode, id=graphene.ID())
        
