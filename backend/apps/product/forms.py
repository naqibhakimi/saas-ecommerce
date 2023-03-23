from .models import PriceList, Product
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
