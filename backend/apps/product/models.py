from django.db import models

from apps.core.models import BaseModel
from apps.store.models import SalesChannel
from apps.tax.models import TaxRate
from apps.shipping.models import ShippingProfile


class PriceList(BaseModel):
    """Price Lists represents a set of prices that overrides the
        default price for one or more product variants.
    """
    # [FIXME: circular import ]
    # from apps.customer.models import CustomerGroup
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, default="sale")
    status = models.CharField(max_length=255, default="draft")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    # description: The Customer Groups that the Price List applies to. Available if the relation `customer_groups` is expanded.
    # customer_groups = models.ManyToManyField("CustomerGroup", related_name="+")
    includes_tax = models.BooleanField(default=False)


class MoneyAmount(BaseModel):
    # do we need this ?
    # currency_code = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey(
        "payment.Currency", on_delete=models.CASCADE, related_name="+"
    )
    amount = models.FloatField()
    min_quantity = models.IntegerField(null=True)
    max_quantity = models.IntegerField(null=True)
    price_list = models.ForeignKey(
        PriceList, on_delete=models.CASCADE, null=True, related_name="+"
    )
    variant = models.ForeignKey(
        "ProductVariant", on_delete=models.CASCADE, related_name="+"
    )
    region = models.ForeignKey(
        "customer.Region", on_delete=models.CASCADE, null=True, related_name="+"
    )


class ProductType(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(blank=True, null=True)


class ProductTag(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)


class Image(BaseModel):
    url = models.CharField(max_length=255, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class ProductCollection(BaseModel):
    title = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True, null=True)
    # products = models.ManyToManyField(Product, related_name="+")
    metadata = models.JSONField(null=True)


class Product(BaseModel):
    Product_Status = (
        ("draft", "DRAFT"),
        ("proposed", "PROPOSED"),
        ("published", "PUBLISHED"),
        ("rejected", "REJECTED"),
    )
    title = models.CharField(max_length=255)
    subtitle = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    handle = models.TextField(null=True, blank=True, unique=True)
    is_gift_card = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=Product_Status, default="draft")
    images = models.ManyToManyField(Image, related_name="+")
    thumbnail = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(
        ShippingProfile, on_delete=models.CASCADE, related_name="+", null=True, blank=True
    )
    weight = models.PositiveIntegerField(null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    hs_code = models.TextField(null=True, blank=True)
    origin_country = models.TextField(null=True, blank=True)
    mid_code = models.TextField(null=True, blank=True)
    material = models.TextField(null=True, blank=True)
    collection = models.ForeignKey(
        ProductCollection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    type = models.ForeignKey(
        ProductType, on_delete=models.SET_NULL, null=True, blank=True, related_name="+"
    )
    tags = models.ManyToManyField(ProductTag, related_name="+")
    discountable = models.BooleanField(default=True)
    external_id = models.TextField(null=True, blank=True)
    sales_channels = models.ManyToManyField(
        SalesChannel, related_name="+")
    metadata = models.JSONField(null=True, blank=True)


class ProductCategory(BaseModel):
    name = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True, null=False)
    is_active = models.BooleanField(default=False)
    is_internal = models.BooleanField(default=False)
    parent_category = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )


class ProductOption(BaseModel):
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="+")
    metadata = models.JSONField(null=True)


class ProductOptionValue(BaseModel):
    value = models.CharField(max_length=255)
    option = models.ForeignKey(
        ProductOption, on_delete=models.CASCADE, related_name="+"
    )
    variant = models.ForeignKey(
        "ProductVariant", on_delete=models.CASCADE, related_name="+"
    )
    metadata = models.JSONField(null=True)


class ProductTaxRate(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE)
    metadata = models.JSONField(null=True)


class ProductTypeTaxRate(BaseModel):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE)
    metadata = models.JSONField(blank=True, null=True)


class ProductVariantInventoryItem(BaseModel):
    inventory_item_id = models.TextField(unique=True)
    variant_id = models.TextField(unique=True)
    required_quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (("variant_id", "inventory_item_id"),)


class ProductVariant(BaseModel):
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="+")
    sku = models.CharField(max_length=255, null=True, unique=True)
    barcode = models.CharField(max_length=255, null=True, unique=True)
    ean = models.CharField(max_length=255, null=True, unique=True)
    upc = models.CharField(max_length=255, null=True, unique=True)
    variant_rank = models.PositiveIntegerField(default=0)
    inventory_quantity = models.PositiveIntegerField()
    allow_backorder = models.BooleanField(default=False)
    manage_inventory = models.BooleanField(default=True)
    hs_code = models.CharField(max_length=255, null=True)
    origin_country = models.CharField(max_length=255, null=True)
    mid_code = models.CharField(max_length=255, null=True)
    material = models.CharField(max_length=255, null=True)
    weight = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = (("sku", "barcode", "ean", "upc"),)
