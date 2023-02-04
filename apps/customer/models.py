from django.db import models
from apps.core.models import BaseModel
from django.core.validators import EmailValidator
from apps.payment.models import PaymentProvider, Currency
from apps.tax.models import TaxRate, TaxProvider
from apps.inventory.models import FulfillmentProvider


# Create your models here.

class Customer(BaseModel):
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    billing_address = models.OneToOneField(
        'Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    phone = models.CharField(max_length=255, blank=True, null=True)
    has_account = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    orders = models.ForeignKey(
        'order.Order', on_delete=models.CASCADE, related_name='+'
    )
    groups = models.ManyToManyField('CustomerGroup', related_name='+')
    metadata = models.JSONField(blank=True, null=True)


class CustomerGroup(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    customers = models.ManyToManyField(Customer, related_name='+')
    price_lists = models.ManyToManyField('product.PriceList')
    metadata = models.JSONField(null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Country(BaseModel):
    iso_2 = models.CharField(max_length=255, unique=True)
    iso_3 = models.CharField(max_length=255)
    num_code = models.IntegerField()
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True,  related_name='+')


class Address(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,  related_name='+')
    company = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='+')
    province = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField()


class Region(BaseModel):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='+')
    tax_rate = models.FloatField()
    tax_rates = models.ForeignKey(TaxRate, on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    tax_code = models.CharField(max_length=100, null=True)
    gift_cards_taxable = models.BooleanField(default=True)
    automatic_taxes = models.BooleanField(default=True)
    countries = models.ManyToManyField(Country, related_name='+')
    tax_provider = models.ForeignKey(TaxProvider, on_delete=models.SET_NULL, null=True)
    payment_providers = models.ManyToManyField(PaymentProvider, related_name='+')
    fulfillment_providers = models.ManyToManyField(FulfillmentProvider, related_name='+')
    metadata = models.JSONField(null=True)
    includes_tax = models.BooleanField(default=False)

