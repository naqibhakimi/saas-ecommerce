import graphene
from graphene_django.fields import DjangoConnectionField

from .types import (
    OrderDiscountNode,
    OrderGiftCardNode,
    OrderNode,
    CustomerNode,
    CountryNode,
    AddressNode,
    AnalyticsConfigNode,
    BatchJobStatusNode,
    BatchJobNode,
    DiscountNode,
    GiftCardNode,
    LineItemNode,
    PaymentNode,
    PaymentSessionNode,
    ShippingMethodNode,
    SalesChannelNode,
    CartNode,
    ClaimTagNode,
    ClaimItemNode,
    ClaimImageNode,
    ClaimOrderNode,
    ReturnNode,
    FulfillmentNode,
    CurrencyNode,
    ShippingOptionNode,
    CustomShippingOptionNode,
    PriceListNode,
    CustomerGroupNode,
    DiscountConditionCustomerGroupNode,
    DiscountConditionProductCollectionNode,
    DiscountConditionProductTagNode,
    ProductTypeNode,
    DiscountConditionProductTypeNode,
    ProductTagNode,
    ProductNode,
    DiscountConditionProductNode,
    DiscountConditionNode,
    DiscountRuleNode,
    DraftOrderNode,
    FulfillmentItemNode,
    FulfillmentProviderNode,
    GiftCardTransactionNode,
    IdempotencyKeyNode,
    ImageNode,
    InviteNode,
    LineItemAdjustmentNode,
    TaxLineNode,
    LineItemTaxLineNode,
    MoneyAmountNode,
    NoteNode,
    NotificationProviderNode,
    NotificationNode,
    OauthNode,
    OrderEditNode,
    OrderItemChangeNode,
    PaymentCollectionStatusNode,
    PaymentCollectionTypeNode,
    PaymentCollectionNode,
    PaymentProviderNode,
    ProductCategoryNode,
    ProductCollectionNode,
    ProductOptionValueNode,
    ProductOptionNode,
    ProductTaxRateNode,
    ProductTypeTaxRateNode,
    ProductVariantInventoryItemNode,
    ProductVariantNode,
    PublishableApiKeySalesChannelNode,
    PublishableApiKeyNode,
    RefundNode,
    RegionNode,
    ReturnItemNode,
    ReturnReasonNode,
    ReturnStatusNode,
    SalesChannelLocationNode,
    ShippingMethodTaxLineNode,
    ShippingOptionRequirementNode,
    ShippingProfileTypeNode,
    ShippingProfileNode,
    TaxRateNode,
    ShippingTaxRateNode,
    StagedJobNode,
    StoreNode,
    SwapNode,
    TaxProviderNode,
    TrackingLinkNode,
)

class OrderDiscountQuery:
        order_discounts = DjangoConnectionField(OrderDiscountNode)
        order_discount = graphene.Field(OrderDiscountNode, id=graphene.ID())
        
class OrderGiftCardQuery:
        order_gift_cards = DjangoConnectionField(OrderGiftCardNode)
        order_gift_card = graphene.Field(OrderGiftCardNode, id=graphene.ID())
        
class OrderQuery:
        orders = DjangoConnectionField(OrderNode)
        order = graphene.Field(OrderNode, id=graphene.ID())
        
class CustomerQuery:
        customers = DjangoConnectionField(CustomerNode)
        customer = graphene.Field(CustomerNode, id=graphene.ID())
        
class CountryQuery:
        countrys = DjangoConnectionField(CountryNode)
        country = graphene.Field(CountryNode, id=graphene.ID())
        
class AddressQuery:
        addresss = DjangoConnectionField(AddressNode)
        address = graphene.Field(AddressNode, id=graphene.ID())
        
class AnalyticsConfigQuery:
        analytics_configs = DjangoConnectionField(AnalyticsConfigNode)
        analytics_config = graphene.Field(AnalyticsConfigNode, id=graphene.ID())
        
class BatchJobQuery:
        batch_jobs = DjangoConnectionField(BatchJobNode)
        batch_job = graphene.Field(BatchJobNode, id=graphene.ID())
        
class DiscountQuery:
        discounts = DjangoConnectionField(DiscountNode)
        discount = graphene.Field(DiscountNode, id=graphene.ID())
        
class GiftCardQuery:
        gift_cards = DjangoConnectionField(GiftCardNode)
        gift_card = graphene.Field(GiftCardNode, id=graphene.ID())
        
class LineItemQuery:
        line_items = DjangoConnectionField(LineItemNode)
        line_item = graphene.Field(LineItemNode, id=graphene.ID())
        
class PaymentQuery:
        payments = DjangoConnectionField(PaymentNode)
        payment = graphene.Field(PaymentNode, id=graphene.ID())
        
class PaymentSessionQuery:
        payment_sessions = DjangoConnectionField(PaymentSessionNode)
        payment_session = graphene.Field(PaymentSessionNode, id=graphene.ID())
        
class ShippingMethodQuery:
        shipping_methods = DjangoConnectionField(ShippingMethodNode)
        shipping_method = graphene.Field(ShippingMethodNode, id=graphene.ID())
        
class SalesChannelQuery:
        sales_channels = DjangoConnectionField(SalesChannelNode)
        sales_channel = graphene.Field(SalesChannelNode, id=graphene.ID())
        
class CartQuery:
        carts = DjangoConnectionField(CartNode)
        cart = graphene.Field(CartNode, id=graphene.ID())
        
class ClaimTagQuery:
        claim_tags = DjangoConnectionField(ClaimTagNode)
        claim_tag = graphene.Field(ClaimTagNode, id=graphene.ID())
        
class ClaimItemQuery:
        claim_items = DjangoConnectionField(ClaimItemNode)
        claim_item = graphene.Field(ClaimItemNode, id=graphene.ID())
        
class ClaimImageQuery:
        claim_images = DjangoConnectionField(ClaimImageNode)
        claim_image = graphene.Field(ClaimImageNode, id=graphene.ID())
        
class ClaimOrderQuery:
        claim_orders = DjangoConnectionField(ClaimOrderNode)
        claim_order = graphene.Field(ClaimOrderNode, id=graphene.ID())
        
class ReturnQuery:
        returns = DjangoConnectionField(ReturnNode)
        return = graphene.Field(ReturnNode, id=graphene.ID())
        
class FulfillmentQuery:
        fulfillments = DjangoConnectionField(FulfillmentNode)
        fulfillment = graphene.Field(FulfillmentNode, id=graphene.ID())
        
class CurrencyQuery:
        currencys = DjangoConnectionField(CurrencyNode)
        currency = graphene.Field(CurrencyNode, id=graphene.ID())
        
class ShippingOptionQuery:
        shipping_options = DjangoConnectionField(ShippingOptionNode)
        shipping_option = graphene.Field(ShippingOptionNode, id=graphene.ID())
        
class CustomShippingOptionQuery:
        custom_shipping_options = DjangoConnectionField(CustomShippingOptionNode)
        custom_shipping_option = graphene.Field(CustomShippingOptionNode, id=graphene.ID())
        
class PriceListQuery:
        price_lists = DjangoConnectionField(PriceListNode)
        price_list = graphene.Field(PriceListNode, id=graphene.ID())
        
class CustomerGroupQuery:
        customer_groups = DjangoConnectionField(CustomerGroupNode)
        customer_group = graphene.Field(CustomerGroupNode, id=graphene.ID())
        
class DiscountConditionCustomerGroupQuery:
        discount_condition_customer_groups = DjangoConnectionField(DiscountConditionCustomerGroupNode)
        discount_condition_customer_group = graphene.Field(DiscountConditionCustomerGroupNode, id=graphene.ID())
        
class DiscountConditionProductCollectionQuery:
        discount_condition_product_collections = DjangoConnectionField(DiscountConditionProductCollectionNode)
        discount_condition_product_collection = graphene.Field(DiscountConditionProductCollectionNode, id=graphene.ID())
        
class DiscountConditionProductTagQuery:
        discount_condition_product_tags = DjangoConnectionField(DiscountConditionProductTagNode)
        discount_condition_product_tag = graphene.Field(DiscountConditionProductTagNode, id=graphene.ID())
        
class ProductTypeQuery:
        product_types = DjangoConnectionField(ProductTypeNode)
        product_type = graphene.Field(ProductTypeNode, id=graphene.ID())
        
class DiscountConditionProductTypeQuery:
        discount_condition_product_types = DjangoConnectionField(DiscountConditionProductTypeNode)
        discount_condition_product_type = graphene.Field(DiscountConditionProductTypeNode, id=graphene.ID())
        
class ProductTagQuery:
        product_tags = DjangoConnectionField(ProductTagNode)
        product_tag = graphene.Field(ProductTagNode, id=graphene.ID())
        
class ProductQuery:
        products = DjangoConnectionField(ProductNode)
        product = graphene.Field(ProductNode, id=graphene.ID())
        
class DiscountConditionProductQuery:
        discount_condition_products = DjangoConnectionField(DiscountConditionProductNode)
        discount_condition_product = graphene.Field(DiscountConditionProductNode, id=graphene.ID())
        
class DiscountConditionQuery:
        discount_conditions = DjangoConnectionField(DiscountConditionNode)
        discount_condition = graphene.Field(DiscountConditionNode, id=graphene.ID())
        
class DiscountRuleQuery:
        discount_rules = DjangoConnectionField(DiscountRuleNode)
        discount_rule = graphene.Field(DiscountRuleNode, id=graphene.ID())
        
class DraftOrderQuery:
        draft_orders = DjangoConnectionField(DraftOrderNode)
        draft_order = graphene.Field(DraftOrderNode, id=graphene.ID())
        
class FulfillmentItemQuery:
        fulfillment_items = DjangoConnectionField(FulfillmentItemNode)
        fulfillment_item = graphene.Field(FulfillmentItemNode, id=graphene.ID())
        
class FulfillmentProviderQuery:
        fulfillment_providers = DjangoConnectionField(FulfillmentProviderNode)
        fulfillment_provider = graphene.Field(FulfillmentProviderNode, id=graphene.ID())
        
class GiftCardTransactionQuery:
        gift_card_transactions = DjangoConnectionField(GiftCardTransactionNode)
        gift_card_transaction = graphene.Field(GiftCardTransactionNode, id=graphene.ID())
        
class IdempotencyKeyQuery:
        idempotency_keys = DjangoConnectionField(IdempotencyKeyNode)
        idempotency_key = graphene.Field(IdempotencyKeyNode, id=graphene.ID())
        
class ImageQuery:
        images = DjangoConnectionField(ImageNode)
        image = graphene.Field(ImageNode, id=graphene.ID())
        
class InviteQuery:
        invites = DjangoConnectionField(InviteNode)
        invite = graphene.Field(InviteNode, id=graphene.ID())
        
class LineItemAdjustmentQuery:
        line_item_adjustments = DjangoConnectionField(LineItemAdjustmentNode)
        line_item_adjustment = graphene.Field(LineItemAdjustmentNode, id=graphene.ID())
        
class TaxLineQuery:
        tax_lines = DjangoConnectionField(TaxLineNode)
        tax_line = graphene.Field(TaxLineNode, id=graphene.ID())
        
class LineItemTaxLineQuery:
        line_item_tax_lines = DjangoConnectionField(LineItemTaxLineNode)
        line_item_tax_line = graphene.Field(LineItemTaxLineNode, id=graphene.ID())
        
class MoneyAmountQuery:
        money_amounts = DjangoConnectionField(MoneyAmountNode)
        money_amount = graphene.Field(MoneyAmountNode, id=graphene.ID())
        
class NoteQuery:
        notes = DjangoConnectionField(NoteNode)
        note = graphene.Field(NoteNode, id=graphene.ID())
        
class NotificationProviderQuery:
        notification_providers = DjangoConnectionField(NotificationProviderNode)
        notification_provider = graphene.Field(NotificationProviderNode, id=graphene.ID())
        
class NotificationQuery:
        notifications = DjangoConnectionField(NotificationNode)
        notification = graphene.Field(NotificationNode, id=graphene.ID())
        
class OauthQuery:
        oauths = DjangoConnectionField(OauthNode)
        oauth = graphene.Field(OauthNode, id=graphene.ID())
        
class OrderEditQuery:
        order_edits = DjangoConnectionField(OrderEditNode)
        order_edit = graphene.Field(OrderEditNode, id=graphene.ID())
        
class OrderItemChangeQuery:
        order_item_changes = DjangoConnectionField(OrderItemChangeNode)
        order_item_change = graphene.Field(OrderItemChangeNode, id=graphene.ID())
        
class PaymentCollectionQuery:
        payment_collections = DjangoConnectionField(PaymentCollectionNode)
        payment_collection = graphene.Field(PaymentCollectionNode, id=graphene.ID())
        
class PaymentProviderQuery:
        payment_providers = DjangoConnectionField(PaymentProviderNode)
        payment_provider = graphene.Field(PaymentProviderNode, id=graphene.ID())
        
class ProductCategoryQuery:
        product_categorys = DjangoConnectionField(ProductCategoryNode)
        product_category = graphene.Field(ProductCategoryNode, id=graphene.ID())
        
class ProductCollectionQuery:
        product_collections = DjangoConnectionField(ProductCollectionNode)
        product_collection = graphene.Field(ProductCollectionNode, id=graphene.ID())
        
class ProductOptionValueQuery:
        product_option_values = DjangoConnectionField(ProductOptionValueNode)
        product_option_value = graphene.Field(ProductOptionValueNode, id=graphene.ID())
        
class ProductOptionQuery:
        product_options = DjangoConnectionField(ProductOptionNode)
        product_option = graphene.Field(ProductOptionNode, id=graphene.ID())
        
class ProductTaxRateQuery:
        product_tax_rates = DjangoConnectionField(ProductTaxRateNode)
        product_tax_rate = graphene.Field(ProductTaxRateNode, id=graphene.ID())
        
class ProductTypeTaxRateQuery:
        product_type_tax_rates = DjangoConnectionField(ProductTypeTaxRateNode)
        product_type_tax_rate = graphene.Field(ProductTypeTaxRateNode, id=graphene.ID())
        
class ProductVariantInventoryItemQuery:
        product_variant_inventory_items = DjangoConnectionField(ProductVariantInventoryItemNode)
        product_variant_inventory_item = graphene.Field(ProductVariantInventoryItemNode, id=graphene.ID())
        
class ProductVariantQuery:
        product_variants = DjangoConnectionField(ProductVariantNode)
        product_variant = graphene.Field(ProductVariantNode, id=graphene.ID())
        
class PublishableApiKeySalesChannelQuery:
        publishable_api_key_sales_channels = DjangoConnectionField(PublishableApiKeySalesChannelNode)
        publishable_api_key_sales_channel = graphene.Field(PublishableApiKeySalesChannelNode, id=graphene.ID())
        
class PublishableApiKeyQuery:
        publishable_api_keys = DjangoConnectionField(PublishableApiKeyNode)
        publishable_api_key = graphene.Field(PublishableApiKeyNode, id=graphene.ID())
        
class RefundQuery:
        refunds = DjangoConnectionField(RefundNode)
        refund = graphene.Field(RefundNode, id=graphene.ID())
        
class RegionQuery:
        regions = DjangoConnectionField(RegionNode)
        region = graphene.Field(RegionNode, id=graphene.ID())
        
class ReturnItemQuery:
        return_items = DjangoConnectionField(ReturnItemNode)
        return_item = graphene.Field(ReturnItemNode, id=graphene.ID())
        
class ReturnReasonQuery:
        return_reasons = DjangoConnectionField(ReturnReasonNode)
        return_reason = graphene.Field(ReturnReasonNode, id=graphene.ID())
        
class SalesChannelLocationQuery:
        sales_channel_locations = DjangoConnectionField(SalesChannelLocationNode)
        sales_channel_location = graphene.Field(SalesChannelLocationNode, id=graphene.ID())
        
class ShippingMethodTaxLineQuery:
        shipping_method_tax_lines = DjangoConnectionField(ShippingMethodTaxLineNode)
        shipping_method_tax_line = graphene.Field(ShippingMethodTaxLineNode, id=graphene.ID())
        
class ShippingOptionRequirementQuery:
        shipping_option_requirements = DjangoConnectionField(ShippingOptionRequirementNode)
        shipping_option_requirement = graphene.Field(ShippingOptionRequirementNode, id=graphene.ID())
        
class ShippingProfileQuery:
        shipping_profiles = DjangoConnectionField(ShippingProfileNode)
        shipping_profile = graphene.Field(ShippingProfileNode, id=graphene.ID())
        
class TaxRateQuery:
        tax_rates = DjangoConnectionField(TaxRateNode)
        tax_rate = graphene.Field(TaxRateNode, id=graphene.ID())
        
class ShippingTaxRateQuery:
        shipping_tax_rates = DjangoConnectionField(ShippingTaxRateNode)
        shipping_tax_rate = graphene.Field(ShippingTaxRateNode, id=graphene.ID())
        
class StagedJobQuery:
        staged_jobs = DjangoConnectionField(StagedJobNode)
        staged_job = graphene.Field(StagedJobNode, id=graphene.ID())
        
class StoreQuery:
        stores = DjangoConnectionField(StoreNode)
        store = graphene.Field(StoreNode, id=graphene.ID())
        
class SwapQuery:
        swaps = DjangoConnectionField(SwapNode)
        swap = graphene.Field(SwapNode, id=graphene.ID())
        
class TaxProviderQuery:
        tax_providers = DjangoConnectionField(TaxProviderNode)
        tax_provider = graphene.Field(TaxProviderNode, id=graphene.ID())
        
class TrackingLinkQuery:
        tracking_links = DjangoConnectionField(TrackingLinkNode)
        tracking_link = graphene.Field(TrackingLinkNode, id=graphene.ID())