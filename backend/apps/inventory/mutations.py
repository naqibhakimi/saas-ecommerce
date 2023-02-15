import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateAddressMixin

class UpdateAddress(UpdateAddressMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation):
    pass



class Mutation:
    update_address = UpdateAddress.Field()