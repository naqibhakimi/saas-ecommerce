from .base import *

GRAPHENE = {
    "SCHEMA": "apps.core.schema.schema",
    "SCHEMA_OUTPUT": "schema.json",
    "SCHEMA_INDENT": 2,
    "MIDDLEWARE": [
        # "apps.core.middlewares.sentry_middleware.gguncaught_exception_middleware",
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
        #  "graphene_django.debug.DjangoDebugMiddleware",
    ],
}
