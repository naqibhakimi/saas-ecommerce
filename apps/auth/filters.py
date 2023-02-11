import django_filters
from django.contrib.auth import get_user_model
class SEUserFilter(django_filters.FilterSet):
    search_fields = "__all__"

    class Meta:
        model =  get_user_model()
        fields = "__all__"