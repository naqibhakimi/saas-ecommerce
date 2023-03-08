import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin


from graphene_django.forms.mutation import DjangoModelFormMutation, ErrorType
from apps.core.mutations import AbstractMutation

from .types import CustomerNode

from .forms import (
    CreateCustomerForm,
    UpdateCustomerForm,
    DeleteCustomerForm,
    CreateCustomerGroupForm,
    UpdateCustomerGroupForm,
    DeleteCustomerGroupForm,
    CreateCountryForm,
    UpdateCountryForm,
    DeleteCountryForm,
    CreateAddressForm,
    UpdateAddressForm,
    DeleteAddressForm,
    CreateRegionForm,
    UpdateRegionForm,
    DeleteRegionForm,
)


class CreateCustomer(DjangoModelFormMutation):
    class Meta:
        form_class = CreateCustomerForm


class UpdateCustomer(DjangoModelFormMutation):
    class Meta:
        form_class = UpdateCustomerForm


class DeleteCustomer(DjangoModelFormMutation):
    class Meta:
        form_class = DeleteCustomerForm


class CreateCustomerGroup(DjangoModelFormMutation):
    class Meta:
        form_class = CreateCustomerGroupForm


class UpdateCustomerGroup(DjangoModelFormMutation):
    class Meta:
        form_class = UpdateCustomerGroupForm


class DeleteCustomerGroup(DjangoModelFormMutation):
    class Meta:
        form_class = DeleteCustomerGroupForm


class CreateCountry(DjangoModelFormMutation):
    class Meta:
        form_class = CreateCountryForm


class UpdateCountry(DjangoModelFormMutation):
    class Meta:
        form_class = UpdateCountryForm


class DeleteCountry(DjangoModelFormMutation):
    class Meta:
        form_class = DeleteCountryForm


class CreateAddress(DjangoModelFormMutation):
    class Meta:
        form_class = CreateAddressForm


class UpdateAddress(DjangoModelFormMutation):
    class Meta:
        form_class = UpdateAddressForm


class DeleteAddress(DjangoModelFormMutation):
    class Meta:
        form_class = DeleteAddressForm


class CreateRegion(DjangoModelFormMutation):
    class Meta:
        form_class = CreateRegionForm


class UpdateRegion(DjangoModelFormMutation):
    class Meta:
        form_class = UpdateRegionForm


class DeleteRegion(DjangoModelFormMutation):
    class Meta:
        form_class = DeleteRegionForm


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
    delete_customer = DeleteCustomer.Field()
    create_customerGroup = CreateCustomerGroup.Field()
    update_customerGroup = UpdateCustomerGroup.Field()
    delete_customerGroup = DeleteCustomerGroup.Field()
    create_country = CreateCountry.Field()
    update_country = UpdateCountry.Field()
    delete_country = DeleteCountry.Field()
    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()
    delete_address = DeleteAddress.Field()
    create_region = CreateRegion.Field()
    update_region = UpdateRegion.Field()
    delete_region = DeleteRegion.Field()
