from apps.core.forms import BaseForm
from .models import Currency


class CreateCurrencyForm(BaseForm):
    class Meta:
        model = Currency
        fields = (
            "code",
            "symbol",
            "symbol_native",
            "name",
            "includes_tax",
        )


class UpdateCurrencyForm(BaseForm):
    class Meta:
        model = Currency
        fields = (
            'id',
            "code",
            "symbol",
            "symbol_native",
            "name",
            "includes_tax",
        )
