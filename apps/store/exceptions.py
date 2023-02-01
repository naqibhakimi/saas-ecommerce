from core.exceptions import GraphQLError
from django.utils.translation import gettext as _

class RecordDoesNotExists(GraphQLError):
    default_message = _("Your request record does not exists.")

