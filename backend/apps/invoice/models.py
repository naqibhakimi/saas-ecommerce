from django.db import models
from apps.core.models import BaseModel
from apps.discount.models import Discount
from apps.store.models import Cart, Swap
from apps.core.models import BaseModel
from apps.product.models import ProductVariant


class LineItem(BaseModel):
    cart = models.ForeignKey(
        Cart, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    order = models.ForeignKey(
        "order.Order", on_delete=models.SET_NULL, null=True, related_name="+"
    )
    swap = models.ForeignKey(
        Swap, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    claim_order = models.ForeignKey(
        "order.ClaimOrder", on_delete=models.SET_NULL, null=True, related_name="+"
    )
    original_item = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, related_name="+"
    )
    order_edit = models.ForeignKey(
        "order.OrderEdit", on_delete=models.SET_NULL, null=True, related_name="+"
    )
    variant = models.ForeignKey(
        ProductVariant, on_delete=models.SET_NULL, null=True, related_name="+"
    )
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    thumbnail = models.TextField(null=True)
    is_return = models.BooleanField(default=False)
    is_giftcard = models.BooleanField(default=False)
    should_merge = models.BooleanField(default=True)
    allow_discounts = models.BooleanField(default=True)
    has_shipping = models.BooleanField(null=True)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    fulfilled_quantity = models.PositiveIntegerField(null=True)
    returned_quantity = models.PositiveIntegerField(null=True)
    shipped_quantity = models.PositiveIntegerField(null=True)
    metadata = models.JSONField(null=True)
    includes_tax = models.BooleanField(default=False)
    refundable = models.PositiveIntegerField(null=True)
    subtotal = models.PositiveIntegerField(null=True)
    tax_total = models.PositiveIntegerField(null=True)
    total = models.PositiveIntegerField(null=True)
    original_total = models.PositiveIntegerField(null=True)
    original_tax_total = models.PositiveIntegerField(null=True)
    discount_total = models.PositiveIntegerField(null=True)
    gift_cart_total = models.PositiveIntegerField(null=True)


class LineItemAdjustment(BaseModel):
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE, related_name="+")
    discount = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    metadata = models.JSONField(null=True, blank=True)


class LineItemTaxLine(BaseModel):
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)
