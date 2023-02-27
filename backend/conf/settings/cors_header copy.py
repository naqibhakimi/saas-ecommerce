from .base import *

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = False


CORS_ALLOWED_ORIGIN_REGEXES = [
    r".*",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Headers"
    
]
