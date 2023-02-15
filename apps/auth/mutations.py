import graphene
from django.contrib.auth import authenticate, login

from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .mixins import SignInMixin, SignupMixin, UpdateUserMixin


class Signup(DynamicInputMixin, RelayMutationMixin, SignupMixin, graphene.ClientIDMutation):
    _required_inputs = {
        'email': graphene.String,
        'password1': graphene.String,
        'password2': graphene.String,
        'first_name': graphene.String,
        'last_name': graphene.String,
    }


class SignIn(DynamicInputMixin, RelayMutationMixin, SignInMixin, graphene.ClientIDMutation):
    _required_inputs = {
        'email': graphene.String,
        'password': graphene.String,
    }


class UpdateUser(DynamicInputMixin, RelayMutationMixin, UpdateUserMixin, graphene.ClientIDMutation):
    _required_inputs = {
        "id": graphene.String,
        'email': graphene.String,
        'password1': graphene.String,
        'password2': graphene.String,
        'first_name': graphene.String,
        'last_name': graphene.String,
    }


class Mutation:
    signup = Signup.Field()
    signin = SignIn.Field()
    update_user = UpdateUser.Field()
