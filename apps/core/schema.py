import asyncio
import datetime
import graphene
from asgiref.sync import async_to_sync


from channels.layers import get_channel_layer
channel_layer = get_channel_layer()

from apps.store.queries import (
    OrderDiscountQuery,
    OrderGiftCardQuery,
    OrderQuery,
    CustomerQuery,
    CountryQuery,
    AddressQuery,
    AnalyticsConfigQuery,
    BatchJobQuery,
    DiscountQuery,
    GiftCardQuery,
    LineItemQuery,
    PaymentQuery,
    PaymentSessionQuery,
    ShippingMethodQuery,
    SalesChannelQuery,
    CartQuery,
    ClaimTagQuery,
    ClaimItemQuery,
    ClaimImageQuery,
    ClaimOrderQuery,
    ReturnQuery,
    FulfillmentQuery,
    CurrencyQuery,
    ShippingOptionQuery,
    CustomShippingOptionQuery,
    PriceListQuery,
    CustomerGroupQuery,
    DiscountConditionCustomerGroupQuery,
    DiscountConditionProductCollectionQuery,
    DiscountConditionProductTagQuery,
    ProductTypeQuery,
    DiscountConditionProductTypeQuery,
    ProductTagQuery,
    ProductQuery,
    DiscountConditionProductQuery,
    DiscountConditionQuery,
    DiscountRuleQuery,
    DraftOrderQuery,
    FulfillmentItemQuery,
    FulfillmentProviderQuery,
    GiftCardTransactionQuery,
    IdempotencyKeyQuery,
    ImageQuery,
    InviteQuery,
    LineItemAdjustmentQuery,
    TaxLineQuery,
    LineItemTaxLineQuery,
    MoneyAmountQuery,
    NoteQuery,
    NotificationProviderQuery,
    NotificationQuery,
    OauthQuery,
    OrderEditQuery,
    OrderItemChangeQuery,
    PaymentCollectionQuery,
    PaymentProviderQuery,
    ProductCategoryQuery,
    ProductCollectionQuery,
    ProductOptionValueQuery,
    ProductOptionQuery,
    ProductTaxRateQuery,
    ProductTypeTaxRateQuery,
    ProductVariantInventoryItemQuery,
    ProductVariantQuery,
    PublishableApiKeySalesChannelQuery,
    PublishableApiKeyQuery,
    RefundQuery,
    RegionQuery,
    ReturnItemQuery,
    ReturnReasonQuery,
    SalesChannelLocationQuery,
    ShippingMethodTaxLineQuery,
    ShippingOptionRequirementQuery,
    ShippingProfileQuery,
    TaxRateQuery,
    ShippingTaxRateQuery,
    StagedJobQuery,
    StoreQuery,
    SwapQuery,
    TaxProviderQuery,
    TrackingLinkQuery,
)


class Query(
    OrderDiscountQuery,
    OrderGiftCardQuery,
    OrderQuery,
    CustomerQuery,
    CountryQuery,
    AddressQuery,
    AnalyticsConfigQuery,
    BatchJobQuery,
    DiscountQuery,
    GiftCardQuery,
    LineItemQuery,
    PaymentQuery,
    PaymentSessionQuery,
    ShippingMethodQuery,
    SalesChannelQuery,
    CartQuery,
    ClaimTagQuery,
    ClaimItemQuery,
    ClaimImageQuery,
    ClaimOrderQuery,
    ReturnQuery,
    FulfillmentQuery,
    CurrencyQuery,
    ShippingOptionQuery,
    CustomShippingOptionQuery,
    PriceListQuery,
    CustomerGroupQuery,
    DiscountConditionCustomerGroupQuery,
    DiscountConditionProductCollectionQuery,
    DiscountConditionProductTagQuery,
    ProductTypeQuery,
    DiscountConditionProductTypeQuery,
    ProductTagQuery,
    ProductQuery,
    DiscountConditionProductQuery,
    DiscountConditionQuery,
    DiscountRuleQuery,
    DraftOrderQuery,
    FulfillmentItemQuery,
    FulfillmentProviderQuery,
    GiftCardTransactionQuery,
    IdempotencyKeyQuery,
    ImageQuery,
    InviteQuery,
    LineItemAdjustmentQuery,
    TaxLineQuery,
    LineItemTaxLineQuery,
    MoneyAmountQuery,
    NoteQuery,
    NotificationProviderQuery,
    NotificationQuery,
    OauthQuery,
    OrderEditQuery,
    OrderItemChangeQuery,
    PaymentCollectionQuery,
    PaymentProviderQuery,
    ProductCategoryQuery,
    ProductCollectionQuery,
    ProductOptionValueQuery,
    ProductOptionQuery,
    ProductTaxRateQuery,
    ProductTypeTaxRateQuery,
    ProductVariantInventoryItemQuery,
    ProductVariantQuery,
    PublishableApiKeySalesChannelQuery,
    PublishableApiKeyQuery,
    RefundQuery,
    RegionQuery,
    ReturnItemQuery,
    ReturnReasonQuery,
    SalesChannelLocationQuery,
    ShippingMethodTaxLineQuery,
    ShippingOptionRequirementQuery,
    ShippingProfileQuery,
    TaxRateQuery,
    ShippingTaxRateQuery,
    StagedJobQuery,
    StoreQuery,
    SwapQuery,
    TaxProviderQuery,
    TrackingLinkQuery,
    graphene.ObjectType
    ):
    test = graphene.String(name=graphene.String())

    def resolve_test(root, info, name):
       async_to_sync(channel_layer.group_send)("new_message", {"data": name})

class Mutatation(graphene.ObjectType):
     test_object = graphene.String()

class Subscription(graphene.ObjectType):
    test = graphene.String()
    test1 = graphene.String()

    async def subscribe_test1(root, info):
        channel_name = await channel_layer.new_channel()
        await channel_layer.group_add("new_message", channel_name)
        try:
            while True:
                message = await channel_layer.receive(channel_name)
                yield message["data"]
        finally:
            await channel_layer.group_discard("new_message", channel_name)

    async def subscribe_test(root, info):
        while True:
            yield datetime.datetime.now().isoformat()
            await asyncio.sleep(1)

schema = graphene.Schema(query=Query, mutation=Mutatation, subscription=Subscription)