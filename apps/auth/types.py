import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphene_django.utils import camelize
from .connections import SEUserConnection
from .exceptions import WrongUsage
from .filters import SEUserFilter, UserStatusFilter
from .models import SEUser, UserStatus


class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        interfaces = (graphene.Node,)
        filterset_class = SEUserFilter
        connection_class = SEUserConnection

    pk = graphene.Int()
    archived = graphene.Boolean()
    verified = graphene.Boolean()
    secondary_email = graphene.String()

    def resolve_pk(self, info):
        return self.pk

    def resolve_archived(self, info):
        return self.status.archived

    def resolve_verified(self, info):
        return self.status.verified

    def resolve_secondary_email(self, info):
        return self.status.secondary_email

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related("status")


class UserStatusNode(DjangoObjectType):
    class Meta:
        model = UserStatus
        interfaces = (graphene.Node,)
        filterset_class = UserStatusFilter
