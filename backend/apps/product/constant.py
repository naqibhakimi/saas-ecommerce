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
    PRODUCT_TYPE_CREATED = [
        {"message": _("Product type created"), "code": "product_type_created"}
    ]
    PRODUCT_TYPE_UPDATED = [
        {"message": _("Product type updated"), "code": "product_type_updated"}
    ]
    PRODUCT_TYPE_DELETED = [
        {"message": _("Product type deleted"), "code": "product_type_deleted"}
    ]
    PRODUCT_TYPE_NOT_EXIST = [
        {"message": _("Product type not exist"), "code": "product_type_not_exist"}
    ]
    PRODUCT_TAG_CREATED = [
        {"message": _("Product tag created"), "code": "product_tag_created"}
    ]
    PRODUCT_TAG_UPDATED = [
        {"message": _("Product tag updated"), "code": "product_tag_updated"}
    ]
    PRODUCT_TAG_DELETED = [
        {"message": _("Product tag deleted"), "code": "product_tag_deleted"}
    ]
    PRODUCT_TAG_NOT_FOUND = [
        {"message": _("Product tag not found"), "code": "product_tag_not_found"}
    ]
