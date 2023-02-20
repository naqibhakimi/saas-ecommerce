import graphene
from django.utils.translation import gettext_lazy as _


class GraphQLError(Exception):
    default_message = None

    def __init__(self, message=None):
        if message is None:
            message = self.default_message

        super().__init__(message)


class WrongUsage(GraphQLError):
    """
    internal exception
    """

    default_message = _("Wrong usage, check your code!.")
