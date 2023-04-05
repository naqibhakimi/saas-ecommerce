import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import CreateTaxRateMixin, DeleteTaxRateMixin, UpdateAddressMixin, UpdateTaxRateMixin
from .inputs import CrateTaxRateInputField, UpdateTaxRateInputField


class CreateTaxRate(DynamicInputMixin, RelayMutationMixin, CreateTaxRateMixin, graphene.ClientIDMutation):
    __doc__ = CreateTaxRateMixin.__doc__
    _inputs = {"tax_rate": CrateTaxRateInputField}


class UpdateTaxRate(DynamicInputMixin, RelayMutationMixin, UpdateTaxRateMixin, graphene.ClientIDMutation):
    __doc__ = UpdateTaxRateMixin.__doc__
    _inputs = {"tax_rate": UpdateTaxRateInputField}


class DeleteTaxRate(DynamicInputMixin, RelayMutationMixin, DeleteTaxRateMixin, graphene.ClientIDMutation):
    __doc__ = DeleteTaxRateMixin.__doc__
    _inputs = {"id": graphene.ID}


class Mutation:
    create_tax_rate = CreateTaxRate.Field()
    update_tax_rate = UpdateTaxRate.Field()
    delete_tax_rate = DeleteTaxRate.Field()
