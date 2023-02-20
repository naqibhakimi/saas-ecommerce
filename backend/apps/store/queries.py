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
    sales_channel = graphene.relay.Node.Field(SalesChannelNode)


class CartQuery:
    carts = DjangoFilterConnectionField(CartNode)
    cart = graphene.relay.Node.Field(CartNode)


class InviteQuery:
    invites = DjangoFilterConnectionField(InviteNode)
    invite = graphene.relay.Node.Field(InviteNode)


class NoteQuery:
    notes = DjangoFilterConnectionField(NoteNode)
    note = graphene.relay.Node.Field(NoteNode)


class NotificationProviderQuery:
    notification_providers = DjangoFilterConnectionField(NotificationProviderNode)
    notification_provider = graphene.relay.Node.Field(NotificationProviderNode)


class NotificationQuery:
    notifications = DjangoFilterConnectionField(NotificationNode)
    notification = graphene.relay.Node.Field(NotificationNode)


class SalesChannelLocationQuery:
    sales_channel_locations = DjangoFilterConnectionField(SalesChannelLocationNode)
    sales_channel_location = graphene.relay.Node.Field(SalesChannelLocationNode)


class StagedJobQuery:
    staged_jobs = DjangoFilterConnectionField(StagedJobNode)
    staged_job = graphene.relay.Node.Field(StagedJobNode)


class StoreQuery:
    stores = DjangoFilterConnectionField(StoreNode)
    store = graphene.relay.Node.Field(StoreNode)


class SwapQuery:
    swaps = DjangoFilterConnectionField(SwapNode)
    swap = graphene.relay.Node.Field(SwapNode)
