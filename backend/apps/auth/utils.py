from django.core import signing
from .exceptions import TokenScopeError


def get_token_payload(token, action, exp=None):
    payload = signing.loads(token, max_age=exp)
    _action = payload.pop("action")
    if _action != action:
        raise TokenScopeError
    return payload
