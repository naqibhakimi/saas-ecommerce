from django.db import models
from apps.core.models import BaseModel
from apps.customer.models import  Region
from apps.product.models import Product, ProductType, ProductTag, ProductCollection
from apps.customer.models import CustomerGroup


class DiscountCondition(BaseModel):
    Discount_Condition_Type = (
        ("products", "PRODUCTS"),
        ("product_types", "PRODUCT_TYPES"),
        ("product_collections", "PRODUCT_COLLECTIONS"),
        ("product_tags", "PRODUCT_TAGS"),
        ("customer_groups", "CUSTOMER_GROUPS")
    )

    Discount_Condition_Operator = (
        ("in", "IN"),
        ("not_in", "NOT_IN"),
    )
    type = models.CharField(
        max_length=20,
        choices=Discount_Condition_Type
        )
    operator = models.CharField(
        max_length=20,
        choices=Discount_Condition_Operator
        )
    discount_rule = models.ForeignKey(
        'DiscountRule',
        on_delete=models.CASCADE,
        related_name='+'
        )
    products = models.ManyToManyField(
        Product,
        through='DiscountConditionProduct',
        )
    product_types = models.ManyToManyField(
        ProductType,
        through='DiscountConditionProductType',
        )
    product_tags = models.ManyToManyField(
        ProductTag,
        through='DiscountConditionProductTag',
        )
    product_collections = models.ManyToManyField(
        "ProductCollection",
        through='DiscountConditionProductCollection',
        )
    customer_groups = models.ManyToManyField(
        CustomerGroup,
        through='DiscountConditionCustomerGroup',
        )
    metadata = models.JSONField(null=True)



class DiscountRule(BaseModel):
    Discount_Rule_Type = (
        ("fixed", "FIXED"),
        ("percentage", "PERCENTAGE"),
        ("free_shipping", "FREE_SHIPPING"),
    )

    Allocation_Type = (
        ("total", "TOTAL"),
        ("item", "ITEM"),
    )
    description = models.CharField(max_length=255, null=True)
    type = models.CharField(choices=Discount_Rule_Type, max_length=20)
    value = models.FloatField()
    allocation = models.CharField(choices=Allocation_Type, max_length=20, null=True)
    conditions = models.ManyToManyField(DiscountCondition, related_name='+')
    metadata = models.JSONField(null=True)

class Discount(BaseModel):
    code = models.CharField(max_length=255, unique=True)
    is_dynamic = models.BooleanField()
    rule = models.ForeignKey(DiscountRule, on_delete=models.CASCADE, null=True, related_name='+')
    is_disabled = models.BooleanField()
    parent_discount = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    starts_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    valid_duration = models.CharField(max_length=255, null=True, blank=True)
    regions = models.ManyToManyField(Region, related_name='+')
    usage_limit = models.IntegerField(null=True, blank=True)
    usage_count = models.IntegerField(default=0)
    metadata = models.JSONField(null=True, blank=True)



class DiscountConditionCustomerGroup(BaseModel):
    customer_group = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(null=True, blank=True)




class DiscountConditionProductCollection(BaseModel):
    product_collection = models.ForeignKey(ProductCollection, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE)
    metadata = models.JSONField(null=True)


class DiscountConditionProductTag(BaseModel):
    product_tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE)
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name='+' )
    metadata = models.JSONField(null=True, blank=True)




class DiscountConditionProductType(BaseModel):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='+')
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product_type", "discount_condition"),)




class DiscountConditionProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    discount_condition = models.ForeignKey(DiscountCondition, on_delete=models.CASCADE, related_name='+')
    metadata = models.JSONField(null=True)

    class Meta:
        unique_together = (("product", "discount_condition"),)




