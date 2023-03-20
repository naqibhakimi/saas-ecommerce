import graphene
from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .forms import DeleteCustomerForm
from .inputs import CreateAddressInputField, CreateCountryInputField, CreateCustomerGroupInputField, CreateCustomerInputField, UpdateAddressInputField, UpdateCountryInputField, UpdateCustomerGroupInputField, UpdateCustomerInputField
from .mixins import (CreateAddressMixin, CreateCountryMixin,
                     CreateCustomerGroupMixin, CreateCustomerMixin,
                     CreateRegionMixin, DeleteAddressMixin, DeleteCountryMixin, DeleteCustomerGroupMixin, DeleteCustomerMixin, UpdateAddressMixin, UpdateCountryMixin, UpdateCustomerGroupMixin,
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
    _inputs = {"customer_group": CreateCustomerGroupInputField}
    _required_inputs = {}


class UpdateCustomerGroup(DynamicInputMixin, RelayMutationMixin, UpdateCustomerGroupMixin, graphene.ClientIDMutation):
   # [FIXME: ]
    _inputs = {"customer_group": UpdateCustomerGroupInputField}
    _required_inputs = {}


class DeleteCustomerGroup(DynamicInputMixin, RelayMutationMixin, DeleteCustomerGroupMixin, graphene.ClientIDMutation):
    _required_inputs = {"id": graphene.ID}


class CreateCountry(DynamicInputMixin, RelayMutationMixin, CreateCountryMixin, graphene.ClientIDMutation):
    __docs__ = CreateCountryMixin.__doc__
    _inputs = {"country": CreateCountryInputField}
    _required_inputs = {}


class UpdateCountry(DynamicInputMixin, RelayMutationMixin, UpdateCountryMixin, graphene.ClientIDMutation):
    _inputs = {"country": UpdateCountryInputField}
    _required_inputs = {}
    # [FIXME:]


class DeleteCountry(DynamicInputMixin, RelayMutationMixin, DeleteCountryMixin, graphene.ClientIDMutation):
    _required_inputs = {"id": graphene.ID}


class CreateAddress(DynamicInputMixin, RelayMutationMixin, CreateAddressMixin, graphene.ClientIDMutation):
    __docs__ = CreateAddressMixin.__doc__
    _inputs = {"Address": CreateAddressInputField}


class DeleteAddress(DynamicInputMixin, RelayMutationMixin, DeleteAddressMixin, graphene.ClientIDMutation):
    __docs__ = DeleteAddressMixin.__doc__
    _required_inputs = {"id": graphene.ID}


class UpdateAddress(DynamicInputMixin, RelayMutationMixin, UpdateAddressMixin, graphene.ClientIDMutation):
    _inputs = {"Address": UpdateAddressInputField}
    _required_inputs = {}


# class CreateRegion(DynamicInputMixin, RelayMutationMixin, CreateRegionMixin, graphene.ClientIDMutation):
#     _inputs = {"Region": RegionNode}


class Mutation(object):
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
    create_customer_group = CreateCustomerGroup.Field()
    update_customer_group = UpdateCustomerGroup.Field()
    delete_customerGroup = DeleteCustomerGroup.Field()
    create_country = CreateCountry.Field()
    update_country = UpdateCountry.Field()
    delete_country = DeleteCountry.Field()
    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()
    delete_address = DeleteAddress.Field()
    # create_region = CreateRegion.Field()
    # update_region = UpdateRegion.Field()
    # delete_region = DeleteRegion.Field()
