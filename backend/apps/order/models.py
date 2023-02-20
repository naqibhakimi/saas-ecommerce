from django.db import models
from apps.core.models import BaseModel
from apps.core.models import BaseModel
from apps.invoice.models import LineItem
from apps.inventory.models import Fulfillment
from apps.discount.models import Discount
from apps.giftcard.models import GiftCard
from apps.store.models import Cart, SalesChannel, Swap
from apps.product.models import ProductVariant


# Create your models here.
class OrderDiscount(BaseModel):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name="+")
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="+")


class OrderGiftCard(BaseModel):
    gift_card = models.ForeignKey(GiftCard, on_delete=models.CASCADE, related_name="+")
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="+")


class Order(BaseModel):
    Order_Status = (
        ("pending", "PENDING"),
        ("completed", "COMPLETED"),
        ("archived", "ARCHIVED"),
        ("canceled", "CANCELED"),
        ("requires_action", "REQUIRES_ACTION"),
    )

    Fulfillment_Status = (
        ("not_fulfilled", "NOT_FULFILLED"),
        ("partially_fulfilled", "PARTIALLY_FULFILLED"),
        ("fulfilled", "FULFILLED"),
        ("partially_shipped", "PARTIALLY_SHIPPED"),
        ("shipped", "SHIPPED"),
        ("partially_returned", "PARTIALLY_RETURNED"),
        ("returned", "RETURNED"),
        ("canceled", "CANCELED"),
        ("requires_action", "REQUIRES_ACTION"),
    )

    Payment_Status = (
        ("not_paid", "NOT PAID"),
        ("awaiting", "AWAITING"),
        ("captured", "CAPTURED"),
        ("partially_refunded", "PARTIALLY REFUNDED"),
        ("refunded", "REFUNDED"),
        ("canceled", "CANCELED"),
        ("requires_action", "REQUIRES ACTION"),
    )
    status = models.CharField(
        max_length=20,
        choices=Order_Status,
        default="Not PAID",
    )
    fulfillment_status = models.CharField(
        max_length=20, choices=Fulfillment_Status, default="NOT_FULFILLED"
    )
    payment_status = models.CharField(
        max_length=20, choices=Payment_Status, default="NOT PAID"
    )
    # display_id = models.AutoField(primary_key=True)
    cart = models.OneToOneField(
        Cart, on_delete=models.CASCADE, null=True, related_name="+"
    )
    customer = models.ForeignKey(
        "customer.Customer", on_delete=models.CASCADE, related_name="+"
    )
    email = models.EmailField()
    billing_address = models.ForeignKey(
        "customer.Address", on_delete=models.CASCADE, related_name="+", null=True
    )
    shipping_address = models.ForeignKey(
        "customer.Address", on_delete=models.CASCADE, related_name="+", null=True
    )
    region = models.ForeignKey(
        "customer.Region", on_delete=models.CASCADE, related_name="+"
    )
    order_number = models.CharField(max_length=255, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    subtotal_price = models.DecimalField(max_digits=20, decimal_places=2)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)

    # currency_code = models.CharField(max_length=10)
    currency = models.ForeignKey(
        "payment.Currency", on_delete=models.CASCADE, related_name="+"
    )
    tax_rate = models.FloatField(null=True)
    discounts = models.ManyToManyField(
        Discount, through="OrderDiscount", related_name="+"
    )
    gift_cards = models.ManyToManyField(
        GiftCard, through="OrderGiftCard", related_name="+"
    )
    draft_order = models.OneToOneField(
        "DraftOrder", on_delete=models.CASCADE, related_name="+", null=True
    )
    canceled_at = models.DateField(null=True)
    metadata = models.JSONField(null=True)
    no_notification = models.BooleanField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    sales_channel = models.ForeignKey(
        SalesChannel, on_delete=models.CASCADE, related_name="+", null=True, blank=True
    )

    # Total fields
    shipping_total = models.IntegerField()
    discount_total = models.FloatField()
    tax_total = models.FloatField(null=True)
    refunded_total = models.FloatField()
    total = models.FloatField()
    sub_total = models.FloatField()
    paid_total = models.FloatField()
    refundable_amount = models.FloatField()
    gift_card_total = models.FloatField()
    gift_card_tax_total = models.FloatField()


class OrderEdit(BaseModel):
    Order_Edit_Status = (
        ("confirmed", "CONFIRMED"),
        ("declined", "DECLINED"),
        ("requested", "REQUESTED"),
        ("created", "CREATED"),
        ("canceled", "CANCELED"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="+")
    changes = models.ManyToManyField("OrderItemChange", related_name="+")
    internal_note = models.TextField(null=True)
    created_by = models.CharField(max_length=255)
    requested_by = models.CharField(max_length=255, null=True)
    requested_at = models.DateTimeField(null=True)
    confirmed_by = models.CharField(max_length=255, null=True)
    confirmed_at = models.DateTimeField(null=True)
    declined_by = models.CharField(max_length=255, null=True)
    declined_reason = models.TextField(null=True)
    declined_at = models.DateTimeField(null=True)
    canceled_by = models.CharField(max_length=255, null=True)
    canceled_at = models.DateTimeField(null=True)
    items = models.ManyToManyField(LineItem, related_name="+")
    payment_collection = models.OneToOneField(
        "payment.PaymentCollection", on_delete=models.SET_NULL, null=True
    )
    shipping_total = models.IntegerField()
    discount_total = models.FloatField()
    tax_total = models.FloatField(null=True)
    total = models.FloatField()
    subtotal = models.FloatField()
    gift_card_total = models.FloatField()
    gift_card_tax_total = models.FloatField()
    difference_due = models.FloatField()
    status = models.CharField(
        choices=Order_Edit_Status, max_length=20, default="CREATED"
    )


class OrderItemChange(BaseModel):
    Order_Edit_Item_Change_Type = (
        ("item_add", "ITEM_ADD"),
        ("item_remove", "ITEM_REMOVE"),
        ("item_update", "ITEM_UPDATE"),
    )
    type = models.CharField(max_length=20, choices=Order_Edit_Item_Change_Type)
    order_edit = models.ForeignKey(
        OrderEdit, on_delete=models.CASCADE, related_name="+"
    )
    original_line_item = models.ForeignKey(
        LineItem,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    line_item = models.OneToOneField(
        LineItem,
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )


class DraftOrder(BaseModel):
    Draft_Order_Status = (
        ("open", "OPEN"),
        ("completed", "COMPLETED"),
    )
    status = models.CharField(max_length=10, choices=Draft_Order_Status, default="OPEN")
    cart = models.OneToOneField(
        Cart, on_delete=models.CASCADE, null=True, related_name="+"
    )
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    canceled_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    no_notification_order = models.BooleanField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)

    @property
    def display_id(self):
        return self.id


class ClaimOrder(BaseModel):
    Claim_Type = (
        ("refund", "REFUND"),
        ("replace", "REPLACE"),
    )
    Claim_Payment_Status = (
        ("na", "NA"),
        ("not_refunded", "NOT_REFUNDED"),
        ("refunded", "REFUNDED"),
    )

    ClaimFulfillmentStatus = (
        ("not_fulfilled", "NOT_FULFILLED"),
        ("partially_fulfilled", "PARTIALLY_FULFILLED"),
        ("fulfilled", "FULFILLED"),
        ("partially_shipped", "PARTIALLY_SHIPPED"),
        ("shipped", "SHIPPED"),
        ("partially_returned", "PARTIALLY_RETURNED"),
        ("returned", "RETURNED"),
        ("canceled", "CANCELED"),
        ("requires_action", "REQUIRES_ACTION"),
    )
    payment_status = models.CharField(
        max_length=20,
        choices=Claim_Payment_Status,
        default="na",
    )
    fulfillment_status = models.CharField(
        max_length=20,
        choices=Claim_Payment_Status,
        default="not_fulfilled",
    )
    claim_items = models.ManyToManyField(
        "ClaimItem",
        related_name="+",
    )
    additional_items = models.ManyToManyField(
        LineItem,
        related_name="+",
    )
    type = models.CharField(
        max_length=20,
        choices=Claim_Type,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="+",
    )
    return_order = models.OneToOneField(
        "order.Return",
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    shipping_address = models.ForeignKey(
        "customer.Address",
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )
    shipping_methods = models.ManyToManyField(
        "shipping.ShippingMethod",
        related_name="+",
    )
    fulfillments = models.ManyToManyField(
        Fulfillment,
        related_name="+",
    )
    refund_amount = models.IntegerField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    no_notification = models.BooleanField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    idempotency_key = models.CharField(max_length=255, null=True, blank=True)


class ClaimTag(BaseModel):
    value = models.CharField(max_length=255, unique=True)
    metadata = models.JSONField(null=True)


class ClaimItem(BaseModel):
    REASON_CHOICES = (
        ("missing_item", "Missing Item"),
        ("wrong_item", "Wrong Item"),
        ("production_failure", "Production Failure"),
        ("other", "Other"),
    )
    images = models.ManyToManyField("ClaimImage")
    claim_order = models.ForeignKey(
        ClaimOrder, related_name="+", on_delete=models.SET_NULL, null=True, blank=True
    )
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255, choices=REASON_CHOICES)
    note = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    tags = models.ManyToManyField(ClaimTag, related_name="+")
    metadata = models.JSONField(blank=True, null=True)


class ClaimImage(BaseModel):
    claim_item = models.ForeignKey(
        ClaimItem, on_delete=models.CASCADE, related_name="+"
    )
    url = models.CharField(max_length=255)
    metadata = models.JSONField(null=True, blank=True)


class Return(BaseModel):
    Return_Status = (
        ("requested", "REQUESTED"),
        ("received", "RECEIVED"),
        ("requires_action", "REQUIRES_ACTION"),
        ("canceled", "CANCELED"),
    )
    status = models.CharField(
        max_length=20,
        choices=Return_Status,
        default="REQUESTED",
    )
    # items = models.ManyToManyField(ReturnItem, related_name='+')
    swap = models.OneToOneField(
        Swap, on_delete=models.SET_NULL, related_name="+", null=True
    )
    claim_order = models.OneToOneField(
        ClaimOrder, on_delete=models.SET_NULL, related_name="+", null=True
    )
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, related_name="+", null=True
    )
    shipping_method = models.OneToOneField(
        "shipping.ShippingMethod", on_delete=models.CASCADE, related_name="+"
    )
    # location_id = models.CharField(max_length=100, null=True)
    shipping_data = models.JSONField(null=True)
    refund_amount = models.FloatField()
    received_at = models.DateTimeField(null=True)
    no_notification = models.BooleanField()
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=100, null=True)


class ReturnItem(BaseModel):
    return_order = models.ForeignKey(
        Return,
        on_delete=models.CASCADE,
        related_name="return_items",
        null=True,
        blank=True,
    )
    item = models.ForeignKey(
        LineItem,
        on_delete=models.CASCADE,
        related_name="return_items",
        null=True,
        blank=True,
    )
    quantity = models.IntegerField()
    is_requested = models.BooleanField(default=True)
    requested_quantity = models.IntegerField(null=True)
    received_quantity = models.IntegerField(null=True)
    reason = models.ForeignKey(
        "ReturnReason", on_delete=models.SET_NULL, related_name="+", null=True
    )
    note = models.TextField(null=True)
    metadata = models.JSONField(null=True)


class ReturnReason(BaseModel):
    value = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    parent_return_reason = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True
    )
    metadata = models.JSONField(blank=True, null=True)
