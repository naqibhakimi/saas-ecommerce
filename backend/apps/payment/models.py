from django.db import models
from apps.order.models import Order
from apps.core.models import BaseModel
from apps.core.models import BaseModel
from apps.store.models import Cart, Swap
from apps.order.models import Order

class IdempotencyKey(BaseModel):
    idempotency_key = models.CharField(unique=True, max_length=255)
    locked_at = models.DateTimeField(null=True, blank=True)
    request_method = models.CharField(max_length=255, null=True, blank=True)
    request_params = models.JSONField(null=True, blank=True)
    request_path = models.CharField(max_length=255, null=True, blank=True)
    response_code = models.IntegerField(null=True, blank=True)
    response_body = models.JSONField(null=True, blank=True)
    recovery_point = models.CharField(default="started", max_length=255)
    
class Currency(BaseModel):
    code = models.CharField(unique=True, max_length=255)
    symbol = models.CharField(max_length=255)
    symbol_native = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    includes_tax = models.BooleanField(default=False)


class Payment(BaseModel):
    swap = models.OneToOneField(Swap, on_delete=models.SET_NULL, null=True,  related_name='+')
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, related_name='+', null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='+', null=True)
    amount = models.FloatField()
    # currency_code = models.CharField(max_length=3)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, related_name='+', null=True)
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
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='+', null=True)
    provider_id = models.CharField(max_length=100)
    is_selected = models.BooleanField(null=True)
    is_initiated = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=Payment_Session_Status)
    data = models.JSONField()
    idempotency_key = models.CharField(max_length=100, null=True)
    amount = models.FloatField(null=True)
    payment_authorized_at = models.DateTimeField(null=True)


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
    region = models.ForeignKey('customer.Region', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    payment_sessions = models.ManyToManyField(PaymentSession)
    payments = models.ManyToManyField(Payment)
    metadata = models.JSONField()
    created_by = models.CharField(max_length=255)


class PaymentProvider(BaseModel):
    is_installed = models.BooleanField(default=True)


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
