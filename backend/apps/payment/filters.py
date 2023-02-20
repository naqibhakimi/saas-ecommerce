import django_filters

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
        fields = "__all__"


class IdempotencyKeyFilter(django_filters.FilterSet):
    class Meta:
        model = IdempotencyKey
        exclude = "metadata"


class CurrencyFilter(django_filters.FilterSet):
    class Meta:
        model = Currency
        exclude = "metadata"


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        exclude = "metadata"


class PaymentSessionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentSession
        exclude = "metadata"


class PaymentCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentCollection
        exclude = "metadata"


class PaymentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentProvider
        exclude = "metadata"


class RefundFilter(django_filters.FilterSet):
    class Meta:
        model = Refund
        exclude = "metadata"
