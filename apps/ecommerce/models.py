from django.contrib.auth.models import User
from django.db import models
from apps.core.models import BaseModel
from django.core.validators import EmailValidator


class Order(models.Model):
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
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    email = models.EmailField()
    billing_address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name="orders", null=True)
    shipping_address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name="orders", null=True)
    region = models.foreignKey('Region', on_delete = models.CASCADE)
    order_number = models.CharField(max_length=255, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    subtotal_price = models.DecimalField(max_digits=20, decimal_places=2)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)


    # currency_code = models.CharField(max_length=10)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    tax_rate = models.FloatField(null=True)
    discounts = models.ManyToManyField('Discount', through='OrderDiscount')
    gift_cards = models.ManyToManyField('GiftCard', through='OrderGiftCard')
    draft_order = models.OneToOneField('DraftOrder', on_delete=models.CASCADE, related_name="orders", null=True)
    canceled_at = models.DateField(null=True)
    metadata = models.JSONField(null=True)
    no_notification = models.BooleanField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    sales_channel = models.ForeignKey('SalesChannel', on_delete=models.CASCADE, related_name="orders", null=True, blank=True)

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
        'Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='billing_address'
    )
    phone = models.CharField(max_length=255, blank=True, null=True)
    has_account = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    orders = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='customers'
    )
    groups = models.ManyToManyField('CustomerGroup', related_name='customers')
    metadata = models.JSONField(blank=True, null=True)



class Region(BaseModel):
    pass

class Country(BaseModel):
    iso_2 = models.CharField(max_length=255, unique=True)
    iso_3 = models.CharField(max_length=255)
    num_code = models.IntegerField()
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)


class Address(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField()
    
    
class AnalyticsConfig(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opt_out = models.BooleanField(default=False)
    anonymize = models.BooleanField(default=False)


class BatchJobStatus:
    pass 
class BatchJob(BaseModel):
    type = models.CharField(max_length=255, null=True, blank=True )
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
    pass

class GiftCard(BaseModel):
    pass


class LineItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True, related_name='line_items')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='line_items')
    swap = models.ForeignKey('Swap', on_delete=models.SET_NULL, null=True, related_name='line_items')
    claim_order = models.ForeignKey('ClaimOrder', on_delete=models.SET_NULL, null=True, related_name='line_items')
    original_item = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='line_item')
    order_edit = models.ForeignKey('OrderEdit', on_delete=models.SET_NULL, null=True, related_name='line_items')
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, null=True, related_name="line_items")
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
    pass

class PaymentSession(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


class ShippingMethod(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

class SalesChannel(BaseModel):
    pass
class Cart(BaseModel):
    CART_TYPE_CHOICES = (
        ("default", "Default"),
        ("swap", "Swap"),
        ("draft_order", "Draft Order"),
        ("payment_link", "Payment Link"),
        ("claim", "Claim"),
    )
    email = models.EmailField(blank=True, null=True)
    billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='billing_address', blank=True, null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='shipping_address', blank=True, null=True)
    items = models.ManyToManyField(LineItem, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    discounts = models.ManyToManyField(Discount, blank=True)
    gift_cards = models.ManyToManyField(GiftCard, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    payment_session = models.OneToOneField(PaymentSession, on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    shipping_methods = models.ManyToManyField(ShippingMethod, blank=True)
    type = models.CharField(max_length=20, choices=CART_TYPE_CHOICES, default='default')
    completed_at = models.DateTimeField(blank=True, null=True)
    payment_authorized_at = models.DateTimeField(blank=True, null=True)
    idempotency_key = models.CharField(max_length=255, blank=True, null=True)
    context = models.JSONField(blank=True, null=True)
    metadata = models.JSONField() # [FIXME] do we even need this ? 
    sales_channel = models.ForeignKey(SalesChannel, related_name='sales_channel', on_delete=models.SET_NULL, null=True)



class ClaimOrder(BaseModel):
    claim_items = models.ForeignKey('ClaimItem', on_delete=models.CASCADE)


class ClaimTag(BaseModel):
    value = models.CharField(max_length=255, unique=True)
    metadata = models.JSONField(null=True)

class ProductVariant(BaseModel):
    pass

class ClaimItem(BaseModel):
    REASON_CHOICES = (
        ('missing_item', 'Missing Item'),
        ('wrong_item', 'Wrong Item'),
        ('production_failure', 'Production Failure'),
        ('other', 'Other'),
    )
    images = models.ManyToManyField('ClaimImage', on_delete=models.CASCADE)
    claim_order = models.ForeignKey(ClaimOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255, choices=REASON_CHOICES)
    note = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    tags = models.ManyToManyField(ClaimTag)
    metadata = models.JSONField(blank=True, null=True)

class ClaimImage(BaseModel):
    claim_item = models.ForeignKey(ClaimItem, on_delete=models.CASCADE, related_name='claim_images')
    url = models.CharField(max_length=255)
    metadata = models.JSONField(null=True, blank=True)



class Return(BaseModel):
    pass

class Fulfillment(BaseModel):
    pass
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
        related_name='claim_order',
    )
    additional_items = models.ManyToManyField(
        LineItem,
        related_name='claim_order',
    )
    type = models.CharField(
        max_length=20,
        choices=Claim_Type,
    )
    order_id = models.CharField(max_length=255)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='claims',
    )
    return_order = models.OneToOneField(
        Return,
        on_delete=models.CASCADE,
        related_name='claim_order',
        null=True,
        blank=True,
    )
    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='claim_order',
        null=True,
        blank=True,
    )
    shipping_methods = models.ManyToManyField(
        ShippingMethod,
        related_name='claim_order',
    )
    fulfillments = models.ManyToManyField(
        Fulfillment,
        related_name='claim_order',
    )
    refund_amount = models.IntegerField(null=True, blank=True)
    canceled_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    no_notification = models.BooleanField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    idempotency_key = models.CharField(max_length=255, null=True, blank=True)


class Currency(BaseModel):
    code = models.CharField(primary_key=True, max_length=255)
    symbol = models.CharField(max_length=255)
    symbol_native = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    includes_tax = models.BooleanField(default=False)


class ShippingOption(BaseModel):
    pass
class CustomShippingOption(BaseModel):
    price = models.IntegerField()
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (('shipping_option', 'cart'),)


class PriceList(BaseModel):
    pass

class CustomerGroup(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    customers = models.ManyToManyField(Customer, on_delete=models.CASCADE)
    price_lists = models.ManyToManyField(PriceList, on_delete=models.CASCADE)
    metadata = models.JSONField(null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)



class DiscountCondition(BaseModel):
    pass

class DiscountConditionCustomerGroup(BaseModel):
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(null=True, blank=True)


class ProductCollection(BaseModel):
    pass 


class DiscountConditionProductCollection(BaseModel):
    product_collection_id = models.CharField(primary_key=True, max_length=255)
    condition_id = models.CharField(primary_key=True, max_length=255)
    product_collection = models.ForeignKey(ProductCollection, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE)
    metadata = models.JSONField(null=True)


class ProductTag(BaseModel):
    pass
class DiscountConditionProductTag(BaseModel):
    product_tag_id = models.CharField(primary_key=True, max_length=255)
    condition_id = models.CharField(primary_key=True, max_length=255)
    product_tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)


class ProductType(BaseModel):
    pass
class DiscountConditionProductType(BaseModel):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='discount_condition_product_types')
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name='discount_condition_product_types')
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product_type", "discount_condition"),)


class Product(BaseModel):
    pass
class DiscountConditionProduct(BaseModel):
    product_id = models.CharField(max_length=255)
    condition_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="discount_condition_products")
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name="discount_condition_products")
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product", "discount_condition"),)


class DiscountRule(BaseModel):
    pass
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
        DiscountRule,
        on_delete=models.CASCADE,
        related_name="conditions"
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
        ProductCollection,
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
    conditions = models.ManyToManyField('DiscountCondition', related_name='discount_rule')
    metadata = models.JSONField(null=True)


class Discount(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    is_dynamic = models.BooleanField()
    rule = models.ForeignKey(DiscountRule, on_delete=models.CASCADE, null=True)
    is_disabled = models.BooleanField()
    parent_discount = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    starts_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    valid_duration = models.CharField(max_length=255, null=True, blank=True)
    regions = models.ManyToManyField(Region)
    usage_limit = models.IntegerField(null=True, blank=True)
    usage_count = models.IntegerField(default=0)
    metadata = models.JSONField(null=True, blank=True)


class DraftOrder(BaseModel):
    Draft_Order_Status = (
        ("open", "OPEN"),
        ("completed", "COMPLETED"),
    )
    status = models.CharField(max_length=10,choices=Draft_Order_Status, default="OPEN")
    display_id = models.AutoField(primary_key=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, related_name='draft_order')
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    canceled_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    no_notification_order = models.BooleanField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)


    
class Fulfillment(BaseModel):
    pass

class FulfillmentItem(BaseModel):
    fulfillment = models.ForeignKey(Fulfillment, on_delete=models.CASCADE)
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class FulfillmentProvider(BaseModel):
    is_installed = models.BooleanField(default=True)


class Swap(BaseModel):
    pass

class TrackingLink(BaseModel):
    pass

class Fulfillment(BaseModel):
    claim_order = models.ForeignKey(ClaimOrder, on_delete=models.CASCADE, null=True, related_name='fulfillments')
    swap = models.ForeignKey(Swap, on_delete=models.CASCADE, null=True, related_name='fulfillments')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='fulfillments')
    no_notification = models.BooleanField(null=True)
    provider = models.ForeignKey(FulfillmentProvider, on_delete=models.CASCADE)
    location_id = models.CharField(max_length=255, null=True)
    items = models.OneToManyField(FulfillmentItem, on_delete=models.CASCADE, related_name='fulfillment')
    tracking_links = models.OneToManyField(TrackingLink, on_delete=models.CASCADE, related_name='fulfillment')
    tracking_numbers = models.JSONField(default=[])
    data = models.JSONField()
    shipped_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)



class GiftCard(BaseModel):
    pass


from django.db import models

class GiftCard(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    value = models.IntegerField()
    balance = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)
    ends_at = models.DateTimeField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)


class GiftCardTransaction(BaseModel):
    gift_card = models.ForeignKey(GiftCard, on_delete=models.CASCADE, related_name='gift_card_transactions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
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


class Invite(models.Model):
    User_Roles = (
        ("admin", "ADMIN"),
        ("member", "MEMBER"),
        ("developer", "DEVELOPER"),
    )
    user_email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in UserRoles], default=UserRoles.MEMBER)
    accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=255)
    expires_at = models.DateTimeField()
    metadata = models.JSONField(null=True)
    deleted_at = models.DateTimeField(null=True)


class LineItemAdjustment(BaseModel):
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE, related_name="line_item_adjustments")
    description = models.CharField(max_length=255, null=True, blank=True)
    discount = models.ManyToManyField(Discount)
    amount = models.IntegerField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)



from django.db import models
from django.db.models import CASCADE


class LineItemAdjustment(models.Model):
    item = models.ForeignKey(LineItem, on_delete=CASCADE, related_name="line_item_adjustments")
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    metadata = models.JSONField(null=True, blank=True)


class TaxLine(models.Model):
    pass

class LineItemTaxLine(models.Model):
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True)


class MoneyAmount(models.Model):
    # do we need this ? 
    # currency_code = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='money_amounts')
    amount = models.IntegerField()
    min_quantity = models.IntegerField(null=True)
    max_quantity = models.IntegerField(null=True)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE, null=True, related_name='money_amounts')
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='money_amounts')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, related_name='money_amounts')


class Note(models.Model):
    value = models.TextField()
    resource_type = models.CharField(max_length=255, null=True, blank=True)
    resource_id = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    metadata = models.JSONField(null=True)



class NotificationProvider(models.Model):
    is_installed = models.BooleanField(default=True)



class Notification(models.Model):
    event_name = models.CharField(max_length=255, null=True)
    resource_type = models.CharField(max_length=255)
    resource_id = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notifications')
    to = models.CharField(max_length=255)
    data = models.JSONField()
    parent_notification = models.ForeignKey('self', on_delete=models.CASCADE, related_name='notifications', null=True)
    provider = models.ForeignKey(NotificationProvider, on_delete=models.CASCADE, related_name='notifications')
    

class Oauth(models.Model):
    display_name = models.CharField(max_length=255)
    application_name = models.CharField(max_length=255, unique=True)
    install_url = models.CharField(max_length=255, null=True)
    uninstall_url = models.CharField(max_length=255, null=True)
    data = models.JSONField(null=True)
    

class OrderEdit(models.Model):
    Order_Edit_Status = (
        ("confirmed", "CONFIRMED"),
        ("declined", "DECLINED"),
        ("requested", "REQUESTED"),
        ("created", "CREATED"),
        ("canceled", "CANCELED"),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="edits")
    changes = models.ManyToManyField("OrderItemChange", related_name="order_edit")
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
    items = models.ManyToManyField(LineItem, related_name="order_edits")
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


class OrderItemChange(models.Model):
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
        related_name='order_item_changes'
    )
    original_line_item = models.ForeignKey(
        LineItem,
        on_delete=models.SET_NULL,
        related_name='order_item_changes',
        null=True,
        blank=True,
    )
    line_item = models.OneToOneField(
        LineItem,
        on_delete=models.SET_NULL,
        related_name='order_item_changes',
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

class PaymentCollection(models.Model):
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
    status = models.CharField(choices=PaymentCollectionStatus.choices, max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField()
    authorized_amount = models.IntegerField(null=True, blank=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    payment_sessions = models.ManyToManyField('PaymentSession')
    payments = models.ManyToManyField('Payment')
    metadata = models.JSONField()
    created_by = models.CharField(max_length=255)
