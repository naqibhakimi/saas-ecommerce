import django_filters

from apps.order.models import OrderDiscount

from .models import (
    IdempotencyKey,
    Currency,
    Payment,
    PaymentSession,
    PaymentCollection,
    PaymentProvider,
    Refund,
)


class OrderDiscountFilter(django_filters.FilterSet):
    class Meta:
        model = OrderDiscount
        exclude = ["metadata"]


class IdempotencyKeyFilter(django_filters.FilterSet):
    class Meta:
        model = IdempotencyKey
        exclude = ["request_params", "response_body"]


class CurrencyFilter(django_filters.FilterSet):
    class Meta:
        model = Currency
        exclude = ["metadata"]


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        exclude = ["metadata", "data"]


class PaymentSessionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentSession
        exclude = ["metadata", "data"]


class PaymentCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentCollection
        exclude = ["metadata"]


class PaymentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentProvider
        exclude = ["metadata"]


class RefundFilter(django_filters.FilterSet):
    class Meta:
        model = Refund
        exclude = ["metadata"]
