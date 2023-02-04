import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True

class OrderDiscountConnection(BaseConnection):
    class Meta:
        abstract = True


class OrderGiftCardConnection(BaseConnection):
    class Meta:
        abstract = True  


class OrderConnection(BaseConnection):
    class Meta:
        abstract = True  


class CustomerConnection(BaseConnection):
    class Meta:
        abstract = True  


class CountryConnection(BaseConnection):
    class Meta:
        abstract = True  


class AddressConnection(BaseConnection):
    class Meta:
        abstract = True  


class AnalyticsConfigConnection(BaseConnection):
    class Meta:
        abstract = True  


class BatchJobStatusConnection(BaseConnection):
    class Meta:
        abstract = True  


class BatchJobConnection(BaseConnection):
    class Meta:
        abstract = True  


class DiscountConnection(BaseConnection):
    class Meta:
        abstract = True  


class GiftCardConnection(BaseConnection):
    class Meta:
        abstract = True  


class LineItemConnection(BaseConnection):
    class Meta:
        abstract = True  


class PaymentConnection(BaseConnection):
    class Meta:
        abstract = True  


class PaymentSessionConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingMethodConnection(BaseConnection):
    class Meta:
        abstract = True  


class SalesChannelConnection(BaseConnection):
    class Meta:
        abstract = True  


class CartConnection(BaseConnection):
    class Meta:
        abstract = True  


class ClaimTagConnection(BaseConnection):
    class Meta:
        abstract = True  


class ClaimItemConnection(BaseConnection):
    class Meta:
        abstract = True  


class ClaimImageConnection(BaseConnection):
    class Meta:
        abstract = True  


class ClaimOrderConnection(BaseConnection):
    class Meta:
        abstract = True  


class ReturnConnection(BaseConnection):
    class Meta:
        abstract = True  


class FulfillmentConnection(BaseConnection):
    class Meta:
        abstract = True  


class CurrencyConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingOptionConnection(BaseConnection):
    class Meta:
        abstract = True  


class CustomShippingOptionConnection(BaseConnection):
    class Meta:
        abstract = True  


class PriceListConnection(BaseConnection):
    class Meta:
        abstract = True  


class CustomerGroupConnection(BaseConnection):
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


class ProductTypeConnection(BaseConnection):
    class Meta:
        abstract = True  


class DiscountConditionProductTypeConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductTagConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductConnection(BaseConnection):
    class Meta:
        abstract = True  


class DiscountConditionProductConnection(BaseConnection):
    class Meta:
        abstract = True  


class DiscountConditionConnection(BaseConnection):
    class Meta:
        abstract = True  


class DiscountRuleConnection(BaseConnection):
    class Meta:
        abstract = True  


class DraftOrderConnection(BaseConnection):
    class Meta:
        abstract = True  


class FulfillmentItemConnection(BaseConnection):
    class Meta:
        abstract = True  


class FulfillmentProviderConnection(BaseConnection):
    class Meta:
        abstract = True  


class GiftCardTransactionConnection(BaseConnection):
    class Meta:
        abstract = True  


class IdempotencyKeyConnection(BaseConnection):
    class Meta:
        abstract = True  


class ImageConnection(BaseConnection):
    class Meta:
        abstract = True  


class InviteConnection(BaseConnection):
    class Meta:
        abstract = True  


class LineItemAdjustmentConnection(BaseConnection):
    class Meta:
        abstract = True  


class TaxLineConnection(BaseConnection):
    class Meta:
        abstract = True  


class LineItemTaxLineConnection(BaseConnection):
    class Meta:
        abstract = True  


class MoneyAmountConnection(BaseConnection):
    class Meta:
        abstract = True  


class NoteConnection(BaseConnection):
    class Meta:
        abstract = True  


class NotificationProviderConnection(BaseConnection):
    class Meta:
        abstract = True  


class NotificationConnection(BaseConnection):
    class Meta:
        abstract = True  


class OauthConnection(BaseConnection):
    class Meta:
        abstract = True  


class OrderEditConnection(BaseConnection):
    class Meta:
        abstract = True  


class OrderItemChangeConnection(BaseConnection):
    class Meta:
        abstract = True  


class PaymentCollectionStatusConnection(BaseConnection):
    class Meta:
        abstract = True  


class PaymentCollectionTypeConnection(BaseConnection):
    class Meta:
        abstract = True  


class PaymentCollectionConnection(BaseConnection):
    class Meta:
        abstract = True  


class PaymentProviderConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductCategoryConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductCollectionConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductOptionValueConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductOptionConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductTaxRateConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductTypeTaxRateConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductVariantInventoryItemConnection(BaseConnection):
    class Meta:
        abstract = True  


class ProductVariantConnection(BaseConnection):
    class Meta:
        abstract = True  


class PublishableApiKeySalesChannelConnection(BaseConnection):
    class Meta:
        abstract = True  


class PublishableApiKeyConnection(BaseConnection):
    class Meta:
        abstract = True  


class RefundConnection(BaseConnection):
    class Meta:
        abstract = True  


class RegionConnection(BaseConnection):
    class Meta:
        abstract = True  


class ReturnItemConnection(BaseConnection):
    class Meta:
        abstract = True  


class ReturnReasonConnection(BaseConnection):
    class Meta:
        abstract = True  


class ReturnStatusConnection(BaseConnection):
    class Meta:
        abstract = True  


class SalesChannelLocationConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingMethodTaxLineConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingOptionRequirementConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingProfileTypeConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingProfileConnection(BaseConnection):
    class Meta:
        abstract = True  


class TaxRateConnection(BaseConnection):
    class Meta:
        abstract = True  


class ShippingTaxRateConnection(BaseConnection):
    class Meta:
        abstract = True  


class StagedJobConnection(BaseConnection):
    class Meta:
        abstract = True  


class StoreConnection(BaseConnection):
    class Meta:
        abstract = True  


class SwapConnection(BaseConnection):
    class Meta:
        abstract = True  


class TaxProviderConnection(BaseConnection):
    class Meta:
        abstract = True  


class TrackingLinkConnection(BaseConnection):
    class Meta:
        abstract = True  

