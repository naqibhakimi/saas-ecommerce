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
from .forms import UpdateCountryForm, UpdateCustomerForm, UpdateCustomerGroupForm
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


# def heavy_calc(arg):
#     for i in range(arg):
#         print(i)


class CreateCustomerGroupMixin(Output):
    form = CreateCustomerGroupForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        # bg_tasks = BackgroundTask(heavy_calc, 400000)
        # bg_tasks()
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
                instance.save(update_fields=customer_group_data.keys())

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
    # [FIXME:]
    form = UpdateCountryForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        country_data = kwargs.get("country")
        try:
            form = cls.form(data=country_data, instance=Country.objects.get(
                id=country_data.pop("id")))
            if form.is_valid:
                print("is_valid")
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
            Country.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.COUNTRY_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.COUNTRY_NOT_FOUND)


class CreateAddressMixin(Output):
    form = CreateAddressForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        print(kwargs)
        try:
            form = cls.form(data=kwargs.get("Address"))
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.ADDRESS_CREATED)
        except ValidationError:
            return cls(success=False, errors=Message.INVALID_INPUT)


class DeleteAddressMixin(Output):
    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Address.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.Address_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.Address_NOT_FOUND)


class DeleteRegionMixin(Output):
    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            id = kwargs.pop("id", None)
            Region.objects.filter(id=id).delete()
            return cls(success=True, errors=Message.Region_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.Region_NOT_FOUND)


class UpdateAddressMixin(Output):
    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop("id", None)
        Address.objects.filter(id=id).update(**kwargs)
        return cls(success=True, errors="")


class CreateRegionMixin(Output):
    form = CreateRegionForm

    @ classmethod
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
    @ classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.pop("id", None)
        Region.objects.filter(id=id).update(**kwargs)
        return cls(success=True, errors="")
