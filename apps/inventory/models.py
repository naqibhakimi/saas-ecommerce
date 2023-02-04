from django.db import models
from apps.core.models import BaseModel
from django.conf import settings
from apps.order import Order, ClaimOrder
from apps.invoice.models import LineItem, FulfillmentProvider
from apps.store.models import Swap


    
class AnalyticsConfig(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='+')
    opt_out = models.BooleanField(default=False)
    anonymize = models.BooleanField(default=False)

class BatchJobStatus(models.TextChoices):
    PRE_PROCESSED='PRE_PROCESSED'
    CONFIRMED='CONFIRMED'
    PROCESSING='PROCESSING'
    COMPLETED='COMPLETED'
    CANCELED='CANCELED'
    FAILED='FAILED'
    CREATED='CREATED'

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



class Fulfillment(BaseModel):
    claim_order = models.ForeignKey(ClaimOrder, on_delete=models.CASCADE, null=True, related_name='+')
    swap = models.ForeignKey(Swap, on_delete=models.CASCADE, null=True, related_name='+')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='+')
    no_notification = models.BooleanField(null=True)
    provider = models.ForeignKey(FulfillmentProvider, on_delete=models.CASCADE)
    location_id = models.CharField(max_length=255, null=True)
    # items = models.OneToManyField("FulfillmentItem", on_delete=models.CASCADE, related_name='+')
    # tracking_links = models.OneToManyField("TrackingLink", on_delete=models.CASCADE, related_name='+')
    tracking_numbers = models.JSONField(default=dict)
    data = models.JSONField()
    shipped_at = models.DateTimeField(null=True)
    canceled_at = models.DateTimeField(null=True)
    metadata = models.JSONField(null=True)
    idempotency_key = models.CharField(max_length=255, null=True)




class FulfillmentItem(BaseModel):
    fulfillment = models.ForeignKey(Fulfillment, on_delete=models.CASCADE)
    item = models.ForeignKey(LineItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class FulfillmentProvider(BaseModel):
    is_installed = models.BooleanField(default=True)


class TrackingLink(BaseModel):
    url = models.URLField(blank=True, null=True)
    tracking_number = models.CharField(max_length=255)
    fulfillment = models.ForeignKey(Fulfillment, related_name='+', on_delete=models.CASCADE)
    idempotency_key = models.CharField(max_length=255, blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)