from graphene_django import DjangoObjectType
import graphene

from core.types import Node

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
from .filters import (
    OrderDiscountFilter,
    OrderGiftCardFilter,
    OrderFilter,
    CustomerFilter,
    CountryFilter,
    AddressFilter,
    AnalyticsConfigFilter,
    BatchJobStatusFilter,
    BatchJobFilter,
    DiscountFilter,
    GiftCardFilter,
    LineItemFilter,
    PaymentFilter,
    PaymentSessionFilter,
    ShippingMethodFilter,
    SalesChannelFilter,
    CartFilter,
    ClaimTagFilter,
    ClaimItemFilter,
    ClaimImageFilter,
    ClaimOrderFilter,
    ReturnFilter,
    FulfillmentFilter,
    CurrencyFilter,
    ShippingOptionFilter,
    CustomShippingOptionFilter,
    PriceListFilter,
    CustomerGroupFilter,
    DiscountConditionCustomerGroupFilter,
    DiscountConditionProductCollectionFilter,
    DiscountConditionProductTagFilter,
    ProductTypeFilter,
    DiscountConditionProductTypeFilter,
    ProductTagFilter,
    ProductFilter,
    DiscountConditionProductFilter,
    DiscountConditionFilter,
    DiscountRuleFilter,
    DraftOrderFilter,
    FulfillmentItemFilter,
    FulfillmentProviderFilter,
    GiftCardTransactionFilter,
    IdempotencyKeyFilter,
    ImageFilter,
    InviteFilter,
    LineItemAdjustmentFilter,
    TaxLineFilter,
    LineItemTaxLineFilter,
    MoneyAmountFilter,
    NoteFilter,
    NotificationProviderFilter,
    NotificationFilter,
    OauthFilter,
    OrderEditFilter,
    OrderItemChangeFilter,
    PaymentCollectionStatusFilter,
    PaymentCollectionTypeFilter,
    PaymentCollectionFilter,
    PaymentProviderFilter,
    ProductCategoryFilter,
    ProductCollectionFilter,
    ProductOptionValueFilter,
    ProductOptionFilter,
    ProductTaxRateFilter,
    ProductTypeTaxRateFilter,
    ProductVariantInventoryItemFilter,
    ProductVariantFilter,
    PublishableApiKeySalesChannelFilter,
    PublishableApiKeyFilter,
    RefundFilter,
    RegionFilter,
    ReturnItemFilter,
    ReturnReasonFilter,
    ReturnStatusFilter,
    SalesChannelLocationFilter,
    ShippingMethodTaxLineFilter,
    ShippingOptionRequirementFilter,
    ShippingProfileTypeFilter,
    ShippingProfileFilter,
    TaxRateFilter,
    ShippingTaxRateFilter,
    StagedJobFilter,
    StoreFilter,
    SwapFilter,
    TaxProviderFilter,
    TrackingLinkFilter,
)
from .connections import (
    OrderDiscountConnection,
    OrderGiftCardConnection,
    OrderConnection,
    CustomerConnection,
    CountryConnection,
    AddressConnection,
    AnalyticsConfigConnection,
    BatchJobStatusConnection,
    BatchJobConnection,
    DiscountConnection,
    GiftCardConnection,
    LineItemConnection,
    PaymentConnection,
    PaymentSessionConnection,
    ShippingMethodConnection,
    SalesChannelConnection,
    CartConnection,
    ClaimTagConnection,
    ClaimItemConnection,
    ClaimImageConnection,
    ClaimOrderConnection,
    ReturnConnection,
    FulfillmentConnection,
    CurrencyConnection,
    ShippingOptionConnection,
    CustomShippingOptionConnection,
    PriceListConnection,
    CustomerGroupConnection,
    DiscountConditionCustomerGroupConnection,
    DiscountConditionProductCollectionConnection,
    DiscountConditionProductTagConnection,
    ProductTypeConnection,
    DiscountConditionProductTypeConnection,
    ProductTagConnection,
    ProductConnection,
    DiscountConditionProductConnection,
    DiscountConditionConnection,
    DiscountRuleConnection,
    DraftOrderConnection,
    FulfillmentItemConnection,
    FulfillmentProviderConnection,
    GiftCardTransactionConnection,
    IdempotencyKeyConnection,
    ImageConnection,
    InviteConnection,
    LineItemAdjustmentConnection,
    TaxLineConnection,
    LineItemTaxLineConnection,
    MoneyAmountConnection,
    NoteConnection,
    NotificationProviderConnection,
    NotificationConnection,
    OauthConnection,
    OrderEditConnection,
    OrderItemChangeConnection,
    PaymentCollectionStatusConnection,
    PaymentCollectionTypeConnection,
    PaymentCollectionConnection,
    PaymentProviderConnection,
    ProductCategoryConnection,
    ProductCollectionConnection,
    ProductOptionValueConnection,
    ProductOptionConnection,
    ProductTaxRateConnection,
    ProductTypeTaxRateConnection,
    ProductVariantInventoryItemConnection,
    ProductVariantConnection,
    PublishableApiKeySalesChannelConnection,
    PublishableApiKeyConnection,
    RefundConnection,
    RegionConnection,
    ReturnItemConnection,
    ReturnReasonConnection,
    ReturnStatusConnection,
    SalesChannelLocationConnection,
    ShippingMethodTaxLineConnection,
    ShippingOptionRequirementConnection,
    ShippingProfileTypeConnection,
    ShippingProfileConnection,
    TaxRateConnection,
    ShippingTaxRateConnection,
    StagedJobConnection,
    StoreConnection,
    SwapConnection,
    TaxProviderConnection,
    TrackingLinkConnection,
)



class OrderDiscountNode(Node, DjangoObjectType):
    class Meta:
        model = OrderDiscount
        filterset_class = OrderDiscountFilter
        interfaces = (graphene.Node)
        connection_class = OrderDiscountConnection 

    
class OrderGiftCardNode(Node, DjangoObjectType):
    class Meta:
        model = OrderGiftCard
        filterset_class = OrderGiftCardFilter
        interfaces = (graphene.Node)
        connection_class = OrderGiftCardConnection 

    
class OrderNode(Node, DjangoObjectType):
    class Meta:
        model = Order
        filterset_class = OrderFilter
        interfaces = (graphene.Node)
        connection_class = OrderConnection 

    
class CustomerNode(Node, DjangoObjectType):
    class Meta:
        model = Customer
        filterset_class = CustomerFilter
        interfaces = (graphene.Node)
        connection_class = CustomerConnection 

    
class CountryNode(Node, DjangoObjectType):
    class Meta:
        model = Country
        filterset_class = CountryFilter
        interfaces = (graphene.Node)
        connection_class = CountryConnection 

    
class AddressNode(Node, DjangoObjectType):
    class Meta:
        model = Address
        filterset_class = AddressFilter
        interfaces = (graphene.Node)
        connection_class = AddressConnection 

    
class AnalyticsConfigNode(Node, DjangoObjectType):
    class Meta:
        model = AnalyticsConfig
        filterset_class = AnalyticsConfigFilter
        interfaces = (graphene.Node)
        connection_class = AnalyticsConfigConnection 


    
class BatchJobNode(Node, DjangoObjectType):
    class Meta:
        model = BatchJob
        filterset_class = BatchJobFilter
        interfaces = (graphene.Node)
        connection_class = BatchJobConnection 

    
class DiscountNode(Node, DjangoObjectType):
    class Meta:
        model = Discount
        filterset_class = DiscountFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConnection 

    
class GiftCardNode(Node, DjangoObjectType):
    class Meta:
        model = GiftCard
        filterset_class = GiftCardFilter
        interfaces = (graphene.Node)
        connection_class = GiftCardConnection 

    
class LineItemNode(Node, DjangoObjectType):
    class Meta:
        model = LineItem
        filterset_class = LineItemFilter
        interfaces = (graphene.Node)
        connection_class = LineItemConnection 

    
class PaymentNode(Node, DjangoObjectType):
    class Meta:
        model = Payment
        filterset_class = PaymentFilter
        interfaces = (graphene.Node)
        connection_class = PaymentConnection 

    
class PaymentSessionNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentSession
        filterset_class = PaymentSessionFilter
        interfaces = (graphene.Node)
        connection_class = PaymentSessionConnection 

    
class ShippingMethodNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingMethod
        filterset_class = ShippingMethodFilter
        interfaces = (graphene.Node)
        connection_class = ShippingMethodConnection 

    
class SalesChannelNode(Node, DjangoObjectType):
    class Meta:
        model = SalesChannel
        filterset_class = SalesChannelFilter
        interfaces = (graphene.Node)
        connection_class = SalesChannelConnection 

    
class CartNode(Node, DjangoObjectType):
    class Meta:
        model = Cart
        filterset_class = CartFilter
        interfaces = (graphene.Node)
        connection_class = CartConnection 

    
class ClaimTagNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimTag
        filterset_class = ClaimTagFilter
        interfaces = (graphene.Node)
        connection_class = ClaimTagConnection 

    
class ClaimItemNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimItem
        filterset_class = ClaimItemFilter
        interfaces = (graphene.Node)
        connection_class = ClaimItemConnection 

    
class ClaimImageNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimImage
        filterset_class = ClaimImageFilter
        interfaces = (graphene.Node)
        connection_class = ClaimImageConnection 

    
class ClaimOrderNode(Node, DjangoObjectType):
    class Meta:
        model = ClaimOrder
        filterset_class = ClaimOrderFilter
        interfaces = (graphene.Node)
        connection_class = ClaimOrderConnection 

    
class ReturnNode(Node, DjangoObjectType):
    class Meta:
        model = Return
        filterset_class = ReturnFilter
        interfaces = (graphene.Node)
        connection_class = ReturnConnection 

    
class FulfillmentNode(Node, DjangoObjectType):
    class Meta:
        model = Fulfillment
        filterset_class = FulfillmentFilter
        interfaces = (graphene.Node)
        connection_class = FulfillmentConnection 

    
class CurrencyNode(Node, DjangoObjectType):
    class Meta:
        model = Currency
        filterset_class = CurrencyFilter
        interfaces = (graphene.Node)
        connection_class = CurrencyConnection 

    
class ShippingOptionNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingOption
        filterset_class = ShippingOptionFilter
        interfaces = (graphene.Node)
        connection_class = ShippingOptionConnection 

    
class CustomShippingOptionNode(Node, DjangoObjectType):
    class Meta:
        model = CustomShippingOption
        filterset_class = CustomShippingOptionFilter
        interfaces = (graphene.Node)
        connection_class = CustomShippingOptionConnection 

    
class PriceListNode(Node, DjangoObjectType):
    class Meta:
        model = PriceList
        filterset_class = PriceListFilter
        interfaces = (graphene.Node)
        connection_class = PriceListConnection 

    
class CustomerGroupNode(Node, DjangoObjectType):
    class Meta:
        model = CustomerGroup
        filterset_class = CustomerGroupFilter
        interfaces = (graphene.Node)
        connection_class = CustomerGroupConnection 

    
class DiscountConditionCustomerGroupNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionCustomerGroup
        filterset_class = DiscountConditionCustomerGroupFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConditionCustomerGroupConnection 

    
class DiscountConditionProductCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProductCollection
        filterset_class = DiscountConditionProductCollectionFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConditionProductCollectionConnection 

    
class DiscountConditionProductTagNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProductTag
        filterset_class = DiscountConditionProductTagFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConditionProductTagConnection 

    
class ProductTypeNode(Node, DjangoObjectType):
    class Meta:
        model = ProductType
        filterset_class = ProductTypeFilter
        interfaces = (graphene.Node)
        connection_class = ProductTypeConnection 

    
class DiscountConditionProductTypeNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProductType
        filterset_class = DiscountConditionProductTypeFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConditionProductTypeConnection 

    
class ProductTagNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTag
        filterset_class = ProductTagFilter
        interfaces = (graphene.Node)
        connection_class = ProductTagConnection 

    
class ProductNode(Node, DjangoObjectType):
    class Meta:
        model = Product
        filterset_class = ProductFilter
        interfaces = (graphene.Node)
        connection_class = ProductConnection 

    
class DiscountConditionProductNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountConditionProduct
        filterset_class = DiscountConditionProductFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConditionProductConnection 

    
class DiscountConditionNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountCondition
        filterset_class = DiscountConditionFilter
        interfaces = (graphene.Node)
        connection_class = DiscountConditionConnection 

    
class DiscountRuleNode(Node, DjangoObjectType):
    class Meta:
        model = DiscountRule
        filterset_class = DiscountRuleFilter
        interfaces = (graphene.Node)
        connection_class = DiscountRuleConnection 

    
class DraftOrderNode(Node, DjangoObjectType):
    class Meta:
        model = DraftOrder
        filterset_class = DraftOrderFilter
        interfaces = (graphene.Node)
        connection_class = DraftOrderConnection 

    
class FulfillmentItemNode(Node, DjangoObjectType):
    class Meta:
        model = FulfillmentItem
        filterset_class = FulfillmentItemFilter
        interfaces = (graphene.Node)
        connection_class = FulfillmentItemConnection 

    
class FulfillmentProviderNode(Node, DjangoObjectType):
    class Meta:
        model = FulfillmentProvider
        filterset_class = FulfillmentProviderFilter
        interfaces = (graphene.Node)
        connection_class = FulfillmentProviderConnection 

    
class GiftCardTransactionNode(Node, DjangoObjectType):
    class Meta:
        model = GiftCardTransaction
        filterset_class = GiftCardTransactionFilter
        interfaces = (graphene.Node)
        connection_class = GiftCardTransactionConnection 

    
class IdempotencyKeyNode(Node, DjangoObjectType):
    class Meta:
        model = IdempotencyKey
        filterset_class = IdempotencyKeyFilter
        interfaces = (graphene.Node)
        connection_class = IdempotencyKeyConnection 

    
class ImageNode(Node, DjangoObjectType):
    class Meta:
        model = Image
        filterset_class = ImageFilter
        interfaces = (graphene.Node)
        connection_class = ImageConnection 

    
class InviteNode(Node, DjangoObjectType):
    class Meta:
        model = Invite
        filterset_class = InviteFilter
        interfaces = (graphene.Node)
        connection_class = InviteConnection 

    
class LineItemAdjustmentNode(Node, DjangoObjectType):
    class Meta:
        model = LineItemAdjustment
        filterset_class = LineItemAdjustmentFilter
        interfaces = (graphene.Node)
        connection_class = LineItemAdjustmentConnection 

    
class TaxLineNode(Node, DjangoObjectType):
    class Meta:
        model = TaxLine
        filterset_class = TaxLineFilter
        interfaces = (graphene.Node)
        connection_class = TaxLineConnection 

    
class LineItemTaxLineNode(Node, DjangoObjectType):
    class Meta:
        model = LineItemTaxLine
        filterset_class = LineItemTaxLineFilter
        interfaces = (graphene.Node)
        connection_class = LineItemTaxLineConnection 

    
class MoneyAmountNode(Node, DjangoObjectType):
    class Meta:
        model = MoneyAmount
        filterset_class = MoneyAmountFilter
        interfaces = (graphene.Node)
        connection_class = MoneyAmountConnection 

    
class NoteNode(Node, DjangoObjectType):
    class Meta:
        model = Note
        filterset_class = NoteFilter
        interfaces = (graphene.Node)
        connection_class = NoteConnection 

    
class NotificationProviderNode(Node, DjangoObjectType):
    class Meta:
        model = NotificationProvider
        filterset_class = NotificationProviderFilter
        interfaces = (graphene.Node)
        connection_class = NotificationProviderConnection 

    
class NotificationNode(Node, DjangoObjectType):
    class Meta:
        model = Notification
        filterset_class = NotificationFilter
        interfaces = (graphene.Node)
        connection_class = NotificationConnection 

    
class OauthNode(Node, DjangoObjectType):
    class Meta:
        model = Oauth
        filterset_class = OauthFilter
        interfaces = (graphene.Node)
        connection_class = OauthConnection 

    
class OrderEditNode(Node, DjangoObjectType):
    class Meta:
        model = OrderEdit
        filterset_class = OrderEditFilter
        interfaces = (graphene.Node)
        connection_class = OrderEditConnection 

    
class OrderItemChangeNode(Node, DjangoObjectType):
    class Meta:
        model = OrderItemChange
        filterset_class = OrderItemChangeFilter
        interfaces = (graphene.Node)
        connection_class = OrderItemChangeConnection 

    
class PaymentCollectionStatusNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentCollectionStatus
        filterset_class = PaymentCollectionStatusFilter
        interfaces = (graphene.Node)
        connection_class = PaymentCollectionStatusConnection 

    
class PaymentCollectionTypeNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentCollectionType
        filterset_class = PaymentCollectionTypeFilter
        interfaces = (graphene.Node)
        connection_class = PaymentCollectionTypeConnection 

    
class PaymentCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentCollection
        filterset_class = PaymentCollectionFilter
        interfaces = (graphene.Node)
        connection_class = PaymentCollectionConnection 

    
class PaymentProviderNode(Node, DjangoObjectType):
    class Meta:
        model = PaymentProvider
        filterset_class = PaymentProviderFilter
        interfaces = (graphene.Node)
        connection_class = PaymentProviderConnection 

    
class ProductCategoryNode(Node, DjangoObjectType):
    class Meta:
        model = ProductCategory
        filterset_class = ProductCategoryFilter
        interfaces = (graphene.Node)
        connection_class = ProductCategoryConnection 

    
class ProductCollectionNode(Node, DjangoObjectType):
    class Meta:
        model = ProductCollection
        filterset_class = ProductCollectionFilter
        interfaces = (graphene.Node)
        connection_class = ProductCollectionConnection 

    
class ProductOptionValueNode(Node, DjangoObjectType):
    class Meta:
        model = ProductOptionValue
        filterset_class = ProductOptionValueFilter
        interfaces = (graphene.Node)
        connection_class = ProductOptionValueConnection 

    
class ProductOptionNode(Node, DjangoObjectType):
    class Meta:
        model = ProductOption
        filterset_class = ProductOptionFilter
        interfaces = (graphene.Node)
        connection_class = ProductOptionConnection 

    
class ProductTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTaxRate
        filterset_class = ProductTaxRateFilter
        interfaces = (graphene.Node)
        connection_class = ProductTaxRateConnection 

    
class ProductTypeTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ProductTypeTaxRate
        filterset_class = ProductTypeTaxRateFilter
        interfaces = (graphene.Node)
        connection_class = ProductTypeTaxRateConnection 

    
class ProductVariantInventoryItemNode(Node, DjangoObjectType):
    class Meta:
        model = ProductVariantInventoryItem
        filterset_class = ProductVariantInventoryItemFilter
        interfaces = (graphene.Node)
        connection_class = ProductVariantInventoryItemConnection 

    
class ProductVariantNode(Node, DjangoObjectType):
    class Meta:
        model = ProductVariant
        filterset_class = ProductVariantFilter
        interfaces = (graphene.Node)
        connection_class = ProductVariantConnection 

    
class PublishableApiKeySalesChannelNode(Node, DjangoObjectType):
    class Meta:
        model = PublishableApiKeySalesChannel
        filterset_class = PublishableApiKeySalesChannelFilter
        interfaces = (graphene.Node)
        connection_class = PublishableApiKeySalesChannelConnection 

    
class PublishableApiKeyNode(Node, DjangoObjectType):
    class Meta:
        model = PublishableApiKey
        filterset_class = PublishableApiKeyFilter
        interfaces = (graphene.Node)
        connection_class = PublishableApiKeyConnection 

    
class RefundNode(Node, DjangoObjectType):
    class Meta:
        model = Refund
        filterset_class = RefundFilter
        interfaces = (graphene.Node)
        connection_class = RefundConnection 

    
class RegionNode(Node, DjangoObjectType):
    class Meta:
        model = Region
        filterset_class = RegionFilter
        interfaces = (graphene.Node)
        connection_class = RegionConnection 

    
class ReturnItemNode(Node, DjangoObjectType):
    class Meta:
        model = ReturnItem
        filterset_class = ReturnItemFilter
        interfaces = (graphene.Node)
        connection_class = ReturnItemConnection 

    
class ReturnReasonNode(Node, DjangoObjectType):
    class Meta:
        model = ReturnReason
        filterset_class = ReturnReasonFilter
        interfaces = (graphene.Node)
        connection_class = ReturnReasonConnection 

    
class ReturnStatusNode(Node, DjangoObjectType):
    class Meta:
        model = ReturnStatus
        filterset_class = ReturnStatusFilter
        interfaces = (graphene.Node)
        connection_class = ReturnStatusConnection 

    
class SalesChannelLocationNode(Node, DjangoObjectType):
    class Meta:
        model = SalesChannelLocation
        filterset_class = SalesChannelLocationFilter
        interfaces = (graphene.Node)
        connection_class = SalesChannelLocationConnection 

    
class ShippingMethodTaxLineNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingMethodTaxLine
        filterset_class = ShippingMethodTaxLineFilter
        interfaces = (graphene.Node)
        connection_class = ShippingMethodTaxLineConnection 

    
class ShippingOptionRequirementNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingOptionRequirement
        filterset_class = ShippingOptionRequirementFilter
        interfaces = (graphene.Node)
        connection_class = ShippingOptionRequirementConnection 

    
class ShippingProfileTypeNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingProfileType
        filterset_class = ShippingProfileTypeFilter
        interfaces = (graphene.Node)
        connection_class = ShippingProfileTypeConnection 

    
class ShippingProfileNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingProfile
        filterset_class = ShippingProfileFilter
        interfaces = (graphene.Node)
        connection_class = ShippingProfileConnection 

    
class TaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = TaxRate
        filterset_class = TaxRateFilter
        interfaces = (graphene.Node)
        connection_class = TaxRateConnection 

    
class ShippingTaxRateNode(Node, DjangoObjectType):
    class Meta:
        model = ShippingTaxRate
        filterset_class = ShippingTaxRateFilter
        interfaces = (graphene.Node)
        connection_class = ShippingTaxRateConnection 

    
class StagedJobNode(Node, DjangoObjectType):
    class Meta:
        model = StagedJob
        filterset_class = StagedJobFilter
        interfaces = (graphene.Node)
        connection_class = StagedJobConnection 

    
class StoreNode(Node, DjangoObjectType):
    class Meta:
        model = Store
        filterset_class = StoreFilter
        interfaces = (graphene.Node)
        connection_class = StoreConnection 

    
class SwapNode(Node, DjangoObjectType):
    class Meta:
        model = Swap
        filterset_class = SwapFilter
        interfaces = (graphene.Node)
        connection_class = SwapConnection 

    
class TaxProviderNode(Node, DjangoObjectType):
    class Meta:
        model = TaxProvider
        filterset_class = TaxProviderFilter
        interfaces = (graphene.Node)
        connection_class = TaxProviderConnection 

    
class TrackingLinkNode(Node, DjangoObjectType):
    class Meta:
        model = TrackingLink
        filterset_class = TrackingLinkFilter
        interfaces = (graphene.Node)
        connection_class = TrackingLinkConnection 

    