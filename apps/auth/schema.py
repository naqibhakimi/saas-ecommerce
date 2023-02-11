import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt import ObtainJSONWebToken

from apps.auth.mutations import (ArchiveAccount, DeleteAccount, Invite,
                                 PasswordChange, PasswordReset, PasswordSet,
                                 RefreshToken, Register, RemoveSecondaryEmail,
                                 ResendActivationEmail, RevokeToken,
                                 SendPasswordResetEmail,
                                 SendSecondaryEmailActivation,
                                 SwapEmails, UpdateAccount,
                                 VerifyAccount, VerifySecondaryEmail,
                                 VerifyToken)
from apps.auth.types import LogAttemptsNode, UserEmailLogNode

from .models import SEUser
from .queries import MeQuery, UserQuery


class Mutation:
    register = Register.Field()
    invite = Invite.Field()
    verify_account = VerifyAccount.Field()
    resend_activation_email = ResendActivationEmail.Field()
    send_password_reset_email = SendPasswordResetEmail.Field()
    password_reset = PasswordReset.Field()
    password_set = PasswordSet.Field()  # For passwordless registration
    password_change = PasswordChange.Field()
    update_account = UpdateAccount.Field()
    archive_account = ArchiveAccount.Field()
    delete_account = DeleteAccount.Field()
    send_secondary_email_activation = SendSecondaryEmailActivation.Field()
    verify_secondary_email = VerifySecondaryEmail.Field()
    swap_emails = SwapEmails.Field()
    remove_secondary_email = RemoveSecondaryEmail.Field()

    # django-graphql-jwt inheritances
    # token_auth = VerifiedObtainJSONWebToken.Field()
    verify_token = VerifyToken.Field()
    refresh_token = RefreshToken.Field()
    revoke_token = RevokeToken.Field()

class Query(UserQuery, MeQuery):
    pass