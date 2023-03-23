from django.utils.translation import gettext as _


class Message:
    INVALID_INPUT = [
        {"message": _("Invalid input"), "code": "invalid_input"}
    ]
    PRODUCT_CREATED = [
        {"message": _("Product created"), "code": "product_created"}
    ]
    PRODUCT_UPDATED = [
        {"message": _("Product updated"), "code": "product_updated"}
    ]
    PRODUCT_DELETED = [
        {"message": _("Product deleted"), "code": "product_deleted"}
    ]
    PRODUCT_NOT_FOUND = [
        {"message": _("Product not found"), "code": "product_not_found"}
    ]
    PRICE_LIST_CREATED = [
        {"message": _("Price list created"), "code": "price_list_created"}
    ]
    PRICE_LIST_UPDATED = [
        {"message": _("Price list updated"), "code": "price_list_updated"}
    ]
    PRICE_LIST_DELETED = [
        {"message": _("Price list deleted"), "code": "price_list_deleted"}
    ]
    PRICE_LIST_NOT_FOUND = [
        {"message": _("Price list not found"), "code": "price_list_not_found"}
    ]
