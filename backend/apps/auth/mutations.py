import graphene
from django.contrib.auth import authenticate, login
from graphql.error import GraphQLError

from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .mixins import ResendActivationEmailMixin, SignInMixin, SignupMixin, UpdateAccountMixin, VerifyAccountMixin


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


class UpdateAccount(DynamicInputMixin, RelayMutationMixin, UpdateAccountMixin, graphene.ClientIDMutation):
    _inputs = {
        'email': graphene.String,
        'first_name': graphene.String,
        'last_name': graphene.String,
    }


class VerifyAccount(
    RelayMutationMixin, DynamicInputMixin, VerifyAccountMixin, graphene.ClientIDMutation
):
    __doc__ = VerifyAccountMixin.__doc__
    _required_inputs = ["token"]


class ResendActivationEmail(
    RelayMutationMixin,
    DynamicInputMixin,
    ResendActivationEmailMixin,
    graphene.ClientIDMutation,
):
    __doc__ = ResendActivationEmailMixin.__doc__
    _required_inputs = ["email"]


class Active( graphene.ClientIDMutation):
    @classmethod
    def mutate_and_get_payload(root, info, *args, **kwargs):
        raise GraphQLError('sadfasdfsadf')

class Mutation:
    signup = Signup.Field()
    signin = SignIn.Field()
    update_account = UpdateAccount.Field()
    verify_account = VerifyAccount.Field()
    active = Active.Field()
    resend_activation_email = ResendActivationEmail.Field()