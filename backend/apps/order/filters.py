import django_filters

from .models import (
    OrderDiscount,
    OrderGiftCard,
    Order,
    OrderEdit,
    OrderItemChange,
    DraftOrder,
    ClaimOrder,
    ClaimTag,
    ClaimItem,
    ClaimImage,
    Return,
    ReturnItem,
    ReturnReason,
)


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        exclude = ('metadata')



class OrderDiscountFilter(django_filters.FilterSet):
    class Meta:
        model = OrderDiscount
        exclude = ('metadata')

        
class OrderGiftCardFilter(django_filters.FilterSet):
    class Meta:
        model = OrderGiftCard
        exclude = ('metadata')

        
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        exclude = ('metadata')

        
class OrderEditFilter(django_filters.FilterSet):
    class Meta:
        model = OrderEdit
        exclude = ('metadata')

        
class OrderItemChangeFilter(django_filters.FilterSet):
    class Meta:
        model = OrderItemChange
        exclude = ('metadata')

        
class DraftOrderFilter(django_filters.FilterSet):
    class Meta:
        model = DraftOrder
        exclude = ('metadata')

        
class ClaimOrderFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimOrder
        exclude = ('metadata')

        
class ClaimTagFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimTag
        exclude = ('metadata')

        
class ClaimItemFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimItem
        exclude = ('metadata')

        
class ClaimImageFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimImage
        exclude = ('metadata')

        
class ReturnFilter(django_filters.FilterSet):
    class Meta:
        model = Return
        exclude = ('metadata')

        
class ReturnItemFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnItem
        exclude = ('metadata')

        
class ReturnReasonFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnReason
        exclude = ('metadata')

        