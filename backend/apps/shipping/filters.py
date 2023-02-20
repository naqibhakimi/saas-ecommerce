import django_filters

from .models import (
    ShippingProfileType,
    ShippingProfile,
    ShippingOption,
    ShippingMethod,
    CustomShippingOption,
    ShippingMethodTaxLine,
    ShippingOptionRequirement,
    ShippingTaxRate,
)


class ShippingProfileTypeFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class ShippingProfileFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class ShippingOptionFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class ShippingMethodFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class CustomShippingOptionFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class ShippingMethodTaxLineFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class ShippingOptionRequirementFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"


class ShippingTaxRateFilter(django_filters.FilterSet):
    class Meta:
        exclude = "metadata"
