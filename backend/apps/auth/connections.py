import graphene

from apps.core.connections import BaseConnection


class SEUserConnection(BaseConnection):
    class Meta:
        abstract = True
