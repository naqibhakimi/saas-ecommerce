from .base import *
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC_REQUESTS": True,
    },
    "read_only": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "read_only_db.sqlite3",
        "ATOMIC_REQUESTS": True,
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "HOST": env("POSTGRES_HOST"),
#         "port": env("POSTGRES_PORT"),
#         "NAME": env("POSTGRES_NAME"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "USER": env("POSTGRES_USER"),
#         "ATOMIC_REQUESTS": env("POSTGRES_ATOMIC"),
#     }
# }
