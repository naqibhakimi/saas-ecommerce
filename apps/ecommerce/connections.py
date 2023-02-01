import graphene


class BaseConnection(graphene.Connection):
    
    class Meta:
        abstract = True

class OrderDiscountConnection(BaseConnection):
    pass 


class OrderGiftCardConnection(BaseConnection):
    pass 


class OrderConnection(BaseConnection):
    pass 


class CustomerConnection(BaseConnection):
    pass 


class CountryConnection(BaseConnection):
    pass 


class AddressConnection(BaseConnection):
    pass 


class AnalyticsConfigConnection(BaseConnection):
    pass 


class BatchJobStatusConnection(BaseConnection):
    pass 


class BatchJobConnection(BaseConnection):
    pass 


class DiscountConnection(BaseConnection):
    pass 


class GiftCardConnection(BaseConnection):
    pass 


class LineItemConnection(BaseConnection):
    pass 


class PaymentConnection(BaseConnection):
    pass 


class PaymentSessionConnection(BaseConnection):
    pass 


class ShippingMethodConnection(BaseConnection):
    pass 


class SalesChannelConnection(BaseConnection):
    pass 


class CartConnection(BaseConnection):
    pass 


class ClaimTagConnection(BaseConnection):
    pass 


class ClaimItemConnection(BaseConnection):
    pass 


class ClaimImageConnection(BaseConnection):
    pass 


class ClaimOrderConnection(BaseConnection):
    pass 


class ReturnConnection(BaseConnection):
    pass 


class FulfillmentConnection(BaseConnection):
    pass 


class CurrencyConnection(BaseConnection):
    pass 


class ShippingOptionConnection(BaseConnection):
    pass 


class CustomShippingOptionConnection(BaseConnection):
    pass 


class PriceListConnection(BaseConnection):
    pass 


class CustomerGroupConnection(BaseConnection):
    pass 


class DiscountConditionCustomerGroupConnection(BaseConnection):
    pass 


class DiscountConditionProductCollectionConnection(BaseConnection):
    pass 


class DiscountConditionProductTagConnection(BaseConnection):
    pass 


class ProductTypeConnection(BaseConnection):
    pass 


class DiscountConditionProductTypeConnection(BaseConnection):
    pass 


class ProductTagConnection(BaseConnection):
    pass 


class ProductConnection(BaseConnection):
    pass 


class DiscountConditionProductConnection(BaseConnection):
    pass 


class DiscountConditionConnection(BaseConnection):
    pass 


class DiscountRuleConnection(BaseConnection):
    pass 


class DraftOrderConnection(BaseConnection):
    pass 


class FulfillmentItemConnection(BaseConnection):
    pass 


class FulfillmentProviderConnection(BaseConnection):
    pass 


class GiftCardTransactionConnection(BaseConnection):
    pass 


class IdempotencyKeyConnection(BaseConnection):
    pass 


class ImageConnection(BaseConnection):
    pass 


class InviteConnection(BaseConnection):
    pass 


class LineItemAdjustmentConnection(BaseConnection):
    pass 


class TaxLineConnection(BaseConnection):
    pass 


class LineItemTaxLineConnection(BaseConnection):
    pass 


class MoneyAmountConnection(BaseConnection):
    pass 


class NoteConnection(BaseConnection):
    pass 


class NotificationProviderConnection(BaseConnection):
    pass 


class NotificationConnection(BaseConnection):
    pass 


class OauthConnection(BaseConnection):
    pass 


class OrderEditConnection(BaseConnection):
    pass 


class OrderItemChangeConnection(BaseConnection):
    pass 


class PaymentCollectionStatusConnection(BaseConnection):
    pass 


class PaymentCollectionTypeConnection(BaseConnection):
    pass 


class PaymentCollectionConnection(BaseConnection):
    pass 


class PaymentProviderConnection(BaseConnection):
    pass 


class ProductCategoryConnection(BaseConnection):
    pass 


class ProductCollectionConnection(BaseConnection):
    pass 


class ProductOptionValueConnection(BaseConnection):
    pass 


class ProductOptionConnection(BaseConnection):
    pass 


class ProductTaxRateConnection(BaseConnection):
    pass 


class ProductTypeTaxRateConnection(BaseConnection):
    pass 


class ProductVariantInventoryItemConnection(BaseConnection):
    pass 


class ProductVariantConnection(BaseConnection):
    pass 


class PublishableApiKeySalesChannelConnection(BaseConnection):
    pass 


class PublishableApiKeyConnection(BaseConnection):
    pass 


class RefundConnection(BaseConnection):
    pass 


class RegionConnection(BaseConnection):
    pass 


class ReturnItemConnection(BaseConnection):
    pass 


class ReturnReasonConnection(BaseConnection):
    pass 


class ReturnStatusConnection(BaseConnection):
    pass 


class SalesChannelLocationConnection(BaseConnection):
    pass 


class ShippingMethodTaxLineConnection(BaseConnection):
    pass 


class ShippingOptionRequirementConnection(BaseConnection):
    pass 


class ShippingProfileTypeConnection(BaseConnection):
    pass 


class ShippingProfileConnection(BaseConnection):
    pass 


class TaxRateConnection(BaseConnection):
    pass 


class ShippingTaxRateConnection(BaseConnection):
    pass 


class StagedJobConnection(BaseConnection):
    pass 


class StoreConnection(BaseConnection):
    pass 


class SwapConnection(BaseConnection):
    pass 


class TaxProviderConnection(BaseConnection):
    pass 


class TrackingLinkConnection(BaseConnection):
    pass 

