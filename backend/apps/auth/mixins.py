import logging
import traceback
from smtplib import SMTPException

import graphene
from graphql_relay import from_global_id
from apps.core.mutations import Output
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.core.signing import BadSignature, SignatureExpired
from django.forms import ValidationError
from graphql_jwt.shortcuts import get_token, get_user_by_token

from .constants import EMAIL_MESSAGES, Messages, TokenAction
from .exceptions import (EmailAlreadyInUse, InvalidCredentials,
                         TokenScopeError, UserAlreadyVerified, UserNotVerified)
from .forms import EmailForm, SignupForm, SingInForm, UpdateAccountForm
from .models import SEUser, UserStatus
from .shortcuts import get_user_by_email
from .signals import user_registered
from .types import UserNode
from .utils import get_token_payload

logger = logging.getLogger(__name__)

UserModel = get_user_model()


class SignupMixin(Output):
    form = SignupForm

    @classmethod
    def resolve_mutation(cls, root, info, *args, **kwargs):

        try:
            form = cls.form(data=kwargs)

            if form.errors:
                return cls(success=False, errors=form.errors)

            if form.is_valid():
                email = kwargs.get(UserModel.EMAIL_FIELD, False)
                user = form.save()
                if send_activation := (
                    settings.AUTH.SEND_ACTIVATION_EMAIL is True and email
                ):
                    user.status.send_activation_email(info)

                user_registered.send(sender=cls, user=user)
                user.status.send_activation_email(info)

                return cls(success=True)

        except ValidationError:
            return cls(success=False, errors=Messages.PASSWORD_DOESNOT_MATCH)
        except EmailAlreadyInUse:
            return cls(success=False, errors=Messages.EMAIL_IN_USE)
        except Exception as e:
            traceback.print_exc()


class SignInMixin(Output):
    form = SingInForm
    token = graphene.String()

    @classmethod
    def resolve_mutation(cls, root, info, *args, **kwargs):
        form = cls.form(data=kwargs)
        user = None

        try:
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]

                if not UserModel.objects.filter(email=email).exists():
                    raise InvalidCredentials()

                user = UserModel.objects.get(email=email)

                if not check_password(password, user.password):
                    raise InvalidCredentials()

                return cls(success=True, token=get_token(user))

        except InvalidCredentials:
            return cls(success=False, errors=Messages.INVALID_CREDENTIALS)


class UpdateAccountMixin(Output):
    form = UpdateAccountForm

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        print(info.context.headers)
        user = info.context.user
        fields = cls.form.Meta.fields
        for field in fields:
            if field not in kwargs:
                kwargs[field] = getattr(user, field)
        f = cls.form(kwargs, instance=user)

        if not f.is_valid():
            return cls(success=False, errors=f.errors.get_json_data())
        f.save()
        return cls(success=True)


class VerifyAccountMixin(Output):
    token = graphene.String()
    user = graphene.Field(UserNode)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            token = kwargs.get("token")
            user = UserStatus.verify(token)
            return cls(success=True, user=user, token=get_token(user))
        except UserAlreadyVerified:
            return cls(success=False, errors=Messages.ALREADY_VERIFIED)
        except SignatureExpired:
            return cls(success=False, errors=Messages.EXPIRED_TOKEN)
        except (BadSignature, TokenScopeError):
            return cls(success=False, errors=Messages.INVALID_TOKEN)
        except Exception as e:
            traceback.print_exc()


class ResendActivationEmailMixin(Output):
    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        logger.info("Sending ResendActivationEmail")
        try:
            email = kwargs.get("email")
            f = EmailForm({"email": email})
            if f.is_valid():
                user = get_user_by_email(email)
                user.status.resend_activation_email(info)
                return cls(success=True)
            return cls(success=False, errors=f.errors.get_json_data())
        except ObjectDoesNotExist:
            logger.warn(f"{email} ObjectDoesNotExist")
            return cls(success=True)  # even if user is not registred
        except SMTPException:
            return cls(success=False, errors=Messages.EMAIL_FAIL)
        except UserAlreadyVerified:
            return cls(success=False, errors=Messages.ALREADY_VERIFIED)


class VerifySecondaryEmailMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            token = kwargs.get("token")
            UserStatus.verify_secondary_email(token)
            return cls(success=True)
        except EmailAlreadyInUse:
            # while the token was sent and the user haven't
            # verified, the email was free. If other account
            # was created with it, it is already in use.
            return cls(success=False, errors=Messages.EMAIL_IN_USE)
        except SignatureExpired:
            return cls(success=False, errors=Messages.EXPIRED_TOKEN)
        except (BadSignature, TokenScopeError):
            return cls(success=False, errors=Messages.INVALID_TOKEN)


class SendPasswordResetEmailMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            email = kwargs.get("email")
            f = EmailForm({"email": email})
            if f.is_valid():
                user = get_user_by_email(email)
                user.status.send_password_reset_email(info, [email])
                return cls(success=True)
            return cls(success=False, errors=f.errors.get_json_data())
        except ObjectDoesNotExist:
            return cls(success=True)  # even if user is not registred
        except SMTPException:
            return cls(success=False, errors=Messages.EMAIL_FAIL)
        except UserNotVerified:
            user = get_user_by_email(email)
            try:
                user.status.resend_activation_email(info)
                return cls(
                    success=False,
                    errors={"email": Messages.NOT_VERIFIED_PASSWORD_RESET},
                )
            except SMTPException:
                return cls(success=False, errors=Messages.EMAIL_FAIL)

class SendSecondaryEmailVerificationMixin(Output):
    user = graphene.Field(UserNode)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        user = info.context.user
        user.secondary_email = kwargs.get('email')
        user.save()

        # Send the activation email to the user's secondary email address
        user.status.send_secondary_email_activation(info, kwargs.get('email'))
        return cls(success=True, user=user)



# class PasswordResetMixin(Output):
#     """
#     Change user password without old password.

#     Receive the token that was sent by email.

#     If token and new passwords are valid, update
#     user password and in case of using refresh
#     tokens, revoke all of them.

#     Also, if user has not been verified yet, verify it.
#     """

#     form = SetPasswordForm

#     @classmethod
#     def resolve_mutation(cls, root, info, **kwargs):
#         try:
#             token = kwargs.pop("token")
#             payload = get_token_payload(
#                 token,
#                 TokenAction.PASSWORD_RESET,
#                 AUTH.EXPIRATION_PASSWORD_RESET_TOKEN,
#             )
#             user = UserModel._default_manager.get(**payload)
#             f = cls.form(user, kwargs)
#             if f.is_valid():
#                 revoke_user_refresh_token(user)
#                 user = f.save()

#                 if user.status.verified is False:
#                     user.status.verified = True
#                     user.status.save(update_fields=["verified"])
#                     user_verified.send(sender=cls, user=user)

#                 return cls(success=True)
#             return cls(success=False, errors=f.errors.get_json_data())
#         except SignatureExpired:
#             return cls(success=False, errors=Messages.EXPIRED_TOKEN)
#         except (BadSignature, TokenScopeError):
#             return cls(success=False, errors=Messages.INVALID_TOKEN)


# class PasswordSetMixin(Output):
#     """
#     Set user password - for passwordless registration

#     Receive the token that was sent by email.

#     If token and new passwords are valid, set
#     user password and in case of using refresh
#     tokens, revoke all of them.

#     Also, if user has not been verified yet, verify it.
#     """

#     form = SetPasswordForm

#     @classmethod
#     def resolve_mutation(cls, root, info, **kwargs):
#         try:
#             token = kwargs.pop("token")
#             payload = get_token_payload(
#                 token,
#                 TokenAction.PASSWORD_SET,
#                 app_settings.EXPIRATION_PASSWORD_SET_TOKEN,
#             )
#             user = UserModel._default_manager.get(**payload)
#             f = cls.form(user, kwargs)
#             if f.is_valid():
#                 # Check if user has already set a password
#                 if user.has_usable_password():
#                     raise PasswordAlreadySetError
#                 revoke_user_refresh_token(user)
#                 user = f.save()

#                 if user.status.verified is False:
#                     user.status.verified = True
#                     user.status.save(update_fields=["verified"])

#                 return cls(success=True)
#             return cls(success=False, errors=f.errors.get_json_data())
#         except SignatureExpired:
#             return cls(success=False, errors=Messages.EXPIRED_TOKEN)
#         except (BadSignature, TokenScopeError):
#             return cls(success=False, errors=Messages.INVALID_TOKEN)
#         except (PasswordAlreadySetError):
#             return cls(success=False, errors=Messages.PASSWORD_ALREADY_SET)
