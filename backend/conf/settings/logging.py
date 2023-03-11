from django.utils.log import DEFAULT_LOGGING
from .base import *

LOGLEVEL = env('DJANGO_LOG_LEVEL')


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(name)s %(module)s %(process)d %(thread)d %(message)s",
            "use-color": True,
        },
        "debug": {
            "format": "%(levelname)s %(asctime)s %(name)s %(module)s %(process)d %(thread)d %(message)s",
            "use-color": True,
        },
    },
    "handlers": {
        "dev": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "prod": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "": {
            "handlers": ["dev"],
            "propagate": True,
            "level": "INFO",
        },
        "daphne.server": {
            "handlers": ["dev"],
            "propagate": True,
            "level": "NOTSET",
        },
    },
}
