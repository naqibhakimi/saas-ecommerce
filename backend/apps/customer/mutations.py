import graphene
from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .forms import DeleteCustomerForm
from .inputs import CreateCustomerInputField, UpdateCustomerGroupInputField, UpdateCustomerInputField
from .mixins import (CreateAddressMixin, CreateCountryMixin,
                     CreateCustomerGroupMixin, CreateCustomerMixin,
                     CreateRegionMixin, DeleteCustomerMixin,
                     UpdateCustomerMixin)
from .types import (AddressNode, CountryNode, CustomerGroupNode, CustomerNode,
                    RegionNode)


class CreateCustomer(DynamicInputMixin, RelayMutationMixin, CreateCustomerMixin, graphene.ClientIDMutation):
    __doc__ = CreateCustomerMixin.__doc__
    _inputs = {}
    _required_inputs = {"customer": CreateCustomerInputField}


class UpdateCustomer(DynamicInputMixin, RelayMutationMixin, UpdateCustomerMixin, graphene.ClientIDMutation):
    _inputs = {}
    _required_inputs = {"customer": UpdateCustomerInputField}


class DeleteCustomer(DynamicInputMixin, RelayMutationMixin, DeleteCustomerMixin, graphene.ClientIDMutation):
    _required_inputs = {"id": graphene.ID}


class CreateCustomerGroup(DynamicInputMixin, RelayMutationMixin, CreateCustomerGroupMixin, graphene.ClientIDMutation):
    _inputs = {"CustomerGroup": UpdateCustomerGroupInputField}


# class CreateCountry(DynamicInputMixin, RelayMutationMixin, CreateCountryMixin, graphene.ClientIDMutation):
#     _inputs = {"Country": CountryNode}


# class CreateAddress(DynamicInputMixin, RelayMutationMixin, CreateAddressMixin, graphene.ClientIDMutation):
#     _inputs = {"Address": AddressNode}


# class CreateRegion(DynamicInputMixin, RelayMutationMixin, CreateRegionMixin, graphene.ClientIDMutation):
#     _inputs = {"Region": RegionNode}


class Mutation(object):
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
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
