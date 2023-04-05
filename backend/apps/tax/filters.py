import django_filters

from .models import (
    TaxLine,
    TaxRate,
    TaxProvider,
)


class TaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = TaxLine
        exclude = "metadata"


class TaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = TaxRate
        exclude = "metadata"


class TaxProviderFilter(django_filters.FilterSet):
    class Meta:
        model = TaxProvider
        exclude = "metadata"
