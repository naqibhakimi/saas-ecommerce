from django.utils.translation import gettext as _

from apps.core.exceptions import GraphQLError


class RecordDoesNotExists(GraphQLError):
    default_message = _("Your request record does not exists.")


class UserAlreadyVerified(GraphQLError):
    default_message = _("User already verified.")


class InvalidCredentials(GraphQLError):
    default_message = _("Invalid credentials.")


class UserNotVerified(GraphQLError):
    default_message = _("User is not verified.")


class EmailAlreadyInUse(GraphQLError):
    default_message = _("This email is already in use.")


class TokenScopeError(GraphQLError):
    default_message = _("This token if for something else.")


class PasswordAlreadySetError(GraphQLError):
    default_message = _("Password already set for account.")


class WrongUsage(GraphQLError):
    """
    internal exception
    """
    default_message = _("Wrong usage, check your code!.")
