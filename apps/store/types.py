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
        filterset_class = SalesChannelFilter 
        interfaces = SalesChannelConnection


class SalesChannelLocationNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = SalesChannelLocationFilter 
        interfaces = SalesChannelLocationConnection


class CartNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = CartFilter 
        interfaces = CartConnection


class InviteNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = InviteFilter 
        interfaces = InviteConnection


class NoteNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = NoteFilter 
        interfaces = NoteConnection


class NotificationProviderNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = NotificationProviderFilter 
        interfaces = NotificationProviderConnection


class NotificationNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = NotificationFilter 
        interfaces = NotificationConnection


class StagedJobNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = StagedJobFilter 
        interfaces = StagedJobConnection


class StoreNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = StoreFilter 
        interfaces = StoreConnection


class SwapNode(Node, DjangoObjectType):
    class Meta:
        filterset_class = SwapFilter 
        interfaces = SwapConnection