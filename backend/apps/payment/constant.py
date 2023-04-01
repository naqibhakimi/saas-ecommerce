from django.utils.translation import gettext as _


class Message:
    CURRENCY_CREATED = [
        {"message": _("Currency created"), "code": "currency_created"}
    ]
    CURRENCY_UPDATED = [
        {"message": _("Currency updated"), "code": "currency_updated"}
    ]
    CURRENCY_DELETED = [
        {"message": _("Currency deleted"), "code": "currency_deleted"}
    ]
    CURRENCY_DOES_NOT_EXIST = [
        {"message": _("Currency does not exist"), "code": "currency_does_not_exist"}
    ]
