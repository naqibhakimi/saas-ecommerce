import graphene
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.forms import ValidationError
from graphql_jwt.shortcuts import get_token

from apps.core.mutations import Output

from .constants import EMAIL_MESSAGES, Messages
from .exceptions import EmailAlreadyInUse, InvalidCredentials
from .forms import SignupForm, SingInForm

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
                user = form.save()
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
