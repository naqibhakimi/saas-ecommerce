import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateAddressMixin, CreateCurrencyMixin, UpdateCurrencyMixin
from .inputs import CreateCurrencyInputField, UpdateCurrencyInputField


class UpdateAddress(
    UpdateAddressMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation
):
    pass


class CreateCurrency(DynamicInputMixin, RelayMutationMixin, CreateCurrencyMixin, graphene.ClientIDMutation):
    __doc__ = CreateCurrencyMixin.__doc__
    _inputs = {'currency': CreateCurrencyInputField}


class Mutation:
    update_address = UpdateAddress.Field()
    create_currency = CreateCurrency.Field()
