import django_filters

from .models import (
    OrderDiscount,
    OrderGiftCard,
    Order,
    Customer,
    Country,
    Address,
    AnalyticsConfig,
    BatchJob,
    Discount,
    GiftCard,
    LineItem,
    Payment,
    PaymentSession,
    ShippingMethod,
    SalesChannel,
    Cart,
    ClaimTag,
    ClaimItem,
    ClaimImage,
    ClaimOrder,
    Return,
    Fulfillment,
    Currency,
    ShippingOption,
    CustomShippingOption,
    PriceList,
    CustomerGroup,
    DiscountConditionCustomerGroup,
    DiscountConditionProductCollection,
    DiscountConditionProductTag,
    ProductType,
    DiscountConditionProductType,
    ProductTag,
    Product,
    DiscountConditionProduct,
    DiscountCondition,
    DiscountRule,
    DraftOrder,
    FulfillmentItem,
    FulfillmentProvider,
    GiftCardTransaction,
    IdempotencyKey,
    Image,
    Invite,
    LineItemAdjustment,
    TaxLine,
    LineItemTaxLine,
    MoneyAmount,
    Note,
    NotificationProvider,
    Notification,
    Oauth,
    OrderEdit,
    OrderItemChange,
    PaymentCollectionStatus,
    PaymentCollectionType,
    PaymentCollection,
    PaymentProvider,
    ProductCategory,
    ProductCollection,
    ProductOptionValue,
    ProductOption,
    ProductTaxRate,
    ProductTypeTaxRate,
    ProductVariantInventoryItem,
    ProductVariant,
    PublishableApiKeySalesChannel,
    PublishableApiKey,
    Refund,
    Region,
    ReturnItem,
    ReturnReason,
    ReturnStatus,
    SalesChannelLocation,
    ShippingMethodTaxLine,
    ShippingOptionRequirement,
    ShippingProfileType,
    ShippingProfile,
    TaxRate,
    ShippingTaxRate,
    StagedJob,
    Store,
    Swap,
    TaxProvider,
    TrackingLink,
)

class OrderDiscountFilter(django_filters.FilterSet):
    class Meta:
        model = OrderDiscount
        fields = '__all__'


class OrderGiftCardFilter(django_filters.FilterSet):
    class Meta:
        model = OrderGiftCard
        fields = '__all__'


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        exclude = ('metadata')


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        exclude = ('metadata')


class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = Country
        fields = '__all__'


class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        exclude = ('metadata')


class AnalyticsConfigFilter(django_filters.FilterSet):
    class Meta:
        model = AnalyticsConfig
        fields = '__all__'


class BatchJobFilter(django_filters.FilterSet):
    class Meta:
        model = BatchJob
        exclude = ('context', 'result')


class DiscountFilter(django_filters.FilterSet):
    class Meta:
        model = Discount
        exclude = ('metadata')


class GiftCardFilter(django_filters.FilterSet):
    class Meta:
        model = GiftCard
        exclude = ('metadata')


class LineItemFilter(django_filters.FilterSet):
    class Meta:
        model = LineItem
        exclude = ('metadata')


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        exclude = ('metadata', 'data')


class PaymentSessionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentSession
        exclude = ('data')


class ShippingMethodFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingMethod
        exclude = ('data')


class SalesChannelFilter(django_filters.FilterSet):
    class Meta:
        model = SalesChannel
        fields = '__all__'


class CartFilter(django_filters.FilterSet):
    class Meta:
        model = Cart
        exclude = ('context', 'metadata')


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


class ClaimOrderFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimOrder
        exclude = ('metadata')


class ReturnFilter(django_filters.FilterSet):
    class Meta:
        model = Return
        exclude = ('metadata', 'shipping_data')


class FulfillmentFilter(django_filters.FilterSet):
    class Meta:
        model = Fulfillment
        exclude = ('tracking_numbers', 'data', 'metadata')


class CurrencyFilter(django_filters.FilterSet):
    class Meta:
        model = Currency
        fields = '__all__'


class ShippingOptionFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingOption
        exclude = ('data', 'metadata')


class CustomShippingOptionFilter(django_filters.FilterSet):
    class Meta:
        model = CustomShippingOption
        exclude = ('metadata')


class PriceListFilter(django_filters.FilterSet):
    class Meta:
        model = PriceList
        fields = '__all__'


class CustomerGroupFilter(django_filters.FilterSet):
    class Meta:
        model = CustomerGroup
        exclude = ('metadata')


class DiscountConditionCustomerGroupFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionCustomerGroup
        exclude = ('metadata')


class DiscountConditionProductCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductCollection
        exclude = ('metadata')


class DiscountConditionProductTagFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductTag
        exclude = ('metadata')


class ProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ProductType
        exclude = ('metadata')


class DiscountConditionProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductType
        exclude = ('metadata')


class ProductTagFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTag
        exclude = ('metadata')


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        exclude = ('metadata')


class DiscountConditionProductFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProduct
        exclude = ('metadata')


class DiscountConditionFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountCondition
        exclude = ('metadata')


class DiscountRuleFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountRule
        exclude = ('metadata')


class DraftOrderFilter(django_filters.FilterSet):
    class Meta:
        model = DraftOrder
        exclude = ('metadata')


class FulfillmentItemFilter(django_filters.FilterSet):
    class Meta:
        model = FulfillmentItem
        exclude = ('metadata')


class FulfillmentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = FulfillmentProvider
        exclude = ('metadata')


class GiftCardTransactionFilter(django_filters.FilterSet):
    class Meta:
        model = GiftCardTransaction
        exclude = ('metadata')


class IdempotencyKeyFilter(django_filters.FilterSet):
    class Meta:
        model = IdempotencyKey
        exclude = ('metadata', 'request_params', 'response_body')


class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        exclude = ('metadata')


class InviteFilter(django_filters.FilterSet):
    class Meta:
        model = Invite
        exclude = ('metadata')


class LineItemAdjustmentFilter(django_filters.FilterSet):
    class Meta:
        model = LineItemAdjustment
        exclude = ('metadata')


class TaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = TaxLine
        exclude = ('metadata')


class LineItemTaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = LineItemTaxLine
        exclude = ('metadata')


class MoneyAmountFilter(django_filters.FilterSet):
    class Meta:
        model = MoneyAmount
        exclude = ('metadata')


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        exclude = ('metadata')


class NotificationProviderFilter(django_filters.FilterSet):
    class Meta:
        model = NotificationProvider
        exclude = ('metadata')


class NotificationFilter(django_filters.FilterSet):
    class Meta:
        model = Notification
        exclude = ('metadata')


class OauthFilter(django_filters.FilterSet):
    class Meta:
        model = Oauth
        exclude = ('metadata')


class OrderEditFilter(django_filters.FilterSet):
    class Meta:
        model = OrderEdit
        exclude = ('metadata')


class OrderItemChangeFilter(django_filters.FilterSet):
    class Meta:
        model = OrderItemChange
        exclude = ('metadata')


class PaymentCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentCollection
        exclude = ('metadata')


class PaymentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentProvider
        exclude = ('metadata')


class ProductCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCategory
        exclude = ('metadata')


class ProductCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCollection
        exclude = ('metadata')


class ProductOptionValueFilter(django_filters.FilterSet):
    class Meta:
        model = ProductOptionValue
        exclude = ('metadata')


class ProductOptionFilter(django_filters.FilterSet):
    class Meta:
        model = ProductOption
        exclude = ('metadata')


class ProductTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTaxRate
        exclude = ('metadata')


class ProductTypeTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTypeTaxRate
        exclude = ('metadata')


class ProductVariantInventoryItemFilter(django_filters.FilterSet):
    class Meta:
        model = ProductVariantInventoryItem
        exclude = ('metadata')


class ProductVariantFilter(django_filters.FilterSet):
    class Meta:
        model = ProductVariant
        exclude = ('metadata')


class PublishableApiKeySalesChannelFilter(django_filters.FilterSet):
    class Meta:
        model = PublishableApiKeySalesChannel
        exclude = ('metadata')


class PublishableApiKeyFilter(django_filters.FilterSet):
    class Meta:
        model = PublishableApiKey
        exclude = ('metadata')


class RefundFilter(django_filters.FilterSet):
    class Meta:
        model = Refund
        exclude = ('metadata')


class RegionFilter(django_filters.FilterSet):
    class Meta:
        model = Region
        exclude = ('metadata')


class ReturnItemFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnItem
        exclude = ('metadata')


class ReturnReasonFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnReason
        exclude = ('metadata')

class SalesChannelLocationFilter(django_filters.FilterSet):
    class Meta:
        model = SalesChannelLocation
        exclude = ('metadata')


class ShippingMethodTaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingMethodTaxLine
        exclude = ('metadata')


class ShippingOptionRequirementFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingOptionRequirement
        exclude = ('metadata')

class ShippingProfileFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingProfile
        exclude = ('metadata')


class TaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = TaxRate
        exclude = ('metadata')


class ShippingTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingTaxRate
        exclude = ('metadata')


class StagedJobFilter(django_filters.FilterSet):
    class Meta:
        model = StagedJob
        exclude = ('metadata', 'options', 'data')


class StoreFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        exclude = ('metadata')


class SwapFilter(django_filters.FilterSet):
    class Meta:
        model = Swap
        exclude = ('metadata')


class TaxProviderFilter(django_filters.FilterSet):
    class Meta:
        model = TaxProvider
        exclude = ('metadata')


class TrackingLinkFilter(django_filters.FilterSet):
    class Meta:
        model = TrackingLink
        exclude = ('metadata')

