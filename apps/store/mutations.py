import graphene
from core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateAddressMixin


class UpdateAddress(
        UpdateAddressMixin,
        RelayMutationMixin,
        DynamicInputMixin,
        graphene.ClientIDMutation):
    pass


class SalesChannel(
    RelayMutationMixin,
    DynamicInputMixin,
    UpdateAddressMixin,
    graphene.ClientIDMutation
):
    pass


class Mutation:
    update_address = UpdateAddress.Field()
