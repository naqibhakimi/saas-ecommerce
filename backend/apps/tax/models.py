from django.db import models
from apps.core.models import BaseModel


# Create your models here.
class TaxLine(BaseModel):
    rate = models.FloatField()
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)


class TaxRate(BaseModel):
    """
    TaxRate model defines general tax rates that can be used across your platform, while the 
    ProductTaxRate model associates these general tax rates with specific products, 
        enabling you to customize tax calculations for individual products. 
        The distinction between the two models allows for flexibility and customization
        in how taxes are applied to different products in your e-commerce platform.

    Represents different tax rates that apply to products based on tax laws and regulations.
    Example: "Standard Tax (10%)," "Zero Tax (0%)," "Special Tax (15%)"

    rate: This field stores the tax rate percentage. For example,
        if the tax rate is 10%, the rate field would hold the value 10.0.

    code: This field could hold a unique code for the tax rate,
        which can be useful for identifying tax rates in systems or reports.

    name: The name field stores a human-readable name for the tax rate.
        For example, "Standard Tax (10%)" could be a name for a tax rate.

    product_count: This field represents the number of products associated with this tax rate.
        It helps track the number of products that use this tax rate.

    product_type_count: Similarly, this field represents the number of product types
        associated with this tax rate. It helps track the number of product types using this tax rate.

    shipping_option_count: This field represents the number of shipping options 
        that apply this tax rate. Shipping options could include different delivery 
        methods with varying tax rates.
    """
    rate = models.FloatField(null=True)
    code = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    # metadata = models.JSONField(null=True, blank=True)
    product_count = models.IntegerField(null=True, blank=True)
    product_type_count = models.IntegerField(null=True, blank=True)
    shipping_option_count = models.IntegerField(null=True, blank=True)


class TaxProvider(BaseModel):
    """
    TaxProvider: This is a model representing a tax provider in your e-commerce platform.
        A tax provider is a service or component that calculates and manages taxes
        for products during the checkout process.

        Suppose you have two tax providers, "Standard Tax Calculator" and "Advanced Tax Calculator,"
        that your e-commerce platform can use to calculate taxes for products.
    """
    is_installed = models.BooleanField(default=True)
