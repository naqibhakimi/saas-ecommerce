from graphene_django import DjangoObjectType
import graphene

from apps.core.types import Node

from .models import (
    SalesChannel,
    SalesChannelLocation,
    Cart,
    Invite,
    Note,
    NotificationProvider,
    Notification,
    StagedJob,
    Store,
    Swap,
)
from .filters import (
    SalesChannelFilter,
    SalesChannelLocationFilter,
    CartFilter,
    InviteFilter,
    NoteFilter,
    NotificationProviderFilter,
    NotificationFilter,
    StagedJobFilter,
    StoreFilter,
    SwapFilter,
)
from .connections import (
    SalesChannelConnection,
    SalesChannelLocationConnection,
    CartConnection,
    InviteConnection,
    NoteConnection,
    NotificationProviderConnection,
    NotificationConnection,
    StagedJobConnection,
    StoreConnection,
    SwapConnection,
)



class SalesChannelNode(Node, DjangoObjectType):
    class Meta:
        model =  SalesChannel
        interfaces =  (graphene.Node,)
        filterset_class = SalesChannelFilter 
        connection_class = SalesChannelConnection


class SalesChannelLocationNode(Node, DjangoObjectType):
    class Meta:
        model =  SalesChannelLocation
        interfaces =  (graphene.Node,)
        filterset_class = SalesChannelLocationFilter 
        connection_class = SalesChannelLocationConnection


class CartNode(Node, DjangoObjectType):
    class Meta:
        model= Cart
        interfaces= (graphene.Node,)
        filterset_class = CartFilter 
        connection_class = CartConnection


class InviteNode(Node, DjangoObjectType):
    class Meta:
        model= Invite
        interfaces= (graphene.Node,)
        filterset_class = InviteFilter 
        connection_class = InviteConnection


class NoteNode(DjangoObjectType):
    class Meta:
        model= Note
        interfaces= (graphene.Node,)
        filterset_class = NoteFilter 
        connection_class = NoteConnection


class NotificationProviderNode(Node, DjangoObjectType):
    class Meta:
        model =  Notification
        interfaces =  (graphene.Node,)
        filterset_class = NotificationFilter 
        connection_class = NotificationProviderConnection


class NotificationNode(Node, DjangoObjectType):
    class Meta:
        model =  Notification
        interfaces =  (graphene.Node,)
        filterset_class = NotificationFilter 
        connection_class = NotificationConnection


class StagedJobNode(Node, DjangoObjectType):
    class Meta:
        model =  StagedJob
        interfaces =  (graphene.Node,)
        filterset_class = StagedJobFilter 
        connection_class = StagedJobConnection


class StoreNode(Node, DjangoObjectType):
    class Meta:
        model =  Store
        interfaces =  (graphene.Node,)
        filterset_class = StoreFilter 
        connection_class = StoreConnection


class SwapNode(Node, DjangoObjectType):
    class Meta:
        model =  Swap
        interfaces =  (graphene.Node,)
        filterset_class = SwapFilter 
        connection_class = SwapConnection