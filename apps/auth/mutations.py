from django.contrib.auth import authenticate, login
import graphene
from apps.core.mutations import DynamicInputMixin, RelayMutationMixin
from .mixins import SignupMixin


class Signup(DynamicInputMixin, RelayMutationMixin, SignupMixin, graphene.ClientIDMutation):
    _required_inputs = {
        'email': graphene.String,
        'password1': graphene.String,
        'password2': graphene.String,
        'first_name': graphene.String,
        'last_name': graphene.String,

    }


class LoginMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    token = graphene.String()

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            raise Exception("Invalid Login")

        login(info.context, user)
        token = user.auth_token.key
        return LoginMutation(success=True, token=token)


class Mutation:
    signup = Signup.Field()
