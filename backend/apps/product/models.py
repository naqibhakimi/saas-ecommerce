from django.db import models

from apps.core.models import BaseModel
from apps.store.models import SalesChannel
from apps.tax.models import TaxRate
from apps.shipping.models import ShippingProfile


class PriceList(BaseModel):
    """Price Lists represents a set of prices that overrides the
        default price for one or more product variants.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, default="sale")
    status = models.CharField(max_length=255, default="draft")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    # description: The Customer Groups that the Price List applies to. Available if the relation `customer_groups` is expanded.
    customer_groups = models.ManyToManyField("customer.CustomerGroup", related_name="+")
    includes_tax = models.BooleanField(default=False)


class MoneyAmount(BaseModel):
    """

    The PriceList model can be used to set different prices for product variants depending
    on the price list. For example, you could have a price list for wholesale
    customers and a price list for retail customers.

    You can use the PriceList model to set different prices for product variants
    in different regions or for different customer groups.

    currency: The currency code for the price.
    amount: The price amount.
    min_quantity: The minimum quantity for the price to apply.
    max_quantity: The maximum quantity for the price to apply.
    region: The region for the price.
    customer_group: The customer group for the price.
    """

    # todo:
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
    """
    For example, let's say you have an online clothing store. 
    You might have the following product collections:

    "Summer Collection": This collection includes all the clothing items that are
    suitable for summer, such as shorts, tank tops, and sundresses.

    "Winter Sale": This collection includes all the clothing items that are part
    of the winter clearance sale.

    "Women's Accessories": This collection includes various accessories 
    like handbags, scarves, and hats tasrgeted specifically for women.
    """
    title = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True, null=True)
    # products = models.ManyToManyField(Product, related_name="+")
    metadata = models.JSONField(null=True)


class Product(BaseModel):
    """
    Product Title: "Premium Smartphone"
    Subtitle: "Powerful Performance and Stunning Display"
    Description: "This premium smartphone combines cutting-edge technology
                    with a sleek design to deliver an exceptional user experience."

    handle:  means slug -> Premium-Smartphone
    MID code:  stands for Manufacturer Identification Code. It is a 13-digit code that
        is used to identify the manufacturer of a product.
        MID codes are used by customs authorities to track 
        the movement of goods across borders.
    HS code:  stands for Harmonized System code. It is a 6-digit code
        that is used to classify products for customs purposes. HS codes are 
        used to determine the tariff rates that will be applied to goods when they
        are imported or exported.

    is_gift_card: field in the code you provided is a Boolean field that indicates whether 
        or not the product is a gift card. If the field is set to True, 
        then the product will be treated as a gift card. 
        This means that the product will not be physically shipped to the customer, 
        but rather, the customer will receive a code that they can redeem for the product.

        is_gift_card field can be used to distinguish between gift cards and regular products.
        This is important for a number of reasons. For example, gift cards may need to
        be handled differently in the checkout process, and they may
        need to be displayed differently on the website.

    external_id: allows storing an external identifier for a product. 
        An external identifier is a unique code or reference number that 
        is used to identify the product within an external system or integration.

        By using external_id, the e-commerce platform can communicate with external
        systems more effectively and keep track of the product's associations
        and mappings across different platforms. It simplifies the data 
        synchronization process and allows for smooth 
        interoperability between various systems.

    sales_channels: is useful if you want to track the sales of your products
        across different channels. For example, you could use the sales_channels
        field to track the number of products sold on your website,
        in physical stores, and through third-party marketplaces.

        Let's say that you are selling a smartphone on your online store.
        You want to track the sales of the smartphone on your website and through Amazon.
        You would create two sales channels, one for your website and one for Amazon.
        You would then associate the smartphone with both sales channels.
        When a customer purchases the smartphone from your website, 
        the sale would be recorded in the sales channel for your website.
        When a customer purchases the smartphone from Amazon, 
        the sale would be recorded in the sales channel for Amazon.
        This would allow you to track the sales of the smartphone across both channels
        and see which channel is generating more sales.


    """
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
    # FIXME: DO WE HAVE TO REMOVE IMAGES
    images = models.ManyToManyField(Image, related_name="+")
    thumbnail = models.ImageField(upload_to="Product/Thumbnail", null=True, blank=True)
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
    # This field holds the count of each unit in a product (e.g., 10 units per package).
    each_unit_count = models.PositiveIntegerField(null=True, blank=True)
    #  This field represents the total count of units in the product (e.g., 100 units in total).
    unit_count = models.PositiveIntegerField(null=True, blank=True)
    # This field specifies the type of unit count (e.g., "per package," "per box, ounce" etc.).
    unit_count_type = models.CharField(max_length=50, null=True, blank=True)
    is_expirable = models.BooleanField(default=False)
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
    allow_back_order = models.BooleanField(default=False)
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
