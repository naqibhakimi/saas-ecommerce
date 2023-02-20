import graphene
from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .mixins import UpdateAddressMixin


class UpdateAddress(
    UpdateAddressMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation
):
    pass


class Mutation:
    update_address = UpdateAddress.Field()
