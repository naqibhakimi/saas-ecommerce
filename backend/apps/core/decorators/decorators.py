from functools import wraps
from typing import Callable

from graphql import GraphQLError

from apps.core.middlewares import thread_local


def add_info(fn) -> Callable:
    @wraps(fn)
    def wrapper(info, root, *args, **kwargs):
        return fn(info=thread_local.info, root=thread_local.root, *args, **kwargs)

    return wrapper


def login_required_property(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = thread_local.info.context.user
        info = thread_local.info
        root = thread_local.root
        if not user.is_authenticated:
            raise GraphQLError(message="Unauthenticated")
        return fn(info, root, *args, **kwargs)

    return wrapper
