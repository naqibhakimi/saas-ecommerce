import django_filters

from .models import Address

class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields = '__all__'
    