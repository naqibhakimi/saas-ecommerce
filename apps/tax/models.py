from django.db import models
from apps.core.models import BaseModel
from apps.customer.models import Region
from apps.product.models import ProductType, Product
from apps.shipping.models import ShippingOption
# Create your models here.
class TaxLine(BaseModel):
    rate = models.FloatField()
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)



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


class TaxProvider(BaseModel):
    is_installed = models.BooleanField(default= True)
