from django.db import models
from django.conf import settings

from apps.core.models import BaseModel
from django.core.validators import EmailValidator

class OrderDiscount(BaseModel):
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, related_name="+")
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="+")

class OrderGiftCard(BaseModel):
    gift_card = models.ForeignKey('GiftCard', on_delete=models.CASCADE, related_name="+")
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="+")



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
        default= "Not PAID",
    )
    fulfillment_status = models.CharField(
        max_length=20,
        choices=Fulfillment_Status,
        default= "NOT_FULFILLED"
    )
    payment_status = models.CharField(
        max_length=20,
        choices=Payment_Status,
        default="NOT PAID"
    )
    # display_id = models.AutoField(primary_key=True)
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE, null=True,  related_name='+')
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE,  related_name='+')
    email = models.EmailField()
    billing_address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name='+', null=True)
    shipping_address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name='+', null=True)
    region = models.ForeignKey('Region', on_delete = models.CASCADE,  related_name='+')
    order_number = models.CharField(max_length=255, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    subtotal_price = models.DecimalField(max_digits=20, decimal_places=2)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)


    # currency_code = models.CharField(max_length=10)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE,  related_name='+')
    tax_rate = models.FloatField(null=True)
    discounts = models.ManyToManyField('Discount', through='OrderDiscount' ,  related_name='+')
    gift_cards = models.ManyToManyField('GiftCard', through='OrderGiftCard',  related_name='+')
    draft_order = models.OneToOneField('DraftOrder', on_delete=models.CASCADE, related_name='+', null=True)
    canceled_at = models.DateField(null=True)
    metadata = models.JSONField(null=True)
    no_notification = models.BooleanField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    sales_channel = models.ForeignKey('SalesChannel', on_delete=models.CASCADE, related_name='+', null=True, blank=True)

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


class Customer(BaseModel):
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    billing_address = models.OneToOneField(
        'Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    phone = models.CharField(max_length=255, blank=True, null=True)
    has_account = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    orders = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='+'
    )
    groups = models.ManyToManyField('CustomerGroup', related_name='+')
    metadata = models.JSONField(blank=True, null=True)




class Country(BaseModel):
    iso_2 = models.CharField(max_length=255, unique=True)
    iso_3 = models.CharField(max_length=255)
    num_code = models.IntegerField()
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    region = models.ForeignKey("Region", on_delete=models.SET_NULL, null=True, blank=True,  related_name='+')


class Address(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,  related_name='+')
    company = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='+')
    province = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField()
    
    
class AnalyticsConfig(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='+')
    opt_out = models.BooleanField(default=False)
    anonymize = models.BooleanField(default=False)


class BatchJobStatus:
    pass 
class BatchJob(BaseModel):
    type = models.CharField(max_length=255, null=True, blank=True )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='+')
    context = models.JSONField(null=True, blank=True)
    result = models.JSONField(null=True, blank = True)
    dry_run = models.BooleanField(default=False, blank = True)
    pre_processed_at = models.DateTimeField(null=True, blank = True)
    processing_at = models.DateTimeField(null=True, blank = True)
    confirmed_at = models.DateTimeField(null=True, blank = True)
    completed_at = models.DateTimeField(null=True, blank = True)
    canceled_at = models.DateTimeField(null=True, blank = True)
    failed_at = models.DateTimeField(null=True, blank = True)

    @property
    def status(self):
        if self.pre_processed_at:
            return BatchJobStatus.PRE_PROCESSED
        if self.confirmed_at:
            return BatchJobStatus.CONFIRMED
        if self.processing_at:
            return BatchJobStatus.PROCESSING
        if self.completed_at:
            return BatchJobStatus.COMPLETED
        if self.canceled_at:
            return BatchJobStatus.CANCELED
        if self.failed_at:
            return BatchJobStatus.FAILED
        return BatchJobStatus.CREATED


class Discount(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    is_dynamic = models.BooleanField()
    rule = models.ForeignKey("DiscountRule", on_delete=models.CASCADE, null=True, related_name='+')
    is_disabled = models.BooleanField()
    parent_discount = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    starts_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    valid_duration = models.CharField(max_length=255, null=True, blank=True)
    regions = models.ManyToManyField("Region", related_name='+')
    usage_limit = models.IntegerField(null=True, blank=True)
    usage_count = models.IntegerField(default=0)
    metadata = models.JSONField(null=True, blank=True)


class GiftCard(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    value = models.IntegerField()
    balance = models.IntegerField()
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)
    ends_at = models.DateTimeField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)


class LineItem(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, related_name='+')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='+')
    swap = models.ForeignKey('Swap', on_delete=models.SET_NULL, null=True, related_name='+')
    claim_order = models.ForeignKey('ClaimOrder', on_delete=models.SET_NULL, null=True, related_name='+')
    original_item = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='+')
    order_edit = models.ForeignKey('OrderEdit', on_delete=models.SET_NULL, null=True, related_name='+')
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, null=True, related_name='+')
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



class Payment(BaseModel):
    swap = models.OneToOneField("Swap", on_delete=models.SET_NULL, null=True,  related_name='+')
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, related_name='+', null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='+', null=True)
    amount = models.FloatField()
    # currency_code = models.CharField(max_length=3)
    currency = models.ForeignKey('Currency', on_delete=models.SET_NULL, related_name='+', null=True)
    amount_refunded = models.FloatField(default=0)
    provider_id = models.CharField(max_length=255)
    data = models.JSONField()
    captured_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)




class PaymentSession(BaseModel):
    Payment_Session_Status = (
        ("authorized", "AUTHORIZED"),
        ("pending", "PENDING"),
        ("requires_more", "REQUIRES_MORE"),
        ("error", "ERROR"),
        ("canceled", "CANCELED"),
    )
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='+', null=True)
    provider_id = models.CharField(max_length=100)
    is_selected = models.BooleanField(null=True)
    is_initiated = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=Payment_Session_Status)
    data = models.JSONField()
    idempotency_key = models.CharField(max_length=100, null=True)
    amount = models.FloatField(null=True)
    payment_authorized_at = models.DateTimeField(null=True)




class ShippingMethod(BaseModel):
    shipping_option = models.ForeignKey("ShippingOption", on_delete=models.CASCADE, related_name='+')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='+')
    claim_order = models.ForeignKey("ClaimOrder", on_delete=models.CASCADE, null=True, related_name='+')
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, null=True, related_name='+')
    swap = models.ForeignKey("Swap", on_delete=models.CASCADE, null=True, related_name='+')
    return_order = models.OneToOneField("Return", on_delete=models.CASCADE, related_name='+', null=True)
    # tax_lines = models.ManyToManyField("ShippingMethodTaxLine", related_name='+')
    price = models.PositiveIntegerField()
    data = models.JSONField()
    includes_tax = models.BooleanField(default=False)
    subtotal = models.PositiveIntegerField(null=True)
    total = models.PositiveIntegerField(null=True)
    tax_total = models.PositiveIntegerField(null=True)



class SalesChannel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)


class Cart(BaseModel):
    CART_TYPE_CHOICES = (
        ("default", "Default"),
        ("swap", "Swap"),
        ("draft_order", "Draft Order"),
        ("payment_link", "Payment Link"),
        ("claim", "Claim"),
    )
    email = models.EmailField(blank=True, null=True)
    billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    items = models.ManyToManyField(LineItem, blank=True, related_name='+')
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    discounts = models.ManyToManyField(Discount, blank=True, related_name='+')
    gift_cards = models.ManyToManyField(GiftCard, blank=True, related_name='+')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    payment_session = models.OneToOneField(PaymentSession, on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    shipping_methods = models.ManyToManyField(ShippingMethod, blank=True, related_name='+')
    type = models.CharField(max_length=20, choices=CART_TYPE_CHOICES, default='default')
    completed_at = models.DateTimeField(blank=True, null=True)
    payment_authorized_at = models.DateTimeField(blank=True, null=True)
    idempotency_key = models.CharField(max_length=255, blank=True, null=True)
    context = models.JSONField(blank=True, null=True)
    metadata = models.JSONField() # [FIXME] do we even need this ? 
    sales_channel = models.ForeignKey(SalesChannel, related_name='+', on_delete=models.SET_NULL, null=True)


class ClaimTag(BaseModel):
    value = models.CharField(max_length=255, unique=True)
    metadata = models.JSONField(null=True)



class ClaimItem(BaseModel):
    REASON_CHOICES = (
        ('missing_item', 'Missing Item'),
        ('wrong_item', 'Wrong Item'),
        ('production_failure', 'Production Failure'),
        ('other', 'Other'),
    )
    images = models.ManyToManyField('ClaimImage')
    claim_order = models.ForeignKey("ClaimOrder", related_name='+', on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    variant = models.ForeignKey("ProductVariant", on_delete=models.CASCADE)
    reason = models.CharField(max_length=255, choices=REASON_CHOICES)
    note = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    tags = models.ManyToManyField(ClaimTag, related_name='+')
    metadata = models.JSONField(blank=True, null=True)

class ClaimImage(BaseModel):
    claim_item = models.ForeignKey(ClaimItem, on_delete=models.CASCADE, related_name='+')
    url = models.CharField(max_length=255)
    metadata = models.JSONField(null=True, blank=True)


class ClaimOrder(BaseModel):
    Claim_Type = (
            ('refund', 'REFUND'),
            ('replace', 'REPLACE'),
        )
    Claim_Payment_Status = (
            ('na', 'NA'),
            ('not_refunded', 'NOT_REFUNDED'),
            ('refunded', 'REFUNDED'),
        )
    
    ClaimFulfillmentStatus = (
            ('not_fulfilled', 'NOT_FULFILLED'),
            ('partially_fulfilled', 'PARTIALLY_FULFILLED'),
            ('fulfilled', 'FULFILLED'),
            ('partially_shipped', 'PARTIALLY_SHIPPED'),
            ('shipped', 'SHIPPED'),
            ('partially_returned', 'PARTIALLY_RETURNED'),
            ('returned', 'RETURNED'),
            ('canceled', 'CANCELED'),
            ('requires_action', 'REQUIRES_ACTION'),
        )
    payment_status = models.CharField(
        max_length=20,
        choices=Claim_Payment_Status,
        default='na',
    )
    fulfillment_status = models.CharField(
        max_length=20,
        choices=Claim_Payment_Status,
        default='not_fulfilled',
    )
    claim_items = models.ManyToManyField(
        ClaimItem,
        related_name='+',
    )
    additional_items = models.ManyToManyField(
        LineItem,
        related_name='+',
    )
    type = models.CharField(
        max_length=20,
        choices=Claim_Type,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='+',
    )
    return_order = models.OneToOneField(
        'Return',
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True,
    )
    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='+',
        null=True,
        blank=True,
    )
    shipping_methods = models.ManyToManyField(
        ShippingMethod,
        related_name='+',
    )
    fulfillments = models.ManyToManyField(
        'Fulfillment',
        related_name='+',
    )
    refund_amount = models.IntegerField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    no_notification = models.BooleanField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    idempotency_key = models.CharField(max_length=255, null=True, blank=True)



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
    swap = models.OneToOneField("Swap", on_delete=models.SET_NULL, related_name='+', null=True)
    claim_order = models.OneToOneField(ClaimOrder, on_delete=models.SET_NULL, related_name='+', null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='+', null=True)
    shipping_method = models.OneToOneField(ShippingMethod, on_delete=models.CASCADE, related_name='+')
    # location_id = models.CharField(max_length=100, null=True)
    shipping_data = models.JSONField(null=True)
    refund_amount = models.FloatField()
    received_at = models.DateTimeField(null=True)
    no_notification = models.BooleanField()
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=100, null=True)




class Fulfillment(BaseModel):
    claim_order = models.ForeignKey(ClaimOrder, on_delete=models.CASCADE, null=True, related_name='+')
    swap = models.ForeignKey("Swap", on_delete=models.CASCADE, null=True, related_name='+')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='+')
    no_notification = models.BooleanField(null=True)
    provider = models.ForeignKey("FulfillmentProvider", on_delete=models.CASCADE)
    location_id = models.CharField(max_length=255, null=True)
    # items = models.OneToManyField("FulfillmentItem", on_delete=models.CASCADE, related_name='+')
    # tracking_links = models.OneToManyField("TrackingLink", on_delete=models.CASCADE, related_name='+')
    tracking_numbers = models.JSONField(default=dict)
    data = models.JSONField()
    shipped_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)



class Currency(BaseModel):
    code = models.CharField(unique=True, max_length=255)
    symbol = models.CharField(max_length=255)
    symbol_native = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    includes_tax = models.BooleanField(default=False)


class ShippingOption(BaseModel):
    Shipping_Option_Price_Type = (
        ("flat_rate", "FLAT_RATE"),
        ("calculated", "CALCULATED")
    )
    name = models.CharField(max_length=255)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    profile = models.ForeignKey("ShippingProfile", on_delete=models.CASCADE, related_name='+')
    provider = models.ForeignKey("FulfillmentProvider", on_delete=models.CASCADE, related_name='+')
    price_type = models.CharField(max_length=20, choices=Shipping_Option_Price_Type, default="FLAT_RATE")
    amount = models.PositiveIntegerField(null=True)
    is_return = models.BooleanField(default=False)
    admin_only = models.BooleanField(default=False)
    # requirements = models.ManyToManyField("ShippingOptionRequirement", through="ShippingOptionRequirement")
    data = models.JSONField()
    metadata = models.JSONField(null=True)
    includes_tax = models.BooleanField(default=False)


class CustomShippingOption(BaseModel):
    price = models.IntegerField()
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (('shipping_option', 'cart'),)


class PriceList(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, default="sale")
    status = models.CharField(max_length=255, default="draft")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    customer_groups = models.ManyToManyField('CustomerGroup', related_name='+')
    # prices = models.OneToManyField('MoneyAmount', related_name='+', on_delete=models.CASCADE)
    includes_tax = models.BooleanField(default=False)

class CustomerGroup(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    customers = models.ManyToManyField(Customer, related_name='+')
    price_lists = models.ManyToManyField(PriceList)
    metadata = models.JSONField(null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class DiscountConditionCustomerGroup(BaseModel):
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(null=True, blank=True)




class DiscountConditionProductCollection(BaseModel):
    product_collection = models.ForeignKey("ProductCollection", on_delete=models.CASCADE)
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE)
    metadata = models.JSONField(null=True)


class DiscountConditionProductTag(BaseModel):
    product_tag = models.ForeignKey('ProductTag', on_delete=models.CASCADE)
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE, related_name='+' )
    metadata = models.JSONField(null=True, blank=True)


class ProductType(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(blank=True, null=True)


class DiscountConditionProductType(BaseModel):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='+')
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product_type", "discount_condition"),)
class ProductTag(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)


class Product(BaseModel):
    Product_Status = (
        ('draft', 'DRAFT'),
        ('proposed', 'PROPOSED'),
        ('published', 'PUBLISHED'),
        ('rejected', 'REJECTED')
    )
    title = models.CharField(max_length=255)
    subtitle = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    handle = models.TextField(null=True, blank=True, unique=True)
    is_gift_card = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=Product_Status, default='draft')
    images = models.ManyToManyField("Image", related_name='+')
    thumbnail = models.TextField(null=True, blank=True)
    profile = models.ForeignKey('ShippingProfile', on_delete=models.CASCADE, related_name='+')
    weight = models.PositiveIntegerField(null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    hs_code = models.TextField(null=True, blank=True)
    origin_country = models.TextField(null=True, blank=True)
    mid_code = models.TextField(null=True, blank=True)
    material = models.TextField(null=True, blank=True)
    collection = models.ForeignKey("ProductCollection", on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    tags = models.ManyToManyField(ProductTag, related_name='+')
    discountable = models.BooleanField(default=True)
    external_id = models.TextField(null=True, blank=True)
    sales_channels = models.ManyToManyField(SalesChannel, related_name='+')
    # deleted_at = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)



class DiscountConditionProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product", "discount_condition"),)



class DiscountCondition(BaseModel):
    Discount_Condition_Type = (
        ("products", "PRODUCTS"),
        ("product_types", "PRODUCT_TYPES"),
        ("product_collections", "PRODUCT_COLLECTIONS"),
        ("product_tags", "PRODUCT_TAGS"),
        ("customer_groups", "CUSTOMER_GROUPS")
    )

    Discount_Condition_Operator = (
        ("in", "IN"),
        ("not_in", "NOT_IN"),
    )
    type = models.CharField(
        max_length=20,
        choices=Discount_Condition_Type
        )
    operator = models.CharField(
        max_length=20,
        choices=Discount_Condition_Operator
        )
    discount_rule = models.ForeignKey(
        'DiscountRule',
        on_delete=models.CASCADE,
        related_name='+'
        )
    products = models.ManyToManyField(
        Product,
        through='DiscountConditionProduct',
        )
    product_types = models.ManyToManyField(
        ProductType,
        through='DiscountConditionProductType',
        )
    product_tags = models.ManyToManyField(
        ProductTag,
        through='DiscountConditionProductTag',
        )
    product_collections = models.ManyToManyField(
        "ProductCollection",
        through='DiscountConditionProductCollection',
        )
    customer_groups = models.ManyToManyField(
        CustomerGroup,
        through='DiscountConditionCustomerGroup',
        )
    metadata = models.JSONField(null=True)


class DiscountRule(BaseModel):
    Discount_Rule_Type = (
        ("fixed", "FIXED"),
        ("percentage", "PERCENTAGE"),
        ("free_shipping", "FREE_SHIPPING"),
    )

    Allocation_Type = (
        ("total", "TOTAL"),
        ("item", "ITEM"),
    )
    description = models.CharField(max_length=255, null=True)
    type = models.CharField(choices=Discount_Rule_Type, max_length=20)
    value = models.FloatField()
    allocation = models.CharField(choices=Allocation_Type, max_length=20, null=True)
    conditions = models.ManyToManyField('DiscountCondition', related_name='+')
    metadata = models.JSONField(null=True)


class DraftOrder(BaseModel):
    Draft_Order_Status = (
        ("open", "OPEN"),
        ("completed", "COMPLETED"),
    )
    status = models.CharField(max_length=10,choices=Draft_Order_Status, default="OPEN")
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, related_name='+')
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    canceled_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    no_notification_order = models.BooleanField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)

    @property
    def display_id(self):
        return self.id


class FulfillmentItem(BaseModel):
    fulfillment = models.ForeignKey(Fulfillment, on_delete=models.CASCADE)
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class FulfillmentProvider(BaseModel):
    is_installed = models.BooleanField(default=True)


class GiftCardTransaction(BaseModel):
    gift_card = models.ForeignKey(GiftCard, on_delete=models.CASCADE, related_name='+')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
    amount = models.IntegerField()
    is_taxable = models.BooleanField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ("gift_card_id", "order_id")


class IdempotencyKey(BaseModel):
    idempotency_key = models.CharField(unique=True, max_length=255)
    locked_at = models.DateTimeField(null=True, blank=True)
    request_method = models.CharField(max_length=255, null=True, blank=True)
    request_params = models.JSONField(null=True, blank=True)
    request_path = models.CharField(max_length=255, null=True, blank=True)
    response_code = models.IntegerField(null=True, blank=True)
    response_body = models.JSONField(null=True, blank=True)
    recovery_point = models.CharField(default="started", max_length=255)


class Image(BaseModel):
    url = models.CharField(max_length=255,null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Invite(BaseModel):
    User_Roles = (
        ("admin", "ADMIN"),
        ("member", "MEMBER"),
        ("developer", "DEVELOPER"),
    )
    user_email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=User_Roles)
    accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=255)
    expires_at = models.DateTimeField()
    metadata = models.JSONField(null=True)
    deleted_at = models.DateTimeField(null=True)


class LineItemAdjustment(BaseModel):
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE, related_name='+')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    metadata = models.JSONField(null=True, blank=True)


class TaxLine(BaseModel):
    rate = models.FloatField()
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)




class LineItemTaxLine(BaseModel):
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)


class MoneyAmount(BaseModel):
    # do we need this ? 
    # currency_code = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='+')
    amount = models.FloatField()
    min_quantity = models.IntegerField(null=True)
    max_quantity = models.IntegerField(null=True)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, null=True, related_name='+')
    variant = models.ForeignKey("ProductVariant", on_delete=models.CASCADE, related_name='+')
    region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True, related_name='+')


class Note(BaseModel):
    value = models.TextField()
    resource_type = models.CharField(max_length=255, null=True, blank=True)
    resource_id = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    metadata = models.JSONField(null=True)



class NotificationProvider(BaseModel):
    is_installed = models.BooleanField(default=True)



class Notification(BaseModel):
    event_name = models.CharField(max_length=255, null=True)
    resource_type = models.CharField(max_length=255)
    resource_id = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='+')
    to = models.CharField(max_length=255)
    data = models.JSONField()
    parent_notification = models.ForeignKey('self', on_delete=models.CASCADE, related_name='+', null=True)
    provider = models.ForeignKey(NotificationProvider, on_delete=models.CASCADE, related_name='+')
    


class Oauth(BaseModel):
    display_name = models.CharField(max_length=255)
    application_name = models.CharField(max_length=255, unique=True)
    install_url = models.CharField(max_length=255, null=True)
    uninstall_url = models.CharField(max_length=255, null=True)
    data = models.JSONField(null=True)
    

class OrderEdit(BaseModel):
    Order_Edit_Status = (
        ("confirmed", "CONFIRMED"),
        ("declined", "DECLINED"),
        ("requested", "REQUESTED"),
        ("created", "CREATED"),
        ("canceled", "CANCELED"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
    changes = models.ManyToManyField("OrderItemChange", related_name='+')
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
    items = models.ManyToManyField(LineItem, related_name='+')
    payment_collection = models.OneToOneField("PaymentCollection", on_delete=models.SET_NULL, null=True)
    shipping_total = models.IntegerField()
    discount_total = models.FloatField()
    tax_total = models.FloatField(null=True)
    total = models.FloatField()
    subtotal = models.FloatField()
    gift_card_total = models.FloatField()
    gift_card_tax_total = models.FloatField()
    difference_due = models.FloatField()
    status = models.CharField(choices=Order_Edit_Status, max_length=20, default="CREATED")


class OrderItemChange(BaseModel):
    Order_Edit_Item_Change_Type = (
        ("item_add", "ITEM_ADD"),
        ("item_remove", "ITEM_REMOVE"),
        ("item_update", "ITEM_UPDATE"),
    )
    type = models.CharField(
        max_length=20,
        choices= Order_Edit_Item_Change_Type
    )
    order_edit = models.ForeignKey(
        OrderEdit,
        on_delete=models.CASCADE,
        related_name='+'
    )
    original_line_item = models.ForeignKey(
        LineItem,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )
    line_item = models.OneToOneField(
        LineItem,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )



class PaymentCollectionStatus(models.TextChoices):
    NOT_PAID = 'not_paid'
    AWAITING = 'awaiting'
    AUTHORIZED = 'authorized'
    PARTIALLY_AUTHORIZED = 'partially_authorized'
    CANCELED = 'canceled'

class PaymentCollectionType(models.TextChoices):
    ORDER_EDIT = 'order_edit'

class PaymentCollection(BaseModel):
    Payment_Collection_Status = (
        ("not_paid", "NOT_PAID"),
        ("awaiting", "AWAITING"),
        ("authorized", "AUTHORIZED"),
        ("partially_authorized", "PARTIALLY_AUTHORIZED"),
        ("canceled", "CANCELED"),
    )

    Payment_Collection_Type  = (
        ("order_edit", "ORDER_EDIT"),
    )
    type = models.CharField(choices=Payment_Collection_Status, max_length=20)
    status = models.CharField(choices=Payment_Collection_Type, max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField()
    authorized_amount = models.FloatField(null=True, blank=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    payment_sessions = models.ManyToManyField(PaymentSession)
    payments = models.ManyToManyField(Payment)
    metadata = models.JSONField()
    created_by = models.CharField(max_length=255)


class PaymentProvider(BaseModel):
    is_installed = models.BooleanField(default=True)



class ProductCategory(BaseModel):
    name = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True, null=False)
    is_active = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


class ProductCollection(BaseModel):
    title = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True, null=True)
    products = models.ManyToManyField(Product, related_name='+')
    metadata = models.JSONField(null=True)



class ProductOptionValue(BaseModel):
    value = models.CharField(max_length=255)
    option = models.ForeignKey("ProductOption", on_delete=models.CASCADE, related_name='+')
    variant = models.ForeignKey("ProductVariant", on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)



class ProductOption(BaseModel):
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)




class ProductTaxRate(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tax_rate = models.ForeignKey("TaxRate", on_delete=models.CASCADE)
    metadata = models.JSONField(null=True)



class ProductTypeTaxRate(BaseModel):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    tax_rate = models.ForeignKey("TaxRate", on_delete=models.CASCADE)
    metadata = models.JSONField(blank=True, null=True)


class ProductVariantInventoryItem(BaseModel):
    inventory_item_id = models.TextField(unique=True)
    variant_id = models.TextField(unique=True)
    required_quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('variant_id', 'inventory_item_id'),)



class ProductVariant(BaseModel):
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    sku = models.CharField(max_length=255,null=True, unique=True)
    barcode = models.CharField(max_length=255,null=True, unique=True)
    ean = models.CharField(max_length=255,null=True, unique=True)
    upc = models.CharField(max_length=255,null=True, unique=True)
    variant_rank = models.PositiveIntegerField(default=0)
    inventory_quantity = models.PositiveIntegerField()
    allow_backorder = models.BooleanField(default=False)
    manage_inventory = models.BooleanField(default=True)
    hs_code = models.CharField(max_length=255,null=True)
    origin_country = models.CharField(max_length=255,null=True)
    mid_code = models.CharField(max_length=255, null=True)
    material = models.CharField(max_length=255, null=True)
    weight = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = (("sku", "barcode", "ean", "upc"),)


class PublishableApiKeySalesChannel(BaseModel):
    sales_channel_id = models.CharField(max_length=100, unique=True)
    publishable_key_id = models.CharField(max_length=100, unique=True)

class PublishableApiKey(BaseModel):
    created_by = models.CharField(max_length=100, null=True)
    revoked_by = models.CharField(max_length=100, null=True)
    revoked_at = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)


class Refund(BaseModel):
    Refund_Reason = (
        ("discount", "DISCOUNT"), 
        ("return", "RETURN"), 
        ("swap", "SWAP"), 
        ("claim", "CLAIM"), 
        ("other", "OTHER"), 
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True, related_name='+')
    amount = models.IntegerField()
    note = models.TextField(null=True)
    reason = models.CharField(choices=Refund_Reason, max_length=16)

    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(null=True, max_length=255)


class Region(BaseModel):
    name = models.CharField(max_length=100)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='+')
    tax_rate = models.FloatField()
    tax_rates = models.ForeignKey('TaxRate', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    tax_code = models.CharField(max_length=100, null=True)
    gift_cards_taxable = models.BooleanField(default=True)
    automatic_taxes = models.BooleanField(default=True)
    countries = models.ManyToManyField(Country, related_name='+')
    tax_provider = models.ForeignKey('TaxProvider', on_delete=models.SET_NULL, null=True)
    payment_providers = models.ManyToManyField(PaymentProvider, related_name='+')
    fulfillment_providers = models.ManyToManyField(FulfillmentProvider, related_name='+')
    metadata = models.JSONField(null=True)
    includes_tax = models.BooleanField(default=False)



class ReturnItem(BaseModel):
    return_order = models.ForeignKey(Return, on_delete=models.CASCADE, related_name = "return_items", null=True, blank=True)
    item = models.ForeignKey(LineItem,on_delete=models.CASCADE, related_name = "return_items", null=True, blank=True)
    quantity = models.IntegerField()
    is_requested = models.BooleanField(default=True)
    requested_quantity = models.IntegerField(null=True)
    received_quantity = models.IntegerField(null=True)
    reason = models.ForeignKey("ReturnReason", on_delete=models.SET_NULL, related_name='+', null=True)
    note = models.TextField(null=True)
    metadata = models.JSONField(null=True)


from django.db import models

class ReturnReason(BaseModel):
    value = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    parent_return_reason = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True
    )
    metadata = models.JSONField(blank=True, null=True)



from django.db import models

class ReturnStatus(models.TextChoices):
    REQUESTED = "requested"
    RECEIVED = "received"
    REQUIRES_ACTION = "requires_action"
    CANCELED = "canceled"


class SalesChannelLocation(BaseModel):
    sales_channel_id = models.CharField(max_length=255)
    location_id = models.CharField(max_length=255)


class ShippingMethodTaxLine(BaseModel):
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE, related_name='+')
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        unique_together = ('shipping_method', 'code')




class ShippingOptionRequirement(BaseModel):
    Requirement_Type = (
        ("min_subtotal", "MIN_SUBTOTAL"),
        ("max_subtotal", "MAX_SUBTOTAL"),
    )
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE, related_name='+')
    type = models.CharField(choices=Requirement_Type, max_length=32)
    amount = models.IntegerField()
    deleted_at = models.DateTimeField(null=True)



class ShippingProfileType(models.TextChoices):
    DEFAULT = 'default'
    GIFT_CARD = 'gift_card'
    CUSTOM = 'custom'

class ShippingProfile(BaseModel):
    Shipping_Profile_Type = (
        ("default", "DEFAULT"),
        ("gift_card", "GIFT_CARD"),
        ("custom", "CUSTOM"),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(choices=Shipping_Profile_Type, max_length=255)
    metadata = models.JSONField(null=True)


class TaxRate(BaseModel):
    rate = models.FloatField(null=True)
    code = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)
    products = models.ManyToManyField(Product, through='ProductTaxRate')
    product_types = models.ManyToManyField(ProductType, through='ProductTypeTaxRate')
    shipping_options = models.ManyToManyField(ShippingOption, through='ShippingTaxRate')
    product_count = models.IntegerField(null=True, blank=True)
    product_type_count = models.IntegerField(null=True, blank=True)
    shipping_option_count = models.IntegerField(null=True, blank=True)

class ShippingTaxRate(BaseModel):
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE, related_name='+')
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)

class StagedJob(BaseModel):
    event_name = models.CharField(max_length=255)
    data = models.JSONField()
    options = models.JSONField(default=dict)


class Store(BaseModel):
    name = models.CharField(max_length=255)
    default_currency_code = models.CharField(default="usd", max_length=255)
    # currencies = models.ManyToManyField( Currency, on_delete=models.CASCADE)
    swap_link_template = models.TextField(null=True, blank=True)
    payment_link_template = models.TextField(null=True, blank=True)
    invite_link_template = models.TextField(null=True, blank=True)
    default_location_id = models.CharField(null=True, max_length=255)
    metadata = models.JSONField(null=True, blank=True)
    default_sales_channel = models.OneToOneField(SalesChannel,null=True, blank=True, on_delete=models.SET_NULL)


class Swap(BaseModel):
    Swap_Fulfillment_Status = (
        ("not_fulfilled", "NOT_FULFILLED"),
        ("fulfilled", "FULFILLED"),
        ("shipped", "SHIPPED"),
        ("partially_shipped", "PARTIALLY_SHIPPED"),
        ("canceled", "CANCELED"),
        ("requires_action", "REQUIRES_ACTION"),
    )

    Swap_Payment_Status = (
        ("not_paid", "NOT_PAID"),
        ("awaiting", "AWAITING"),
        ("captured", "CAPTURED"),
        ("confirmed", "CONFIRMED"),
        ("canceled", "CANCELED"),
        ("difference_refunded", "DIFFERENCE_REFUNDED"),
        ("partially_refunded", "PARTIALLY_REFUNDED"),
        ("refunded", "REFUNDED"),
        ("requires_action", "REQUIRES_ACTION"),
    )
    fulfillment_status = models.CharField(
        max_length=20,
        choices=Swap_Fulfillment_Status,
        default="NOT_FULFILLED"
    )
    payment_status = models.CharField(
        max_length=20,
        choices=Swap_Payment_Status,
        default="NOT_PAID"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='+')
    return_order = models.OneToOneField(Return, on_delete=models.CASCADE, related_name='+')
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE,  related_name='+')
    difference_due = models.IntegerField(null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE,  related_name='+')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE,  related_name='+')
    confirmed_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    no_notification = models.BooleanField(null=True)
    allow_back_order = models.BooleanField(default=False)
    idempotency_key = models.CharField(max_length=255, null=True)
    metadata = models.JSONField(null=True)



class TaxProvider(BaseModel):
    is_installed = models.BooleanField(default= True)


class TrackingLink(BaseModel):
    url = models.URLField(blank=True, null=True)
    tracking_number = models.CharField(max_length=255)
    fulfillment = models.ForeignKey(Fulfillment, related_name='+', on_delete=models.CASCADE)
    idempotency_key = models.CharField(max_length=255, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)