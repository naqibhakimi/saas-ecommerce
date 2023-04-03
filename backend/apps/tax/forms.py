from apps.core.forms import BaseForm
from .models import TaxRate


class CreateTaxRateForm(BaseForm):
    class Meta:
        model = TaxRate
        fields = (
            "rate",
            "code",
            "name",
            # "metadata",
            "product_count",
            "product_type_count",
            "shipping_option_count",
        )


class UpdateTaxRateForm(BaseForm):
    class Meta:
        model = TaxRate
        fields = (
            "id",
            "rate",
            "code",
            "name",
            # "metadata",
            "product_count",
            "product_type_count",
            "shipping_option_count",
        )
