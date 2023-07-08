import graphene
from django.contrib.auth import authenticate, login
from graphql_relay import from_global_id

from apps.core.mutations import DynamicInputMixin, RelayMutationMixin

from .mixins import (
    PasswordResetMixin,
    ResendActivationEmailMixin,
    SendPasswordResetEmailMixin,
    SendSecondaryEmailVerificationMixin,
    SignInMixin,
    SignupMixin,
    SwapEmailsMixin,
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


class SendSecondaryEmailVerification(
    DynamicInputMixin, RelayMutationMixin, SendSecondaryEmailVerificationMixin, graphene.ClientIDMutation
):
    _inputs = {
        "email": graphene.String,
    }


class SwapEmails(DynamicInputMixin, RelayMutationMixin, SwapEmailsMixin, graphene.ClientIDMutation):
    __doc__ = SwapEmailsMixin.__doc__
    _inputs = ["password"]


class PasswordReset(
    DynamicInputMixin, RelayMutationMixin, PasswordResetMixin, graphene.ClientIDMutation
):
    __doc__ = PasswordResetMixin.__doc__
    # _required_args = ["token", "new_password1", "new_password2"]
    _inputs = ["token", "new_password1", "new_password2"]


class Mutation:
    signup = Signup.Field()
    signin = SignIn.Field()
    update_account = UpdateAccount.Field()
    verify_account = VerifyAccount.Field()
    resend_activation_email = ResendActivationEmail.Field()
    send_password_reset_email = SendPasswordResetEmail.Field()
    send_secondary_email_verification = SendSecondaryEmailVerification.Field()
    swap_emails = SwapEmails.Field()
    password_reset = PasswordReset.Field()
