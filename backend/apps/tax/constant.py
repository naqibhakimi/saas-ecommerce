from django.utils.translation import gettext as _


class Message(object):
    TAX_CREATED = [
        {"message": _("Tax created successfully"), "code": "tax_created"}
    ]
    TAX_UPDATED = [
        {"message": _("Tax updated successfully"), "code": "tax_updated"}
    ]
    TAX_RATE_DELETED = [
        {"message": _("Tax deleted successfully"), "code": "tax_rate_deleted"}
    ]
    TAX_DOES_NOT_EXIST = [
        {"message": _("Tax does not exist"), "code": "tax_rate_does_not_exist"}
    ]
