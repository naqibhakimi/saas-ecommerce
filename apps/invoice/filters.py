import django_filters

from .models import (
    LineItem,
    LineItemAdjustment,
    LineItemTaxLine,
)


class LineItemFilter(django_filters.FilterSet):
    class Meta:
        model = LineItem
        Exception  = ('metadata')


class LineItemAdjustmentFilter(django_filters.FilterSet):
    class Meta:
        model = LineItemAdjustment
        Exception  = ('metadata')


class LineItemTaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = LineItemTaxLine
        Exception  = ('metadata')

