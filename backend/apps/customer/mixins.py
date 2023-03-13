import traceback
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
from .forms import UpdateCustomerForm
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
            form = cls.form(data=kwargs)
            if form.errors:
                return cls(success=False, error=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, error=Message.CUSTOMER_CREATED)
        except ValidationError:
            return cls(success=False, error=Message.INVALID_INPUT)


class UpdateCustomerMixin(Output):
    form = UpdateCustomerForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs.get('customer'))

            if form.is_valid():
                form.save()
                return cls(success=True, errors=form.errors)
            return cls(success=False, errors=form.errors)
        except ValidationError as err:
            return cls(success=False, errors=form.errors)
        except ValueError as err:
            return cls(success=False, errors=form.errors)


class DeleteCustomerMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Customer.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.CUSTOMER_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.CUSTOMER_NOT_FOUND)


class DeleteCustomerGroupMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            CustomerGroup.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.CustomerGroup_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.CustomerGroup_NOT_FOUND)


class DeleteCountryMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Country.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.Country_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.Country_NOT_FOUND)


class DeleteAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Address.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.Address_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.Address_NOT_FOUND)


class DeleteRegionMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Region.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.Region_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.Region_NOT_FOUND)


class CreateCountryMixin(Output):
    # [FIXME: do we need form for update and delete?]
    form = CreateCountryForm

    @classmethod
    def resolve_mutation(cls, root, info, *args, **kwargs):
        try:
            form = cls.form(data=kwargs)
            if form.errors:
                return cls(success=False, error=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, error=Message.COUNTRY_CREATED)
        except ValidationError as err:
            return cls(success=False, error=Message.COUNTRY_CREATED)


class UpdateCountryMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop("id", None)
        Country.objects.filter(id=id).update(**kwargs)
        return cls(success=True, errors="")


class CreateCustomerGroupMixin(Output):
    form = CreateCustomerGroupForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs)
            if form.errors:
                return cls(success=False, error=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, error=Message.CUSTOMER_CREATED)
        except ValidationError as err:
            return cls(success=True, error=Message.CUSTOMER_CREATED)


class CreateAddressMixin(Output):
    form = CreateAddressForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs)
            if form.errors:
                return cls(success=False, error=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, error=Message.CUSTOMER_DELETED)
        except ValidationError as err:
            return cls(success=True, error=Message.CUSTOMER_DELETED)


class UpdateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop("id", None)
        Address.objects.filter(id=id).update(**kwargs)
        return cls(success=True, errors="")


class CreateRegionMixin(Output):
    form = CreateRegionForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            form = cls.form(data=kwargs)
            if form.errors:
                return cls(success=False, error=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, error=Message.COUNTRY_CREATED)
        except ValidationError as err:
            return cls(success=True, error=Message.COUNTRY_CREATED)


class UpdateRegionMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop("id", None)
        Region.objects.filter(id=id).update(**kwargs)
        return cls(success=True, errors="")
