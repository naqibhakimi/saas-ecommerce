import graphene


class BaseConnection(graphene.Connection):
    class Meta:
        abstract = True


class DiscountConditionConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountRuleConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountConditionCustomerGroupConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountConditionProductCollectionConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountConditionProductTagConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountConditionProductTypeConnection(BaseConnection):
    class Meta:
        abstract = True


class DiscountConditionProductConnection(BaseConnection):
    class Meta:
        abstract = True
