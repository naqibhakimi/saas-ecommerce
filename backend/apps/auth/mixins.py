import graphene
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.forms import ValidationError
from django.core.signing import BadSignature, SignatureExpired
from django.core.exceptions import ObjectDoesNotExist
from smtplib import SMTPException


from apps.core.mutations import Output

from .constants import EMAIL_MESSAGES, Messages
from .exceptions import EmailAlreadyInUse, InvalidCredentials, UserAlreadyVerified, TokenScopeError
from .forms import SignupForm, SingInForm, UpdateAccountForm, EmailForm
from .models import SEUser, UserStatus
from .types import UserNode
from django.conf import settings
from .signals import user_registered
from .shortcuts import get_user_by_email

from graphql_jwt.shortcuts import  get_token, get_user_by_token
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
                user.status.send(
                    context=info.context,
                    recipient_list=[user.email],
                    **EMAIL_MESSAGES.SIGN_UP)

                return cls(success=True)

        except ValidationError:
            return cls(success=False, errors=Messages.PASSWORD_DOESNOT_MATCH)
        except EmailAlreadyInUse:
            return cls(success=False, errors=Messages.EMAIL_IN_USE)


class SignInMixin(Output):
    form = SingInForm
    token = graphene.String()

    @classmethod
    def resolve_mutation(cls, root, info, *args, **kwargs):
        form = cls.form(data=kwargs)
        user = None

        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

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

    @classmethod
    def Field(cls, *args, **kwargs):
        cls._meta.fields["token"] = graphene.Field(graphene.String)
        cls._meta.fields["user"] = graphene.Field(UserNode)
        return super().Field(*args, **kwargs)

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):        
        try:
            token = kwargs.get("token")
            user = UserStatus.verify(token)
            return cls(success=True, user=user, token=token)
        except UserAlreadyVerified:
            return cls(success=False, errors=Messages.ALREADY_VERIFIED)
        except SignatureExpired:
            return cls(success=False, errors=Messages.EXPIRED_TOKEN)
        except (BadSignature, TokenScopeError):
            return cls(success=False, errors=Messages.INVALID_TOKEN)


class ResendActivationEmailMixin(Output):

    @classmethod
    def resolve_mutation(cls, root, info, **kwargs):
        try:
            email = kwargs.get("email")
            f = EmailForm({"email": email})
            if f.is_valid():
                user = get_user_by_email(email)
                user.status.resend_activation_email(info)
                return cls(success=True)
            return cls(success=False, errors=f.errors.get_json_data())
        except ObjectDoesNotExist:
            return cls(success=True)  # even if user is not registred
        except SMTPException:
            return cls(success=False, errors=Messages.EMAIL_FAIL)
        except UserAlreadyVerified:
            return cls(success=False, errors={"email": Messages.ALREADY_VERIFIED})

# class VerifySecondaryEmailMixin(Output):

#     @classmethod
#     def resolve_mutation(cls, root, info, **kwargs):
#         try:
#             token = kwargs.get("token")
#             UserStatus.verify_secondary_email(token)
#             return cls(success=True)
#         except EmailAlreadyInUse:
#             # while the token was sent and the user haven't
#             # verified, the email was free. If other account
#             # was created with it, it is already in use.
#             return cls(success=False, errors=Messages.EMAIL_IN_USE)
#         except SignatureExpired:
#             return cls(success=False, errors=Messages.EXPIRED_TOKEN)
#         except (BadSignature, TokenScopeError):
#             return cls(success=False, errors=Messages.INVALID_TOKEN)
