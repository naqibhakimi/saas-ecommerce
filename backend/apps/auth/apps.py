from django.apps import AppConfig


class SeAuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.auth"
    label = "apps_auth"

    def ready(self) -> None:
        import apps.auth.signals

        return super().ready()
