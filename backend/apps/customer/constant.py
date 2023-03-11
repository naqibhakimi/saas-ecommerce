from django.utils.translation import gettext as _


class Message:
    INVALID_INPUT = [
        {"message": _("Invalid input"), "code": "invalid_input"}
    ]
    CUSTOMER_DELETED = [
        {"message": _("Customer deleted successfully"), "code": "customer_deleted"}
    ]
    CUSTOMER_NOT_FOUND = [
        {"message": _("Customer not found"), "code": "customer_not_found"}
    ]
    CUSTOMER_CREATED = [
        {"message": _("Customer created successfully"), "code": "customer_created"}
    ]
    COUNTRY_CREATED = [
        {"message": _("Country created successfully"), "code": "country_created"}
    ]
