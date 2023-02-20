import django_filters

from .models import (
    DiscountCondition,
    DiscountRule,
    Discount,
    DiscountConditionCustomerGroup,
    DiscountConditionProductCollection,
    DiscountConditionProductTag,
    DiscountConditionProductType,
    DiscountConditionProduct,
)


class DiscountConditionFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountCondition
        exclude = "metadata"


class DiscountRuleFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountRule
        exclude = "metadata"


class DiscountFilter(django_filters.FilterSet):
    class Meta:
        model = Discount
        exclude = "metadata"


class DiscountConditionCustomerGroupFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionCustomerGroup
        exclude = "metadata"


class DiscountConditionProductCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductCollection
        exclude = "metadata"


class DiscountConditionProductTagFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductTag
        exclude = "metadata"


class DiscountConditionProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductType
        exclude = "metadata"


class DiscountConditionProductFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProduct
        exclude = "metadata"
