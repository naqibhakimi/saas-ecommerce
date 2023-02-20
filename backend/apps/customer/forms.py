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


# class CustomerGroupForm(forms.ModelForm):
#     class Meta:
#         model = CustomerGroup
#         # fields = ("","")


# class CountryForm(forms.ModelForm):
#     class Meta:
#         model = Country
#         # fields = ("","")


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         # fields = ("","")


# class RegionForm(forms.ModelForm):
#     class Meta:
#         model = Region
#         fields = ("","")
