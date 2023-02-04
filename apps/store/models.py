from django.db import models
from django.conf import settings
from apps.core.models import BaseModel
from apps.giftcard.models import GiftCard
from apps.shipping.models import ShippingMethod




class SalesChannel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)


class SalesChannelLocation(BaseModel):
    sales_channel_id = models.CharField(max_length=255)
    location_id = models.CharField(max_length=255)



class Cart(BaseModel):
    CART_TYPE_CHOICES = (
        ("default", "Default"),
        ("swap", "Swap"),
        ("draft_order", "Draft Order"),
        ("payment_link", "Payment Link"),
        ("claim", "Claim"),
    )
    email = models.EmailField(blank=True, null=True)
    billing_address = models.ForeignKey('customer.Address', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    shipping_address = models.ForeignKey('customer.Address', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    items = models.ManyToManyField('invoice.LineItem', blank=True, related_name='+')
    region = models.ForeignKey('customer.Region', on_delete=models.CASCADE)
    discounts = models.ManyToManyField('discount.Discount', blank=True, related_name='+')
    gift_cards = models.ManyToManyField(GiftCard, blank=True, related_name='+')
    customer = models.ForeignKey('customer.Customer', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    payment_session = models.OneToOneField('payment.PaymentSession', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    payment = models.OneToOneField('payment.Payment', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    shipping_methods = models.ManyToManyField(ShippingMethod, blank=True, related_name='+')
    type = models.CharField(max_length=20, choices=CART_TYPE_CHOICES, default='default')
    completed_at = models.DateTimeField(blank=True, null=True)
    payment_authorized_at = models.DateTimeField(blank=True, null=True)
    idempotency_key = models.CharField(max_length=255, blank=True, null=True)
    context = models.JSONField(blank=True, null=True)
    metadata = models.JSONField() # [FIXME] do we even need this ? 
    sales_channel = models.ForeignKey(SalesChannel, related_name='+', on_delete=models.SET_NULL, null=True)



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
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, related_name='+')
    to = models.CharField(max_length=255)
    data = models.JSONField()
    parent_notification = models.ForeignKey('self', on_delete=models.CASCADE, related_name='+', null=True)
    provider = models.ForeignKey(NotificationProvider, on_delete=models.CASCADE, related_name='+')
    


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
    """
    A swap occurs when a customer wants to exchange one or more products they have
    bought for different items. This process involves returning the original products 
    and receiving new ones. The payment for the returned items will be applied towards 
    the purchase of the new ones. If the payment for the returned products is greater than 
    the cost of the new items, a refund for the remaining amount will be provided.
    """
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
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='+')
    return_order = models.OneToOneField('order.Return', on_delete=models.CASCADE, related_name='+')
    payment = models.OneToOneField('payment.Payment', on_delete=models.CASCADE,  related_name='+')
    difference_due = models.IntegerField(null=True)
    shipping_address = models.ForeignKey('customer.Address', on_delete=models.CASCADE,  related_name='+')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE,  related_name='+')
    confirmed_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    no_notification = models.BooleanField(null=True)
    allow_back_order = models.BooleanField(default=False)
    idempotency_key = models.CharField(max_length=255, null=True)
    metadata = models.JSONField(null=True)

