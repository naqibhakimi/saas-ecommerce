import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin


from apps.customer.mixins import (
    CreateCustomerMixin,
    CreateCustomerGroupMixin,
    CreateCountryMixin,
    CreateAddressMixin,
    CreateRegionMixin
)
from apps.customer.mixins import UpdateCustomerMixin
from apps.customer.types import (
    CustomerNode,
    CustomerGroupNode,
    CountryNode,
    AddressNode,
    RegionNode,
)
from apps.customer.forms import DeleteCustomerForm
from apps.customer.mixins import DeleteCustomerMixin


class CreateCustomer(DynamicInputMixin, RelayMutationMixin, CreateCustomerMixin, graphene.ClientIDMutation):
    __doc__ = CreateCustomerMixin.__doc__
    # [FIXME: This]
    # _inputs = {'customer': CustomerNode}
    _inputs = {"billing_address": graphene.String, "phone": graphene.String, "has_account": graphene.String,
               "password_hash": graphene.String, "orders": graphene.String, "groups": graphene.String, "metadata": graphene.String}
    _required_inputs = {"email": graphene.String,
                        "first_name": graphene.String, "last_name": graphene.String, }


class UpdateCustomer(DynamicInputMixin, RelayMutationMixin, UpdateCustomerMixin, graphene.ClientIDMutation):
    # [FIXME:]
    # _inputs = {'customer': CustomerNode}
    _inputs = {"billing_address": graphene.String, "phone": graphene.String, "has_account": graphene.String,
               "password_hash": graphene.String, "order": graphene.String, "groups": graphene.String, "metadata": graphene.JSONString}


class DeleteCustomer(DynamicInputMixin, RelayMutationMixin, DeleteCustomerMixin, graphene.ClientIDMutation):
    _required_inputs = {"id": graphene.ID}


class CreateCustomerGroup(DynamicInputMixin, RelayMutationMixin, CreateCustomerGroupMixin, graphene.ClientIDMutation):
    _inputs = {"CustomerGroup": CustomerGroupNode}


class CreateCountry(DynamicInputMixin, RelayMutationMixin, CreateCountryMixin, graphene.ClientIDMutation):
    _inputs = {"Country": CountryNode}


class CreateAddress(DynamicInputMixin, RelayMutationMixin, CreateAddressMixin, graphene.ClientIDMutation):
    _inputs = {"Address": AddressNode}


class CreateRegion(DynamicInputMixin, RelayMutationMixin, CreateRegionMixin, graphene.ClientIDMutation):
    _inputs = {"Region": RegionNode}


class Mutation(object):
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
    # delete_customer = DeleteCustomer.Field()
    create_customerGroup = CreateCustomerGroup.Field()
    # update_customerGroup = UpdateCustomerGroup.Field()
    # delete_customerGroup = DeleteCustomerGroup.Field()
    create_country = CreateCountry.Field()
    # update_country = UpdateCountry.Field()
    # delete_country = DeleteCountry.Field()
    create_address = CreateAddress.Field()
    # update_address = UpdateAddress.Field()
    # delete_address = DeleteAddress.Field()
    create_region = CreateRegion.Field()
    # update_region = UpdateRegion.Field()
    # delete_region = DeleteRegion.Field()
