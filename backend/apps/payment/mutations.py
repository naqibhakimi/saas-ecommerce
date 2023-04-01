import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateAddressMixin, CreateCurrencyMixin, UpdateCurrencyMixin, DeleteCurrencyMixin
from .inputs import CreateCurrencyInputField, UpdateCurrencyInputField


class UpdateAddress(
    UpdateAddressMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation
):
    pass


class CreateCurrency(DynamicInputMixin, RelayMutationMixin, CreateCurrencyMixin, graphene.ClientIDMutation):
    __doc__ = CreateCurrencyMixin.__doc__
    _inputs = {'currency': CreateCurrencyInputField}


class UpdateCurrency(DynamicInputMixin, RelayMutationMixin, UpdateCurrencyMixin, graphene.ClientIDMutation):
    __doc__ = UpdateCurrencyMixin.__doc__
    _inputs = {'currency': UpdateCurrencyInputField}


class DeleteCurrency(DynamicInputMixin, RelayMutationMixin, DeleteCurrencyMixin, graphene.ClientIDMutation):
    __doc__ = DeleteCurrencyMixin.__doc__
    _inputs = {"id": graphene.ID}


class Mutation:
    update_address = UpdateAddress.Field()
    create_currency = CreateCurrency.Field()
    update_currency = UpdateCurrency.Field()
    delete_currency = DeleteCurrency.Field()
