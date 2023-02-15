from django.db import models
from django.conf import settings
from apps.core.models import BaseModel
from apps.giftcard.models import GiftCard
from apps.shipping.models import ShippingMethod

from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericForeignKey

from django.utils import timezone

from apps.store.querysets import NoteQuerSet


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
    objects = NoteQuerSet.as_manager()



class NotificationProvider(BaseModel):
    is_installed = models.BooleanField(default=True)



class NotificationQuerySet(models.query.QuerySet):
    """Notification QuerySet"""

    def unsent(self):
        return self.filter(emailed=False)

    def sent(self):
        return self.filter(emailed=True)

    def unread(self, include_deleted=False):
        return self.filter(unread=True, deleted=False)

    def read(self, include_deleted=False):
        return self.filter(unread=False)

    def mark_all_as_read(self, recipient=None):
        qset = self.unread(True)
        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(unread=False)

    def mark_all_as_unread(self, recipient=None):
        qset = self.read(True)

        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(unread=True)

    def deleted(self):
        return self.filter(deleted=True)

    def active(self):
        return self.filter(deleted=False)

    def mark_all_as_deleted(self, recipient=None):
        qset = self.active()
        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(deleted=True)

    def mark_all_as_active(self, recipient=None):
        qset = self.deleted()
        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(deleted=False)

    def mark_as_unsent(self, recipient=None):
        qset = self.sent()
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(emailed=False)

    def mark_as_sent(self, recipient=None):
        qset = self.unsent()
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(emailed=True)

class LevelChoices(models.Choices):
    INFO="info"
    WARNING='warning'
    DANGER="danger"
    SUCCESS = 'success'


class Notification(BaseModel):
   
    level = models.CharField(choices=LevelChoices.choices, default=LevelChoices.SUCCESS, max_length=20)

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        related_name="notifications",
        on_delete=models.CASCADE,
    )

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        null=True,
        related_name="zenpro_notifications_actor",
        on_delete=models.CASCADE,
    )

    unread = models.BooleanField(default=True, blank=False, db_index=True)
    verb = models.TextField()
    description = models.TextField(blank=True, null=True)

    target_content_type = models.ForeignKey(
        ContentType,
        related_name="notify_target",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    target = GenericForeignKey("target_content_type", "target_object_id")

    action_object_content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="notify_action_object",
        on_delete=models.CASCADE,
    )
    action_object_object_id = models.CharField(max_length=255, blank=True, null=True)
    action_object = GenericForeignKey(
        "action_object_content_type", "action_object_object_id"
    )

    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    public = models.BooleanField(default=True, db_index=True)
    deleted = models.BooleanField(default=False, db_index=True)
    emailed = models.BooleanField(default=False, db_index=True)

    data = models.JSONField(blank=True, null=True)

    @property
    def get_target(self):
        ct = ContentType.objects.get_for_id(self.target_content_type.id)
        obj = ct.get_object_for_this_type(pk=self.target_object_id)
        return obj

    @property
    def get_action(self):
        ct = ContentType.objects.get_for_id(self.action_object_content_type.id)
        obj = ct.get_object_for_this_type(pk=self.action_object_object_id)
        return obj

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ("-timestamp",)
        index_together = ("recipient", "unread")

    def __str__(self):
        ctx = {
            "actor": self.actor,
            "verb": self.verb,
            "action_object": self.action_object,
            "target": self.target,
            "timesince": self.timesince,
        }
        if self.target:
            if self.action_object:
                return (
                    "%(actor)s %(verb)s %(action_object)s on %(target)s %(timesince)s ago"
                    % ctx
                )
            return "%(actor)s %(verb)s %(target)s %(timesince)s ago" % ctx
        if self.action_object:
            return "%(actor)s %(verb)s %(action_object)s %(timesince)s ago" % ctx
        return "%(actor)s %(verb)s %(timesince)s ago" % ctx

    @property
    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_

        return timesince_(self.timestamp, now).split(",")[0]

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def mark_as_unread(self):
        if not self.unread:
            self.unread = True
            self.save()

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

