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

class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields = '__all__'


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
        fields = '__all__'


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'


class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = Country
        fields = '__all__'


class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields = '__all__'


class AnalyticsConfigFilter(django_filters.FilterSet):
    class Meta:
        model = AnalyticsConfig
        fields = '__all__'


class BatchJobFilter(django_filters.FilterSet):
    class Meta:
        model = BatchJob
        fields = '__all__'


class DiscountFilter(django_filters.FilterSet):
    class Meta:
        model = Discount
        fields = '__all__'


class GiftCardFilter(django_filters.FilterSet):
    class Meta:
        model = GiftCard
        fields = '__all__'


class LineItemFilter(django_filters.FilterSet):
    class Meta:
        model = LineItem
        fields = '__all__'


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentSessionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentSession
        fields = '__all__'


class ShippingMethodFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingMethod
        fields = '__all__'


class SalesChannelFilter(django_filters.FilterSet):
    class Meta:
        model = SalesChannel
        fields = '__all__'


class CartFilter(django_filters.FilterSet):
    class Meta:
        model = Cart
        fields = '__all__'


class ClaimTagFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimTag
        fields = '__all__'


class ClaimItemFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimItem
        fields = '__all__'


class ClaimImageFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimImage
        fields = '__all__'


class ClaimOrderFilter(django_filters.FilterSet):
    class Meta:
        model = ClaimOrder
        fields = '__all__'


class ReturnFilter(django_filters.FilterSet):
    class Meta:
        model = Return
        fields = '__all__'


class FulfillmentFilter(django_filters.FilterSet):
    class Meta:
        model = Fulfillment
        fields = '__all__'


class CurrencyFilter(django_filters.FilterSet):
    class Meta:
        model = Currency
        fields = '__all__'


class ShippingOptionFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingOption
        fields = '__all__'


class CustomShippingOptionFilter(django_filters.FilterSet):
    class Meta:
        model = CustomShippingOption
        fields = '__all__'


class PriceListFilter(django_filters.FilterSet):
    class Meta:
        model = PriceList
        fields = '__all__'


class CustomerGroupFilter(django_filters.FilterSet):
    class Meta:
        model = CustomerGroup
        fields = '__all__'


class DiscountConditionCustomerGroupFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionCustomerGroup
        fields = '__all__'


class DiscountConditionProductCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductCollection
        fields = '__all__'


class DiscountConditionProductTagFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductTag
        fields = '__all__'


class ProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ProductType
        fields = '__all__'


class DiscountConditionProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProductType
        fields = '__all__'


class ProductTagFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTag
        fields = '__all__'


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'


class DiscountConditionProductFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountConditionProduct
        fields = '__all__'


class DiscountConditionFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountCondition
        fields = '__all__'


class DiscountRuleFilter(django_filters.FilterSet):
    class Meta:
        model = DiscountRule
        fields = '__all__'


class DraftOrderFilter(django_filters.FilterSet):
    class Meta:
        model = DraftOrder
        fields = '__all__'


class FulfillmentItemFilter(django_filters.FilterSet):
    class Meta:
        model = FulfillmentItem
        fields = '__all__'


class FulfillmentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = FulfillmentProvider
        fields = '__all__'


class GiftCardTransactionFilter(django_filters.FilterSet):
    class Meta:
        model = GiftCardTransaction
        fields = '__all__'


class IdempotencyKeyFilter(django_filters.FilterSet):
    class Meta:
        model = IdempotencyKey
        fields = '__all__'


class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = '__all__'


class InviteFilter(django_filters.FilterSet):
    class Meta:
        model = Invite
        fields = '__all__'


class LineItemAdjustmentFilter(django_filters.FilterSet):
    class Meta:
        model = LineItemAdjustment
        fields = '__all__'


class TaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = TaxLine
        fields = '__all__'


class LineItemTaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = LineItemTaxLine
        fields = '__all__'


class MoneyAmountFilter(django_filters.FilterSet):
    class Meta:
        model = MoneyAmount
        fields = '__all__'


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = '__all__'


class NotificationProviderFilter(django_filters.FilterSet):
    class Meta:
        model = NotificationProvider
        fields = '__all__'


class NotificationFilter(django_filters.FilterSet):
    class Meta:
        model = Notification
        fields = '__all__'


class OauthFilter(django_filters.FilterSet):
    class Meta:
        model = Oauth
        fields = '__all__'


class OrderEditFilter(django_filters.FilterSet):
    class Meta:
        model = OrderEdit
        fields = '__all__'


class OrderItemChangeFilter(django_filters.FilterSet):
    class Meta:
        model = OrderItemChange
        fields = '__all__'


class PaymentCollectionStatusFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentCollectionStatus
        fields = '__all__'


class PaymentCollectionTypeFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentCollectionType
        fields = '__all__'


class PaymentCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentCollection
        fields = '__all__'


class PaymentProviderFilter(django_filters.FilterSet):
    class Meta:
        model = PaymentProvider
        fields = '__all__'


class ProductCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCollection
        fields = '__all__'


class ProductOptionValueFilter(django_filters.FilterSet):
    class Meta:
        model = ProductOptionValue
        fields = '__all__'


class ProductOptionFilter(django_filters.FilterSet):
    class Meta:
        model = ProductOption
        fields = '__all__'


class ProductTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTaxRate
        fields = '__all__'


class ProductTypeTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ProductTypeTaxRate
        fields = '__all__'


class ProductVariantInventoryItemFilter(django_filters.FilterSet):
    class Meta:
        model = ProductVariantInventoryItem
        fields = '__all__'


class ProductVariantFilter(django_filters.FilterSet):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class PublishableApiKeySalesChannelFilter(django_filters.FilterSet):
    class Meta:
        model = PublishableApiKeySalesChannel
        fields = '__all__'


class PublishableApiKeyFilter(django_filters.FilterSet):
    class Meta:
        model = PublishableApiKey
        fields = '__all__'


class RefundFilter(django_filters.FilterSet):
    class Meta:
        model = Refund
        fields = '__all__'


class RegionFilter(django_filters.FilterSet):
    class Meta:
        model = Region
        fields = '__all__'


class ReturnItemFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnItem
        fields = '__all__'


class ReturnReasonFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnReason
        fields = '__all__'


class ReturnStatusFilter(django_filters.FilterSet):
    class Meta:
        model = ReturnStatus
        fields = '__all__'


class SalesChannelLocationFilter(django_filters.FilterSet):
    class Meta:
        model = SalesChannelLocation
        fields = '__all__'


class ShippingMethodTaxLineFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingMethodTaxLine
        fields = '__all__'


class ShippingOptionRequirementFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingOptionRequirement
        fields = '__all__'


class ShippingProfileTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingProfileType
        fields = '__all__'


class ShippingProfileFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingProfile
        fields = '__all__'


class TaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = TaxRate
        fields = '__all__'


class ShippingTaxRateFilter(django_filters.FilterSet):
    class Meta:
        model = ShippingTaxRate
        fields = '__all__'


class StagedJobFilter(django_filters.FilterSet):
    class Meta:
        model = StagedJob
        fields = '__all__'


class StoreFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        fields = '__all__'


class SwapFilter(django_filters.FilterSet):
    class Meta:
        model = Swap
        fields = '__all__'


class TaxProviderFilter(django_filters.FilterSet):
    class Meta:
        model = TaxProvider
        fields = '__all__'


class TrackingLinkFilter(django_filters.FilterSet):
    class Meta:
        model = TrackingLink
        fields = '__all__'

