from django.db import models
from apps.core.models import BaseModel
from apps.core.models import BaseModel
from apps.inventory.models import  FulfillmentProvider
from apps.tax.models import TaxRate



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

class ShippingOption(BaseModel):
    Shipping_Option_Price_Type = (
        ("flat_rate", "FLAT_RATE"),
        ("calculated", "CALCULATED")
    )
    name = models.CharField(max_length=255)
    region = models.ForeignKey('customer.Region', on_delete=models.CASCADE)
    profile = models.ForeignKey(ShippingProfile, on_delete=models.CASCADE, related_name='+')
    provider = models.ForeignKey(FulfillmentProvider, on_delete=models.CASCADE, related_name='+')
    price_type = models.CharField(max_length=20, choices=Shipping_Option_Price_Type, default="FLAT_RATE")
    amount = models.PositiveIntegerField(null=True)
    is_return = models.BooleanField(default=False)
    admin_only = models.BooleanField(default=False)
    # requirements = models.ManyToManyField("ShippingOptionRequirement", through="ShippingOptionRequirement")
    data = models.JSONField()
    metadata = models.JSONField(null=True)
    includes_tax = models.BooleanField(default=False)


class ShippingMethod(BaseModel):
    price = models.PositiveIntegerField()
    data = models.JSONField()
    includes_tax = models.BooleanField(default=False)
    subtotal = models.PositiveIntegerField(null=True)
    total = models.PositiveIntegerField(null=True)
    tax_total = models.PositiveIntegerField(null=True)
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE, related_name='shipping_methods')

class CustomShippingOption(BaseModel):
    price = models.IntegerField()
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE)
    cart = models.ForeignKey('store.Cart', on_delete=models.SET_NULL, null=True)
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (('shipping_option', 'cart'),)



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



class ShippingTaxRate(BaseModel):
    shipping_option = models.ForeignKey(ShippingOption, on_delete=models.CASCADE, related_name='+')
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)
