import django_filters
from django.contrib.auth import get_user_model
from core.utils import check_id

from .models import Company, LogAttempts, Profile, SecureUser, UserEmailLog


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = get_user_model()
        exclude = ('metadata')


# class CompanyUsersMixin(django_filters.FilterSet):
#     company = django_filters.CharFilter(method="filter_by_company")

#     def filter_by_company(self, queryset, name, value):
#         return queryset.filter(employee=check_id(value))
    

# class SecureUserFilter(CompanyUsersMixin, django_filters.FilterSet):
#     search_fields = "__all__"

#     class Meta:
#         model = SecureUser
#         fields = "__all__"
class SEUserFilter(django_filters.FilterSet):
    search_fields = "__all__"

    class Meta:
        model = SecureUser
        fields = "__all__"


# class CompanyFilter(django_filters.FilterSet):
#     search_fields = "__all__"

#     class Meta:
#         model = Company
#         fields = "__all__"
#         exclude = ["company_logo"]


# class ProfileFilter(django_filters.FilterSet):
#     search_fields = "__all__"

#     class Meta:
#         model = Profile
#         fields = "__all__"


class LogAttemptsFilter(django_filters.FilterSet):
    search_fields = "__all__"

    class Meta:
        model = LogAttempts
        fields = "__all__"


class UserEmailLogFilter(django_filters.FilterSet):
    search_fields = "__all__"

    class Meta:
        model = UserEmailLog
        fields = "__all__"
