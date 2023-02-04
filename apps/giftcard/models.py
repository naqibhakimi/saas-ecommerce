from django.db import models
from apps.core.models import BaseModel


class GiftCard(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    value = models.IntegerField()
    balance = models.IntegerField()
    region = models.ForeignKey('customer.Region', on_delete=models.CASCADE)
    order = models.ForeignKey('order.Order', on_delete=models.SET_NULL, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)
    ends_at = models.DateTimeField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)


class GiftCardTransaction(BaseModel):
    gift_card = models.ForeignKey(GiftCard, on_delete=models.CASCADE, related_name='+')
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='+')
    amount = models.IntegerField()
    is_taxable = models.BooleanField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ("gift_card_id", "order_id")
