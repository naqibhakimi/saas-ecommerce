import graphene
from django.contrib.auth import authenticate, login

from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .mixins import SignInMixin, SignupMixin


class Signup(DynamicInputMixin, RelayMutationMixin, SignupMixin, graphene.ClientIDMutation):
    _required_inputs = {
        'email': graphene.String,
        'password1': graphene.String,
        'password2': graphene.String,
    }


class SignIn(DynamicInputMixin, RelayMutationMixin, SignInMixin, graphene.ClientIDMutation):
    _required_inputs = {
        'email': graphene.String,
        'password': graphene.String,
    }

class Mutation:
    signup = Signup.Field()
    signin = SignIn.Field()
