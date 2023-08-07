from .models import Image, MoneyAmount, PriceList, Product, ProductCategory, ProductCollection, ProductOption, ProductOptionValue, ProductTag, ProductTaxRate, ProductType
from apps.core.forms import BaseForm


class CreateProductFrom(BaseForm):
    class Meta:
        model = Product
        fields = (
            "title",
            "subtitle",
            "description",
            "handle",
            "is_gift_card",
            "status",
            "images",
            "thumbnail",
            "profile",
            "weight",
            "length",
            "height",
            "width",
            "hs_code",
            "origin_country",
            "mid_code",
            "material",
            "collection",
            "type",
            "tags",
            "discountable",
            "external_id",
            "sales_channels",
            "each_unit_count",
            "unit_count",
            "unit_count_type",
            "is_expirable",
            "metadata"
        )


class UpdateProductFrom(BaseForm):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "subtitle",
            "description",
            "handle",
            "is_gift_card",
            "status",
            "images",
            "thumbnail",
            "profile",
            "weight",
            "length",
            "height",
            "width",
            "hs_code",
            "origin_country",
            "mid_code",
            "material",
            "collection",
            "type",
            "tags",
            "discountable",
            "external_id",
            "sales_channels",
            "each_unit_count",
            "unit_count",
            "unit_count_type",
            "is_expirable",
            "metadata"
        )


class CreatePriceListFrom(BaseForm):
    class Meta:
        model = PriceList
        fields = "__all__"


class UpdatePriceListForm(BaseForm):
    class Meta:
        model = PriceList
        fields = (
            "id",
            "name",
            "description",
            "type",
            "status",
            "starts_at",
            "ends_at",
            # "customer_groups",
            "includes_tax"
        )


class CreateMoneyAmountForm(BaseForm):
    class Meta:
        model = MoneyAmount
        fields = (
            "currency",
            "amount",
            "min_quantity",
            "max_quantity",
            "price_list",
            "variant",
            "region",
        )


class UpdateMoneyAmountForm(BaseForm):
    class Meta:
        model = MoneyAmount
        fields = (
            "id",
            "currency",
            "amount",
            "min_quantity",
            "max_quantity",
            "price_list",
            "variant",
            "region",
        )


class CreateProductTypeForm(BaseForm):
    class Meta:
        model = ProductType
        fields = (
            "value",
            "metadata"
        )


class UpdateProductTypeForm(BaseForm):
    class Meta:
        model = ProductType
        fields = (
            "id",
            "value",
            "metadata",
        )


class CreateProductTagForm(BaseForm):
    class Meta:
        model = ProductTag
        fields = (
            "value",
            "metadata"
        )


class UpdateProductTagForm(BaseForm):
    class Meta:
        model = ProductTag
        fields = (
            "id",
            "value",
            "metadata"
        )


class CreateImageForm(BaseForm):
    class Meta:
        model = Image
        fields = (
            "file",
            "metadata"
        )


class UpdateImageForm(BaseForm):
    class Meta:
        model = Image
        fields = (
            "id",
            "file",
            "metadata"
        )


class CreateProductCollectionForm(BaseForm):
    class Meta:
        model = ProductCollection
        fields = (
            "title",
            "handle",
            "metadata"
        )


class UpdateProductCollectionForm(BaseForm):
    class Meta:
        model = ProductCollection
        fields = (
            "id",
            "title",
            "handle",
            "metadata"
        )


class CreateProductCategoryForm(BaseForm):
    class Meta:
        model = ProductCategory
        fields = (
            "name",
            "handle",
            "is_active",
            "is_internal",
            "parent_category",
        )


class UpdateProductCategoryForm(BaseForm):
    class Meta:
        model = ProductCategory
        fields = (
            "id",
            "name",
            "handle",
            "is_active",
            "is_internal",
            "parent_category",
        )


class CreateProductOptionForm(BaseForm):
    class Meta:
        model = ProductOption
        fields = (
            "title",
            "product",
            "metadata",
        )


class UpdateProductOptionForm(BaseForm):
    class Meta:
        model = ProductOption
        fields = (
            "id",
            "title",
            "product",
            "metadata",
        )


class CreateProductOptionValueForm(BaseForm):
    class Meta:
        model = ProductOptionValue
        fields = (
            "value",
            "option",
            "variant",
            "metadata",
        )


class UpdateProductOptionValueForm(BaseForm):
    class Meta:
        model = ProductOptionValue
        fields = (
            "id",
            "value",
            "option",
            "variant",
            "metadata",
        )


class CreateProductTaxRateForm(BaseForm):
    class Meta:
        model = ProductTaxRate
        fields = (
            "tax_rate",
            "metadata",
        )


class UpdateProductTaxRateForm(BaseForm):
    class Meta:
        model = ProductTaxRate
        fields = (
            "id",
            "tax_rate",
            "metadata",
        )


class CreateProductTypeTaxRateForm(BaseForm):
    class Meta:
        fields = (
            "product_type",
            "tax_rate",
            "metadata",
        )


class UpdateProductTypeTaxRateForm(BaseForm):
    class Meta:
        fields = (
            "id",
            "product_type",
            "tax_rate",
            "metadata",
        )


class CreateVariantInventoryItemForm(BaseForm):
    class Meta:
        fields = (
            "inventory_item_id",
            "variant_id",
            "required_quantity",
        )


class UpdateVariantInventoryItemForm(BaseForm):
    class Meta:
        fields = (
            "id",
            "inventory_item_id",
            "variant_id",
            "required_quantity",
        )


class CreateProductVariantForm(BaseForm):
    class Meta:
        fields = (
            "title",
            "product",
            "sku",
            "barcode",
            "ean",
            "upc",
            "variant_rank",
            "inventory_quantity",
            "allow_back_order",
            "manage_inventory",
            "hs_code",
            "origin_country",
            "mid_code",
            "material",
            "weight",
            "length",
            "height",
            "width",
            "metadata",
        )


class UpdateProductVariantForm(BaseForm):
    class Meta:
        fields = (
            "id",
            "title",
            "product",
            "sku",
            "barcode",
            "ean",
            "upc",
            "variant_rank",
            "inventory_quantity",
            "allow_back_order",
            "manage_inventory",
            "hs_code",
            "origin_country",
            "mid_code",
            "material",
            "weight",
            "length",
            "height",
            "width",
            "metadata",
        )
