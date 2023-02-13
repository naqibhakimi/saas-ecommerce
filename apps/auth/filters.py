import django_filters
from django.contrib.auth import get_user_model
from .models import SEUser, UserStatus


class SEUserFilter(django_filters.FilterSet):
    search_fields = "__all__"

    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserStatusFilter(django_filters.FilterSet):
    class Meta:
        model = UserStatus
        fields = "__all__"
