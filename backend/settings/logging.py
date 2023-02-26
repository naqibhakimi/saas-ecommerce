from django.utils.log import DEFAULT_LOGGING
from .base import *

LOGLEVEL = env('DJANGO_LOG_LEVEL')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{asctime}: [{levelname}] [{name}] [{module}.{funcName} line: {lineno}]: {message}',
            'style': '{',
        },
        'report': {
            'format': '{asctime}: [{name}.{module}.{funcName} line: {lineno}]: {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
        }
    }
}
