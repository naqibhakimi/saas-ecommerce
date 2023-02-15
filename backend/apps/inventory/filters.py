import django_filters

from .models import (
    AnalyticsConfig,
    BatchJob,
    Fulfillment,
    FulfillmentItem,
    FulfillmentProvider,
    TrackingLink,
)

class OrderDiscountFilter(django_filters.FilterSet):
    class Meta:
        model = OrderDiscount
        fields = '__all__'


class AnalyticsConfigFilter(django_filters.FilterSet):
    class Meta:
        model = AnalyticsConfig
        exception = ('metadata')


class BatchJobFilter(django_filters.FilterSet):
    class Meta:
        model = BatchJob
        exception = ('metadata')


class FulfillmentFilter(django_filters.FilterSet):
    class Meta:
        model = Fulfillment
        exception = ('metadata')


class FulfillmentItemFilter(django_filters.FilterSet):
    class Meta:
        model = FulfillmentItem
        exception = ('metadata')


class FulfillmentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = FulfillmentProvider
        exception = ('metadata')


class TrackingLinkFilter(django_filters.FilterSet):
    class Meta:
        model = TrackingLink
        exception = ('metadata')

