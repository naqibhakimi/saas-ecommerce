import django_filters

from .models import (
    Customer,
    CustomerGroup,
    Country,
    Address,
    Region,
)


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        exclude = "metadata"


class CustomerGroupFilter(django_filters.FilterSet):
    class Meta:
        model = CustomerGroup
        exclude = "metadata"


class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = Country
        fields = "__all__"


class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        exclude = "metadata"


class RegionFilter(django_filters.FilterSet):
    class Meta:
        model = Region
        exclude = "metadata"
