import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateCustomerMixin
from .types import CustomerNode

from graphene_django.forms.mutation import DjangoModelDjangoFormMutationOptions, DjangoModelFormMutation

# class UpdateCustomer(UpdateCustomerMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation):
#     _inputs = {'customer': CustomerNode}
#     _inputs = {"id": graphene.ID , "email": graphene.String , "first_name": graphene.String }

#     _required_inputs = {}


# email
# first_name
# last_name
# billing_address
# phone
# has_account
# password_hash
# orders
# groups
# metadata



class Mutation:
    pass
    # update_address = UpdateAddress.Field()