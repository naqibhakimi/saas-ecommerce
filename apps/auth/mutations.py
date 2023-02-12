import graphene
from apps.core.mutations import DynamicInputMixin, RelayMutationMixin
from .mixins import SignupMixin
class Signup(DynamicInputMixin, RelayMutationMixin, SignupMixin, graphene.ClientIDMutation):
    _required_inputs = {
        'email': graphene.String,
        'password1': graphene.String,
        'password2': graphene.String,
        'first_name': graphene.String,
        'last_name': graphene.String,

    }
class Mutation:
    signup = Signup.Field()
