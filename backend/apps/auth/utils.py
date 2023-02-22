from django.core import signing
from django.conf import settings as django_settings

from . exceptions import TokenScopeError


def get_token_payload(token, action, exp=None):
    payload = signing.loads(token, max_age=exp)
    _action = payload.pop("action")
    if _action != action:
        raise TokenScopeError
    return payload


def using_refresh_tokens():
    if (
        hasattr(django_settings, "GRAPHQL_JWT")
        and django_settings.GRAPHQL_JWT.get("JWT_LONG_RUNNING_REFRESH_TOKEN", False)
        and "graphql_jwt.refresh_token.apps.RefreshTokenConfig"
        in django_settings.INSTALLED_APPS
    ):
        return True
    return False


def revoke_user_refresh_token(user):
    if using_refresh_tokens():
        refresh_tokens = user.refresh_tokens.all()
        for refresh_token in refresh_tokens:
            try:
                refresh_token.revoke()
            except Exception:  # JSONWebTokenError
                pass
