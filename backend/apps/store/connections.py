import graphene


class BaseConnection(graphene.Connection):
    class Meta:
        abstract = True


class SalesChannelConnection(BaseConnection):
    class Meta:
        abstract = True


class SalesChannelLocationConnection(BaseConnection):
    class Meta:
        abstract = True


class CartConnection(BaseConnection):
    class Meta:
        abstract = True


class InviteConnection(BaseConnection):
    class Meta:
        abstract = True


class NoteConnection(BaseConnection):
    class Meta:
        abstract = True


class NotificationProviderConnection(BaseConnection):
    class Meta:
        abstract = True


class NotificationConnection(BaseConnection):
    class Meta:
        abstract = True


class StagedJobConnection(BaseConnection):
    class Meta:
        abstract = True


class StoreConnection(BaseConnection):
    class Meta:
        abstract = True


class SwapConnection(BaseConnection):
    class Meta:
        abstract = True
