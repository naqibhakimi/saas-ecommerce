from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("POSTGRES_HOST"),
        "port": env("POSTGRES_PORT"),
        "NAME": env("POSTGRES_NAME"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "USER": env("POSTGRES_USER"),
        "ATOMIC_REQUESTS": env("POSTGRES_ATOMIC"),
    }
}
