# from functools import wraps

# from .constants import Messages
# from .exceptions import WrongUsage


# def login_required(fn):
#     @wraps(fn)
#     def wrapper(cls, root, info, **kwargs):
#         user = info.context.user
#         if not user.is_authenticated:
#             return cls(success=False, errors=Messages.UNAUTHENTICATED)
#         return fn(cls, root, info, **kwargs)

#     return wrapper


# def verification_required(fn):
#     @wraps(fn)
#     @login_required
#     def wrapper(cls, root, info, **kwargs):
#         user = info.context.user
#         if not user.status.verified:
#             return cls(success=False, errors=Messages.NOT_VERIFIED)
#         return fn(cls, root, info, **kwargs)

#     return wrapper
