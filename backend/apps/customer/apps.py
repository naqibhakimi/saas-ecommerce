from django.apps import AppConfig


class CustomerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.customer"

    def ready(self) -> None:
        import apps.customer.signals
        return super().ready()
