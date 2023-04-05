from django.forms import ValidationError
from apps.core.mutations import Output
from django.core.exceptions import ObjectDoesNotExist

from .forms import CreateTaxRateForm, UpdateTaxRateForm
from .constant import Message
from .models import TaxRate


class AddressRepository(object):
    def update(self):
        pass


class UpdateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        AddressRepository().update(root, info, **kwargs)
        return cls(success=True, errors="")


class CreateTaxRateMixin(Output):
    form = CreateTaxRateForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        tax_rate = kwargs.get('tax_rate')
        try:
            form = cls.form(data=tax_rate)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.TAX_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class UpdateTaxRateMixin(Output):
    form = UpdateTaxRateForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        tax_rate = kwargs.get('tax_rate')
        try:
            form = cls.form(
                data=tax_rate, instance=TaxRate.objects.get(id=tax_rate.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save(update_fields=tax_rate.keys())
                return cls(success=True, errors=Message.TAX_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValidationError, ValueError)as e:
            return cls(success=False, errors=e)


class DeleteTaxRateMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            TaxRate.objects.get(id=kwargs.get('id')).delete()
            return cls(success=True, errors=Message.TAX_RATE_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.TAX_DOES_NOT_EXIST)
