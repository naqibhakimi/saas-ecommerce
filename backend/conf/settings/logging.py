from django.utils.log import DEFAULT_LOGGING
from .base import *

LOGLEVEL = env('DJANGO_LOG_LEVEL')


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "NOTSET",
        },
        "django.request": {
            "handlers": ["console"],
            "propagate": False,
            "level": "ERROR",
        },
    },
}
