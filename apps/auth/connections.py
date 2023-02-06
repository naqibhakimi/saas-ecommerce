import graphene

from apps.core.connections import BaseConnection


class UserConnection(BaseConnection):
    class Meta:
        abstract = True