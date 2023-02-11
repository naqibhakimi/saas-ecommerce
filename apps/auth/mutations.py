import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateAddressMixin

class UpdateAddress(UpdateAddressMixin, RelayMutationMixin, DynamicInputMixin, graphene.ClientIDMutation):
    pass



class Mutation:
    update_address = UpdateAddress.Field()



from .models import SEUser
import graphene
import graphql_jwt

from graphene_file_upload.scalars import Upload

from apps.core.mutations import DynamicInputMixin, RelayMutationMixin
from .mixins import (ArchiveAccountMixin, DeleteAccountMixin, InviteMixin,
                     ObtainJSONWebTokenMixin, PasswordChangeMixin,
                     PasswordResetMixin, PasswordSetMixin, RegisterMixin,
                     RemoveSecondaryEmailMixin, ResendActivationEmailMixin,
                     SendPasswordResetEmailMixin,
                     SendSecondaryEmailActivationMixin, SlackAuthCodeMixin, SwapEmailsMixin,
                     UpdateAccountMixin, UpdateCompanyMixin, VerifyAccountMixin, VerifyCnameMixin,
                     VerifyOrRefreshOrRevokeTokenMixin,
                     VerifySecondaryEmailMixin)
from .settings import graphql_auth_settings as app_settings
from .types import UserNode
from .utils import normalize_fields


class Register(
    RelayMutationMixin, DynamicInputMixin, RegisterMixin, graphene.ClientIDMutation
):

    __doc__ = RegisterMixin.__doc__

    password_fields = (
        []
        if app_settings.ALLOW_PASSWORDLESS_REGISTRATION
        else ["company", "password1", "password2", 'bot_token']
    )

    _required_inputs = normalize_fields(
        app_settings.REGISTER_MUTATION_FIELDS, password_fields
    )
    _inputs = app_settings.REGISTER_MUTATION_FIELDS_OPTIONAL



class Invite(
    RelayMutationMixin, DynamicInputMixin, InviteMixin, graphene.ClientIDMutation
):

    __doc__ = InviteMixin.__doc__
    

    _required_inputs = app_settings.REGISTER_MUTATION_FIELDS
    _inputs = app_settings.REGISTER_MUTATION_FIELDS_OPTIONAL


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


class SendSecondaryEmailActivation(
    RelayMutationMixin,
    DynamicInputMixin,
    SendSecondaryEmailActivationMixin,
    graphene.ClientIDMutation,
):
    __doc__ = SendSecondaryEmailActivationMixin.__doc__
    _required_inputs = ["email", "password"]


class VerifySecondaryEmail(
    RelayMutationMixin,
    DynamicInputMixin,
    VerifySecondaryEmailMixin,
    graphene.ClientIDMutation,
):
    __doc__ = VerifySecondaryEmailMixin.__doc__
    _required_inputs = ["token"]


class SwapEmails(
    RelayMutationMixin, DynamicInputMixin, SwapEmailsMixin, graphene.ClientIDMutation
):
    __doc__ = SwapEmailsMixin.__doc__
    _required_inputs = ["password"]


class RemoveSecondaryEmail(
    RelayMutationMixin,
    DynamicInputMixin,
    RemoveSecondaryEmailMixin,
    graphene.ClientIDMutation,
):
    __doc__ = RemoveSecondaryEmailMixin.__doc__
    _required_inputs = ["password"]


class PasswordSet(
    RelayMutationMixin, DynamicInputMixin, PasswordSetMixin, graphene.ClientIDMutation
):
    __doc__ = PasswordSetMixin.__doc__
    _required_inputs = ["token", "new_password1", "new_password2"]


class PasswordReset(
    RelayMutationMixin, DynamicInputMixin, PasswordResetMixin, graphene.ClientIDMutation
):
    __doc__ = PasswordResetMixin.__doc__
    _required_inputs = ["token", "new_password1", "new_password2"]


class ObtainJSONWebToken(
    RelayMutationMixin, ObtainJSONWebTokenMixin, graphql_jwt.relay.JSONWebTokenMutation
):
    __doc__ = ObtainJSONWebTokenMixin.__doc__
    user = graphene.Field(UserNode)
    unarchiving = graphene.Boolean(default_value=False)

    @classmethod
    def Field(cls, *args, **kwargs):
        cls._meta.arguments["input"]._meta.fields.update(
            {"password": graphene.InputField(graphene.String, required=True)}
        )
        for field in app_settings.LOGIN_ALLOWED_FIELDS:
            cls._meta.arguments["input"]._meta.fields.update(
                {field: graphene.InputField(graphene.String)}
            )
        return super(graphql_jwt.relay.JSONWebTokenMutation, cls).Field(*args, **kwargs)


class ArchiveAccount(
    RelayMutationMixin,
    ArchiveAccountMixin,
    DynamicInputMixin,
    graphene.ClientIDMutation,
):
    __doc__ = ArchiveAccountMixin.__doc__
    _required_inputs = ["password"]


class DeleteAccount(
    RelayMutationMixin, DeleteAccountMixin, DynamicInputMixin, graphene.ClientIDMutation
):
    __doc__ = DeleteAccountMixin.__doc__
    _required_inputs = ["password"]


class PasswordChange(
    RelayMutationMixin,
    PasswordChangeMixin,
    DynamicInputMixin,
    graphene.ClientIDMutation,
):
    __doc__ = PasswordChangeMixin.__doc__
    _required_inputs = ["old_password", "new_password1", "new_password2"]


class UpdateAccount(
    RelayMutationMixin, DynamicInputMixin, UpdateAccountMixin, graphene.ClientIDMutation
):
    __doc__ = UpdateAccountMixin.__doc__
    _inputs = app_settings.UPDATE_MUTATION_FIELDS


class VerifyToken(
    RelayMutationMixin, VerifyOrRefreshOrRevokeTokenMixin, graphql_jwt.relay.Verify
):
    __doc__ = VerifyOrRefreshOrRevokeTokenMixin.__doc__

    class Input:
        token = graphene.String(required=True)


class RefreshToken(
    RelayMutationMixin, VerifyOrRefreshOrRevokeTokenMixin, graphql_jwt.relay.Refresh
):
    __doc__ = VerifyOrRefreshOrRevokeTokenMixin.__doc__

    class Input(graphql_jwt.mixins.RefreshMixin.Fields):
        """Refresh Input"""


class RevokeToken(
    RelayMutationMixin, VerifyOrRefreshOrRevokeTokenMixin, graphql_jwt.relay.Revoke
):
    __doc__ = VerifyOrRefreshOrRevokeTokenMixin.__doc__

    class Input:
        refresh_token = graphene.String(required=True)


class UpdateCompany(
    RelayMutationMixin, DynamicInputMixin, UpdateCompanyMixin, graphene.ClientIDMutation
):
    __doc__ = UpdateCompanyMixin.__doc__
    _required_inputs = {
        "domain": graphene.String,
        "header_text": graphene.String,
        "company_logo": Upload,
        "name": graphene.String,
        "company_header_color": graphene.String,
        "company_text_color": graphene.String,
        "brand_domain": graphene.String,

    }

class SlackAuthCode(
    RelayMutationMixin, DynamicInputMixin, SlackAuthCodeMixin, graphene.ClientIDMutation
):
    __doc__ = SlackAuthCodeMixin.__doc__
    _required_inputs = {
        "code": graphene.String,
    }


class VerfiyCname(
    RelayMutationMixin, DynamicInputMixin, VerifyCnameMixin, graphene.ClientIDMutation
):
    __doc__ = VerifyCnameMixin.__doc__
    _required_inputs = {
        "domain": graphene.String,
    }
