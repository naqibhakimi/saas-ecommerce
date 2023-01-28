from django.contrib.auth.models import User
from django.db import models
from apps.core.models import BaseModel
from django.core.validators import EmailValidator


class Order(BaseModel):
    pass

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

class LineItem(BaseModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

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
class DiscountConditionProductTag(models.Model):
    product_tag_id = models.CharField(primary_key=True, max_length=255)
    condition_id = models.CharField(primary_key=True, max_length=255)
    product_tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey('DiscountCondition', on_delete=models.CASCADE)
    metadata = models.JSONField(null=True, blank=True)


class ProductType(BaseModel):
    pass
class DiscountConditionProductType(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='discount_condition_product_types')
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name='discount_condition_product_types')
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product_type", "discount_condition"),)


class Product(BaseModel):
    pass
class DiscountConditionProduct(models.Model):
    product_id = models.CharField(max_length=255)
    condition_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="discount_condition_products")
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name="discount_condition_products")
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product", "discount_condition"),)


class DiscountRule(BaseModel):
    pass
class DiscountCondition(models.Model):
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


class DiscountRuleType(models.TextChoices):
    FIXED = 'fixed'
    PERCENTAGE = 'percentage'
    FREE_SHIPPING = 'free_shipping'

class AllocationType(models.TextChoices):
    TOTAL = 'total'
    ITEM = 'item'

class DiscountRule(models.Model):
    description = models.CharField(max_length=255, null=True)
    type = models.CharField(choices=DiscountRuleType.choices, max_length=20)
    value = models.FloatField()
    allocation = models.CharField(choices=AllocationType.choices, max_length=20, null=True)
    conditions = models.ManyToManyField('DiscountCondition', related_name='discount_rule')
    metadata = models.JSONField(null=True)
