import django_filters

from .models import (
    GiftCard,
    GiftCardTransaction,
)


class GiftCardFilter(django_filters.FilterSet):
    class Meta:
        model = GiftCard
        exclude = "metadata"


class GiftCardTransactionFilter(django_filters.FilterSet):
    class Meta:
        model = GiftCardTransaction
        exclude = "metadata"
