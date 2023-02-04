import django_filters

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

class SalesChannelFilter(django_filters.FilterSet):
    class Meta:
        model = SalesChannel
        exclude = ('metadata')


class SalesChannelLocationFilter(django_filters.FilterSet):
    class Meta:
        model = SalesChannelLocation
        exclude = ('metadata')


class CartFilter(django_filters.FilterSet):
    class Meta:
        model = Cart
        exclude = ('metadata')


class InviteFilter(django_filters.FilterSet):
    class Meta:
        model = Invite
        exclude = ('metadata')


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        exclude = ('metadata')


class NotificationProviderFilter(django_filters.FilterSet):
    class Meta:
        model = NotificationProvider
        exclude = ('metadata')


class NotificationFilter(django_filters.FilterSet):
    class Meta:
        model = Notification
        exclude = ('metadata')


class StagedJobFilter(django_filters.FilterSet):
    class Meta:
        model = StagedJob
        exclude = ('metadata')


class StoreFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        exclude = ('metadata')


class SwapFilter(django_filters.FilterSet):
    class Meta:
        model = Swap
        exclude = ('metadata')

