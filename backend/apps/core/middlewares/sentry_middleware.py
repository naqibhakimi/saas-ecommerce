import logging
import graphql

logger = logging.getLogger(__name__)


def log_error(error):
    logger.error(error)  # we've set this up to send issues to sentry
    raise graphql.GraphQLError("An internal error occurred")


def gguncaught_exception_middleware(next, root, info, **args):
    print(next, root, info, args)
    return next(root, info, **args).catch(log_error)


from time import time as timer


def uncaught_exception_middleware(next, root, info, **args):
    start = timer()
    return_value = next(root, info, **args)
    duration = round((timer() - start) * 1000, 2)
    parent_type_name = root._meta.name if root and hasattr(root, "_meta") else ""
    logger.debug(f"{parent_type_name}.{info.field_name}: {duration} ms")
    return return_value


# class SentryMiddleware(object):
#     """
#     Properly capture errors during query execution and send them to Sentry.
#     Then raise the error again and let Graphene handle it.
#     """

#     def on_error(self, error):
#         print(error)
#         raise error

#     def resolve(self, next, root, info, **args):
#        return next(root, info, **args).catch(self.on_error)
