from .base import *

GRAPHENE = {
    "SCHEMA": "core.schema.schema",
    "SCHEMA_OUTPUT": "schema.json",
    "SCHEMA_INDENT": 2,
    "MIDDLEWARE": [
        "core.middlewares.CaptureRequestMiddleware",
        "graphene_django.debug.DjangoDebugMiddleware",
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}
