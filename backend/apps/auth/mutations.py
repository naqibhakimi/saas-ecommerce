from graphene import InputObjectType, Mutation, String
import graphene
from django.contrib.auth import authenticate, login
from graphql.error import GraphQLError
from graphql_relay import from_global_id

from apps.core.mutations import DynamicInputMixin, RelayMutationMixin
from .types import UserNode
from .models import SEUser

from .mixins import (
    ResendActivationEmailMixin,
    SendPasswordResetEmailMixin,
    SignInMixin,
    SignupMixin,
    UpdateAccountMixin,
    VerifyAccountMixin,
)


class Signup(
    DynamicInputMixin, RelayMutationMixin, SignupMixin, graphene.ClientIDMutation
):
    _required_inputs = {
        "email": graphene.String,
        "password1": graphene.String,
        "password2": graphene.String,
    }


class SignIn(
    DynamicInputMixin, RelayMutationMixin, SignInMixin, graphene.ClientIDMutation
):
    _required_inputs = {
        "email": graphene.String,
        "password": graphene.String,
    }


class UpdateAccount(
    DynamicInputMixin, RelayMutationMixin, UpdateAccountMixin, graphene.ClientIDMutation
):
    _inputs = {
        "email": graphene.String,
        "first_name": graphene.String,
        "last_name": graphene.String,
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


class SendPasswordResetEmail(
    RelayMutationMixin,
    DynamicInputMixin,
    SendPasswordResetEmailMixin,
    graphene.ClientIDMutation,
):
    __doc__ = SendPasswordResetEmailMixin.__doc__
    _required_inputs = ["email"]


# class SendSecondaryEmailActivation(
#     RelayMutationMixin,
#     DynamicInputMixin,
#     SendSecondaryEmailActivationMixin,
#     graphene.ClientIDMutation,
# ):
#     __doc__ = SendSecondaryEmailActivationMixin.__doc__
#     _required_inputs = ["email", "password"]


class ActivateSecondaryEmailInput(InputObjectType):
    user_id = String(required=True)
    email = String(required=True)


class ActivateSecondaryEmail(Mutation):
    class Arguments:
        input = ActivateSecondaryEmailInput(required=True)

    user = graphene.Field(UserNode)

    @classmethod
    def mutate(cls, root, info, input):
        user_id = from_global_id(input.user_id)[1]
        user = SEUser.objects.get(pk=user_id)

        user.secondary_email = input.email
        user.save()

        # Send the activation email to the user's secondary email address
        user.status.send_secondary_email_activation(info, input.email)

        return ActivateSecondaryEmail(user=user)


class Active(graphene.ClientIDMutation):
    @classmethod
    def mutate_and_get_payload(root, info, *args, **kwargs):
        raise GraphQLError("sadfasdfsadf")


class Mutation:
    signup = Signup.Field()
    signin = SignIn.Field()
    update_account = UpdateAccount.Field()
    verify_account = VerifyAccount.Field()
    active = Active.Field()
    resend_activation_email = ResendActivationEmail.Field()
    send_password_reset_email = SendPasswordResetEmail.Field()
    activate_secondary_email = ActivateSecondaryEmail.Field()
