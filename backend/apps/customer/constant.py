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
    CUSTOMER_GROUP_CREATED = [
        {"message": _("Customer Group created successfully"),
         "code": "created_customer_group"}
    ]
    CustomerGroup_DELETED = [
        {"message": _("Customer Group deleted successfully"),
         "code": "customer_group_deleted"}
    ]
    CUSTOMER_GROUP_NOT_FOUND = [
        {"message": _("Customer group not found"), "code": "customer_group_not_found"}
    ]
    COUNTRY_CREATED = [
        {"message": _("Country created successfully"), "code": "country_created"}
    ]
    COUNTRY_DELETED = [
        {"message": _("Country deleted successfully"), "code": "country_deleted"}
    ]
    COUNTRY_NOT_FOUND = [
        {"message": _("Country doesn't found"), "code": "country_not_found"}
    ]
    ADDRESS_CREATED = [
        {"message": _("Address created successfully"), "code": "address_created"}
    ]
    ADDRESS_DELETED = [
        {"message": _("Address deleted successfully"), "code": "address_deleted"}
    ]
    ADDRESS_NOT_FOUND = [
        {"message": _("Address not found"), "code": "address_not_found"}
    ]
    REGION_CREATED = [
        {"message": _("Region created successfully"), "code": "region_created"}
    ]
    REGION_DELETED = [
        {"message": _("Region deleted successfully"), "code": "region_delete"}
    ]
    REGION_NOT_FOUND = [
        {"message": _("Region not found"), "code": "region_not_found"}
    ]
