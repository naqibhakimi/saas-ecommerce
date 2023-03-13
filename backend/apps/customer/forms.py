from django import forms
from django.forms import fields
from apps.core.forms import BaseForm

from .models import (
    Customer,
    CustomerGroup,
    Country,
    Address,
    Region,
)


class CreateCustomerForm(BaseForm):
    class Meta:
        model = Customer
        fields = (
            "email",
            "first_name",
            "last_name",
            "billing_address",
            "phone",
            "has_account",
            "metadata",
        )


class UpdateCustomerForm(BaseForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model = Customer
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "billing_address",
            "phone",
            "has_account",
            # "orders",
            # "groups",
            # "metadata",
        )


class DeleteCustomerForm(BaseForm):
    class Meta:
        model= Customer
        fields = ("id",)


class CreateCustomerGroupForm(BaseForm):
    class Meta:
        model = CustomerGroup
        fields = (
            "name",
            "customers",
            "price_lists",
            "metadata",
        )


class UpdateCustomerGroupForm(BaseForm):
    class Meta:
        model = CustomerGroup
        fields = (
            "name",
            "customers",
            "price_lists",
            "metadata",
        )


class DeleteCustomerGroupForm(BaseForm):
    class Meta:
        model = CustomerGroup
        fields = ("id",)


class CreateCountryForm(BaseForm):
    class Meta:
        model = Country
        fields = (
            "iso_2",
            "iso_3",
            "num_code",
            "name",
            "display_name",
            "region",
        )


class UpdateCountryForm(BaseForm):
    class Meta:
        model = Country
        fields = (
            "iso_2",
            "iso_3",
            "num_code",
            "name",
            "display_name",
            "region",
        )


class DeleteCountryForm(BaseForm):
    class Meta:
        model = Country
        fields = ("id",)


class CreateAddressForm(BaseForm):
    class Meta:
        model = Address
        fields = (
            "company",
            "address_1",
            "address_2",
            "city",
            "country_code",
            "country",
            "province",
            "postal_code",
            "phone",
            "metadata",
        )


class UpdateAddressForm(BaseForm):
    class Meta:
        model = Address
        fields = (
            "company",
            "address_1",
            "address_2",
            "city",
            "country_code",
            "country",
            "province",
            "postal_code",
            "phone",
            "metadata",
        )


class DeleteAddressForm(BaseForm):
    class Meta:
        model = Address
        fields = ("id",)


class CreateRegionForm(BaseForm):
    class Meta:
        model = Region
        fields = (
            "name",
            "currency",
            # "tax_rates",
            "tax_code",
            "gift_cards_taxable",
            "automatic_taxes",
            "tax_provider",
            "metadata",
            "includes_tax",
        )


class UpdateRegionForm(BaseForm):
    class Meta:
        model = Region
        fields = (
            "name",
            "currency",
            # "tax_rates",
            "tax_code",
            "gift_cards_taxable",
            "automatic_taxes",
            "tax_provider",
            "metadata",
            "includes_tax",
        )


class DeleteRegionForm(BaseForm):
    class Meta:
        model = Region
        fields = ("id",)
