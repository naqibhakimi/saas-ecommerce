from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from apps.core.mutations import Output
from apps.customer.forms import (
    CreateCustomerForm,
    CreateCountryForm,
    CreateCustomerGroupForm,
    CreateCountryForm,
    CreateAddressForm,
    CreateRegionForm,
)
from apps.core.background_tasks import BackgroundTask
from .forms import UpdateAddressForm, UpdateCountryForm, UpdateCustomerForm, UpdateCustomerGroupForm, UpdateRegionForm
from .constant import Message
from .models import (
    Customer,
    CustomerGroup,
    Country,
    Address,
    Region,
)


class CreateCustomerMixin(Output):
    form = CreateCustomerForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get('customer'))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.CUSTOMER_CREATED)
        except ValidationError:
            return cls(success=False, errors=Message.INVALID_INPUT)


class UpdateCustomerMixin(Output):
    form = UpdateCustomerForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        customer_data = kwargs.get('customer')

        try:
            form = cls.form(data=customer_data,
                            instance=Customer.objects.get(id=customer_data.pop('id')))

            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=customer_data.keys())

                return cls(success=True, errors=form.errors)

            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as err:
            return cls(success=False, errors=err)


class DeleteCustomerMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Customer.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.CUSTOMER_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.CUSTOMER_NOT_FOUND)


class CreateCustomerGroupMixin(Output):
    form = CreateCustomerGroupForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:

            form = cls.form(data=kwargs.get("customer_group", {}))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.CUSTOMER_GROUP_CREATED)
        except ValidationError:
            return cls(success=False, errors=Message.INVALID_INPUT)


class UpdateCustomerGroupMixin(Output):
    form = UpdateCustomerGroupForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        customer_group_data = kwargs.get("customer_group")

        try:
            form = cls.form(data=customer_group_data,
                            instance=CustomerGroup.objects.get(id=customer_group_data.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                # because it's many to many(m2m) field so we don't need to update
                # first I I'll pop customers then update the form then I'll add customers to the form
                customers = customer_group_data.pop('customers')
                instance.save(update_fields=customer_group_data.keys())
                instance.customers.set(customers, clear=True)

                return cls(success=True, errors=form.errors)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeleteCustomerGroupMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            CustomerGroup.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.CustomerGroup_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.CUSTOMER_GROUP_NOT_FOUND)


class CreateCountryMixin(Output):
    form = CreateCountryForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get("country", {}))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid:
                form.save()
                return cls(success=True, errors=Message.COUNTRY_CREATED)
        except ValidationError:
            return cls(success=False, errors=Message.INVALID_INPUT)


class UpdateCountryMixin(Output):
    form = UpdateCountryForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        country_data = kwargs.get("country")
        try:
            form = cls.form(data=country_data, instance=Country.objects.get(
                id=country_data.pop("id")))
            if form.is_valid:
                instance = form.save(commit=False)
                instance.save(update_fields=country_data.keys())
                return cls(success=True, errors=form.errors)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeleteCountryMixin(Output):
    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Country.objects.get(id=id).delete()
            return cls(success=True, errors=Message.COUNTRY_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.COUNTRY_NOT_FOUND)


class CreateAddressMixin(Output):
    form = CreateAddressForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get("Address"))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid:
                form.save()
                return cls(success=True, errors=Message.ADDRESS_CREATED)
        except ValidationError:
            return cls(sum=False, errors=Message.INVALID_INPUT)


class UpdateAddressMixin(Output):
    form = UpdateAddressForm

    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        address_data = kwargs.get("Address")

        try:
            form = cls.form(data=address_data, instance=Address.objects.get(
                id=address_data.pop("id")))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=address_data.keys())
                return cls(success=True, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=False, errors=e)


class DeleteAddressMixin(Output):
    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Address.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.ADDRESS_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.ADDRESS_NOT_FOUND)


class CreateRegionMixin(Output):
    # [FIXME: query the region and call currency]
    form = CreateRegionForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get("Region"))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid:
                form.save()
                return cls(success=True, errors=Message.REGION_CREATED)
        except ValidationError:
            return cls(success=False, errors=Message.INVALID_INPUT)


class UpdateRegionMixin(Output):
    form = UpdateRegionForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        region_data = kwargs.get("Region")
        try:
            form = cls.form(data=region_data, instance=Region.objects.get(
                id=region_data.pop("id")))
            if form.is_valid:
                instance = form.save(commit=False)
                instance.save(update_fields=region_data.keys())
                return cls(success=True, errors=form.errors)
        except (ValidationError, ValueError) as e:
            return cls(success=True, errors=e)


class DeleteRegionMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Region.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.REGION_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.REGION_NOT_FOUND)
