import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin


from graphene_django.forms.mutation import DjangoModelFormMutation, ErrorType
from apps.core.mutations import AbstractMutation

from .types import CustomerNode

from .forms import (
    CreateCustomerForm,
    # CreateCustomerGroupForm,
    # CreateCountryForm,
    # CreateAddressForm,
    # CreateRegionForm,
)



class CreateCustomer(AbstractMutation):

    class Meta:
        form_class = CreateCustomerForm



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


class Query(object):
    pass 

class Mutation(object):
    create_customer = CreateCustomer.Field()