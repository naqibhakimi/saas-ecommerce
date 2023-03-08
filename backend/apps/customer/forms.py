from django import forms
from django.forms import fields
from django.forms.models import ModelForm

from .models import (
    Customer,
    CustomerGroup,
    Country,
    Address,
    Region,
)


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "email",
            "first_name",
            "last_name",
            "billing_address",
            "phone",
            "has_account",
            "password_hash",
            "orders",
            "groups",
            "metadata",
        )


class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "email",
            "first_name",
            "last_name",
            # "billing_address",
            "phone",
            "has_account",
            "password_hash",
            # "orders",
            # "groups",
            # "metadata",
        )


class DeleteCustomerForm(forms.ModelForm):
    class Meta:
        fields = ("id",)


class CreateCustomerGroupForm(forms.ModelForm):
    class Meta:
        model = CustomerGroup
        fields = (
            "name"
            "customers"
            "price_lists"
            "metadata"
        )


class UpdateCustomerGroupForm(forms.ModelForm):
    class Meta:
        model = CustomerGroup
        fields = (
            "name"
            "customers"
            "price_lists"
            "metadata"
        )


class DeleteCustomerGroupForm(forms.ModelForm):
    class Meta:
        model = CustomerGroup
        fields = ("id",)


class CreateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            "iso_2"
            "iso_3"
            "num_code"
            "name"
            "display_name"
            "region"
        )


class UpdateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = (
            "iso_2"
            "iso_3"
            "num_code"
            "name"
            "display_name"
            "region"
        )


class DeleteCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ("id",)


class CreateAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "company"
            "first_name"
            "last_name"
            "address_1"
            "address_2"
            "city"
            "country_code"
            "country"
            "province"
            "postal_code"
            "phone"
            "metadata"
        )


class UpdateAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "company"
            "first_name"
            "last_name"
            "address_1"
            "address_2"
            "city"
            "country_code"
            "country"
            "province"
            "postal_code"
            "phone"
            "metadata"
        )


class DeleteAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("id",)


class CreateRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = (
            "name"
            "currency"
            # "tax_rates"
            "tax_code"
            "gift_cards_taxable"
            "automatic_taxes"
            "countries"
            "tax_provider"
            "payment_providers"
            "fulfillment_providers"
            "metadata"
            "includes_tax"
        )


class UpdateRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = (
            "name"
            "currency"
            # "tax_rates"
            "tax_code"
            "gift_cards_taxable"
            "automatic_taxes"
            "countries"
            "tax_provider"
            "payment_providers"
            "fulfillment_providers"
            "metadata"
            "includes_tax"
        )


class DeleteRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ("id",)
