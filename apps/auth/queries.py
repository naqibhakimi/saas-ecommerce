import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField

from .types import UserNode


class Query:
    users = DjangoFilterConnectionField(UserNode, 'users')


class Mutation:
    pass



import graphene
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from core.utils import convert_fields
# from secure_auth.models import Company
from django.db.models import Q
# from apps.auth.types import CompanyNode, UserNode
from apps.auth.types import UserNode


class UserQuery(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)


class MeQuery(graphene.ObjectType):
    me = graphene.Field(UserNode)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_authenticated:
            user.owner = user.employee.first()
            return user
        return None
    
    
    
# class CompanyQuery(graphene.ObjectType):
#     get_company_by_domain = graphene.Field(CompanyNode , **convert_fields(Company, only_fields=["domain", 'brand_domain']),)
#     def resolve_get_company_by_domain(self, info, **kwargs):
#         return Company.objects.get((Q(domain=kwargs.get('domain')) | Q(brand_domain=kwargs.get('brand_domain'))) & Q(brand_domain__isnull=False))
