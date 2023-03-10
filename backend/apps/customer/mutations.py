import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin


from graphene_django.forms.mutation import DjangoModelFormMutation, ErrorType
from apps.core.mutations import AbstractMutation
from apps.customer.mixins import CreateCustomerMixin
from backend.apps.customer.mixins import UpdateCustomerMixin
from backend.apps.customer.types import CustomerNode


class CreateCustomer(DynamicInputMixin, RelayMutationMixin, CreateCustomerMixin, graphene.ClientIDMutation):
    __doc__ = CreateCustomerMixin.__doc__
    # [FIXME: This]
    # _inputs = {'customer': CustomerNode}
    _inputs = {"billing_address": graphene.String, "phone": graphene.String, "has_account": graphene.String,
               "password_hash": graphene.String, "orders": graphene.String, "groups": graphene.String, "metadata": graphene.String}
    _required_inputs = {"email": graphene.String,
                        "first_name": graphene.String, "last_name": graphene.String, }


class UpdateCustomer(UpdateCustomerMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation):
    _inputs = {'customer': CustomerNode}
    # _inputs = {"id": graphene.ID, "email": graphene.String,
    #            "first_name": graphene.String}


class Mutation(object):
    create_customer = CreateCustomer.Field()
    # delete_customer = DeleteCustomer.Field()
    # create_customerGroup = CreateCustomerGroup.Field()
    # update_customerGroup = UpdateCustomerGroup.Field()
    # delete_customerGroup = DeleteCustomerGroup.Field()
    # create_country = CreateCountry.Field()
    # update_country = UpdateCountry.Field()
    # delete_country = DeleteCountry.Field()
    # create_address = CreateAddress.Field()
    # update_address = UpdateAddress.Field()
    # delete_address = DeleteAddress.Field()
    # create_region = CreateRegion.Field()
    # update_region = UpdateRegion.Field()
    # delete_region = DeleteRegion.Field()
