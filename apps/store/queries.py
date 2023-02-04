import graphene
from graphene_django.fields import DjangoConnectionField

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
        sales_channels = DjangoConnectionField(SalesChannelNode)
        sales_channel = graphene.Field(SalesChannelNode, id=graphene.ID())
        
class CartQuery:
        carts = DjangoConnectionField(CartNode)
        cart = graphene.Field(CartNode, id=graphene.ID())
        

class InviteQuery:
        invites = DjangoConnectionField(InviteNode)
        invite = graphene.Field(InviteNode, id=graphene.ID())
        

class NoteQuery:
        notes = DjangoConnectionField(NoteNode)
        note = graphene.Field(NoteNode, id=graphene.ID())
        
class NotificationProviderQuery:
        notification_providers = DjangoConnectionField(NotificationProviderNode)
        notification_provider = graphene.Field(NotificationProviderNode, id=graphene.ID())
        
class NotificationQuery:
        notifications = DjangoConnectionField(NotificationNode)
        notification = graphene.Field(NotificationNode, id=graphene.ID())

        
class SalesChannelLocationQuery:
        sales_channel_locations = DjangoConnectionField(SalesChannelLocationNode)
        sales_channel_location = graphene.Field(SalesChannelLocationNode, id=graphene.ID())
        

class StagedJobQuery:
        staged_jobs = DjangoConnectionField(StagedJobNode)
        staged_job = graphene.Field(StagedJobNode, id=graphene.ID())
        
class StoreQuery:
        stores = DjangoConnectionField(StoreNode)
        store = graphene.Field(StoreNode, id=graphene.ID())
        
class SwapQuery:
        swaps = DjangoConnectionField(SwapNode)
        swap = graphene.Field(SwapNode, id=graphene.ID())
        
