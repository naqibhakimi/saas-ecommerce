from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from apps.core.mutations import Output
from .forms import CreateCurrencyForm, UpdateCurrencyForm
from .constant import Message
from .models import Currency


class AddressRepository(object):
    def update(self):
        pass


class UpdateAddressMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        AddressRepository().update(root, info, **kwargs)
        return cls(success=True, errors="")


class CreateCurrencyMixin(Output):
    form = CreateCurrencyForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        currency_data = kwargs.get('currency')
        try:
            form = cls.form(data=currency_data)
            if form.errors:
                return cls(success=False, errors=form.errors)
            if form.is_valid():
                form.save()
                return cls(success=True, errors=Message.CURRENCY_CREATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class UpdateCurrencyMixin(Output):
    form = UpdateCurrencyForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        currency_data = kwargs.get('currency')
        try:
            form = cls.form(data=currency_data, instance=Currency.objects.get(
                id=currency_data.pop('id')))
            if form.is_valid():
                instance = form.save(commit=False)
                # FIXME: WHEY we do't make the commit = True after it becomes False
                instance.save(update_fields=currency_data.keys())
                return cls(success=True, errors=Message.CURRENCY_UPDATED)
            return cls(success=False, errors=form.errors)
        except (ValueError, ValidationError) as e:
            return cls(success=False, errors=e)


class DeleteCurrencyMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        id = kwargs.get('id')
        try:
            Currency.objects.get(id=id).delete()
            return cls(success=True, errors=Message.CURRENCY_DELETED)
        except ObjectDoesNotExist:
            return cls(success=False, errors=Message.CURRENCY_DOES_NOT_EXIST)
