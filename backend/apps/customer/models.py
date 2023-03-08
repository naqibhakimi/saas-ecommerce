from django.core.validators import EmailValidator
from django.db import models

from apps.core.models import BaseModel
from apps.inventory.models import FulfillmentProvider
from apps.payment.models import Currency, PaymentProvider
from apps.tax.models import TaxProvider, TaxRate


class Customer(BaseModel):
    """
    This class represents a customer in the store.
    """

    email = models.EmailField(
        validators=[EmailValidator()],
        unique=True,
        help_text="Email of the customer, must be unique.",
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="First name of the customer, not required.",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Last name of the customer, not required.",
    )
    billing_address = models.OneToOneField(
        "Address",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        help_text="Billing address of the customer, not required.",
    )
    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Phone number of the customer, not required.",
    )
    has_account = models.BooleanField(
        default=False, help_text="Indicates whether the customer has an account or not."
    )
    password_hash = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Hashed password of the customer, not required.",
    )
    orders = models.ForeignKey(
        "order.Order",
        on_delete=models.CASCADE,
        related_name="+",
        help_text="Orders placed by the customer.",
    )
    groups = models.ManyToManyField(
        "CustomerGroup", related_name="+", help_text="Groups the customer belongs to."
    )
    metadata = models.JSONField(
        blank=True,
        null=True,
        help_text="Metadata related to the customer, not required.",
    )

    def __str__(self):
        """
        Returns a string representation of the customer, in the format
        '{first_name} {last_name} ({email})'.
        """
        return f"{self.first_name} {self.last_name} ({self.email})"


class CustomerGroup(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    customers = models.ManyToManyField(Customer, related_name="+")
    price_lists = models.ManyToManyField("product.PriceList")
    metadata = models.JSONField(null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Country(BaseModel):
    iso_2 = models.CharField(max_length=255, unique=True)
    iso_3 = models.CharField(max_length=255)
    num_code = models.IntegerField()
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    region = models.ForeignKey(
        "Region", on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )


class Address(BaseModel):
    company = models.CharField(max_length=255, null=True, blank=True)
    # first_name = models.CharField(max_length=255, null=True, blank=True)
    # last_name = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="+")
    province = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField()


class Region(BaseModel):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="+")
    # tax_rate = models.FloatField()
    tax_rates = models.ForeignKey(
        TaxRate, on_delete=models.SET_NULL, related_name="+", null=True, blank=True
    )
    tax_code = models.CharField(max_length=100, null=True)
    gift_cards_taxable = models.BooleanField(default=True)
    automatic_taxes = models.BooleanField(default=True)
    countries = models.ManyToManyField(Country, related_name="+")
    tax_provider = models.ForeignKey(TaxProvider, on_delete=models.SET_NULL, null=True)
    payment_providers = models.ManyToManyField(PaymentProvider, related_name="+")
    fulfillment_providers = models.ManyToManyField(
        FulfillmentProvider, related_name="+"
    )
    metadata = models.JSONField(null=True)
    includes_tax = models.BooleanField(default=False)


# {
#   "$schema": "http://json-schema.org/draft-07/schema#",
#   "title": "Customer",
#   "type": "object",
#   "properties": {
#     "id": {
#       "type": "integer",
#       "description": "Primary key of the customer."
#     },
#     "email": {
#       "type": "string",
#       "format": "email",
#       "description": "Email of the customer, must be unique."
#     },
#     "first_name": {
#       "type": "string",
#       "maxLength": 255,
#       "description": "First name of the customer, not required."
#     },
#     "last_name": {
#       "type": "string",
#       "maxLength": 255,
#       "description": "Last name of the customer, not required."
#     },
#     "billing_address": {
#       "type": "integer",
#       "description": "ID of the billing address of the customer, not required."
#     },
#     "phone": {
#       "type": "string",
#       "maxLength": 255,
#       "description": "Phone number of the customer, not required."
#     },
#     "has_account": {
#       "type": "boolean",
#       "description": "Indicates whether the customer has an account or not."
#     },
#     "password_hash": {
#       "type": "string",
#       "maxLength": 255,
#       "description": "Hashed password of the customer, not required."
#     },
#     "orders": {
#       "type": "array",
#       "items": {
#         "type": "integer"
#       },
#       "description": "IDs of the orders placed by the customer."
#     },
#     "groups": {
#       "type": "array",
#       "items": {
#         "type": "integer"
#       },
#       "description": "IDs of the groups the customer belongs to."
#     },
#     "metadata": {
#       "type": "object",
#       "description": "Metadata related to the customer, not required."
#     }
#   },
#   "required": [
#     "email",
#     "has_account"
#   ],
#   "example": {
#     "id": 1,
#     "email": "johndoe@example.com",
#     "first_name": "John",
#     "last_name": "Doe",
#     "billing_address": 2,
#     "phone": "555-555-5555",
#     "has_account": true,
#     "password_hash": "hashed_password",
#     "orders": [1, 2, 3],
#     "groups": [1, 2],
#     "metadata": {
#       "favourite_products": [5, 6, 7],
#       "preferred_payment_method": "Credit Card"
#     }
#   }
# }
