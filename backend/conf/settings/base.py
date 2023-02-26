"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see©
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import environ


from django.test.signals import setting_changed
from django.conf import settings as django_settings
import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# setup the enviroment

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env(SITE_ID=int, BROKER_URL=str, USE_S3=bool)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8j8k)&0lt3&mg79-=1vdw%y5r_v(^w=qpr^bnl!lm=vl2_1lgg"

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


APPEND_SLASH = True


# GRAPHQL_JWT = {
#     "JWT_VERIFY_EXPIRATION": True,
#     "JWT_AUTH_HEADER_PREFIX": "Bearer",
#     "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
#     "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=9),
#     "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(hours=9),
#     "JWT_ALLOW_ANY_CLASSES": [
#         # "secure_auth.mutations.Register",
#         # "secure_auth.mutations.VerifyAccount",
#         # "secure_auth.mutations.ResendActivationEmail",
#         # "secure_auth.mutations.SendPasswordResetEmail",
#         # "secure_auth.mutations.PasswordReset",
#         # "secure_auth.mutations.ObtainJSONWebToken",
#         # "secure_auth.mutations.VerifyToken",
#         # "secure_auth.mutations.RefreshToken",
#         # "secure_auth.mutations.RevokeToken",
#         # "secure_auth.mutations.VerifySecondaryEmail",
#         # "secure_auth.mutations.SlackAuthCode",
#         # "secure_auth.mutations.VerifySecondaryEmail",
#         # "graphql_social_auth.relay.SocialAuthJWT",
#     ],
# }


# # Auth Backends
# AUTHENTICATION_BACKENDS = [
#     # "graphql_jwt.backends.JSONWebTokenBackend",
#     "apps.auth.backends.GraphQLAuthBackend",
#     "django.contrib.auth.backends.ModelBackend",
# ]


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "graphene_django",
    "django_filters",
    "apps.account",
    "apps.auth",
    "apps.channel",
    "apps.checkout",
    "apps.core",
    "apps.customer",
    "apps.discount",
    "apps.giftcard",
    "apps.inventory",
    "apps.invoice",
    "apps.order",
    "apps.payment",
    "apps.permission",
    "apps.product",
    "apps.shipping",
    "apps.store",
    "apps.tax",
    # third party
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
]

# from django.contrib.auth.middleware import AuthenticationMiddleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conf.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = "conf.wsgi.application"
ASGI_APPLICATION = "conf.asgi.application"


# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#         "ATOMIC_REQUESTS": True,
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True

# SITE_URLS = "localhost"


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # from graphene_django.debug  import DjangoDebugMiddleware
# # Grphene settings
# GRAPHENE = {
#     "SCHEMA": "apps.core.schema.schema",
#     "SCHEMA_OUTPUT": "schema.json",
#     "SCHEMA_INDENT": 2,
#     "MIDDLEWARE": [
#         # "apps.core.middlewares.sentry_middleware.gguncaught_exception_middleware",
#         "graphql_jwt.middleware.JSONWebTokenMiddleware",
#         #  "graphene_django.debug.DjangoDebugMiddleware",
#     ],
# }

# DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
SITE_ID = 1

# CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}


# AUTH_USER_MODEL = "apps_auth.SEUser"


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#         },
#     },
# }


# Email settings
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# AUTH_COFIG = {
#     # if allow to login without verification,
#     # the register mutation will return a token
#     "ALLOW_LOGIN_NOT_VERIFIED": False,
#     # mutations fields options
#     "LOGIN_ALLOWED_FIELDS": ["email"],
#     "ALLOW_LOGIN_WITH_SECONDARY_EMAIL": True,
#     # required fields on register, plus password1 and password2,
#     # can be a dict like UPDATE_MUTATION_FIELDS setting
#     "REGISTER_MUTATION_FIELDS": ["email"],
#     "REGISTER_MUTATION_FIELDS_OPTIONAL": [],
#     # optional fields on update account, can be list of fields
#     "UPDATE_MUTATION_FIELDS": {"first_name": "String", "last_name": "String"},
#     # tokens
#     "EXPIRATION_ACTIVATION_TOKEN": datetime.timedelta(days=7),
#     "EXPIRATION_PASSWORD_RESET_TOKEN": datetime.timedelta(hours=1),
#     "EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN": datetime.timedelta(hours=1),
#     "EXPIRATION_PASSWORD_SET_TOKEN": datetime.timedelta(hours=1),
#     # email stuff
#     "EMAIL_FROM": getattr(django_settings, "DEFAULT_FROM_EMAIL", "test@email.com"),
#     "SEND_ACTIVATION_EMAIL": True,
#     # client: example.com/activate/token
#     "ACTIVATION_PATH_ON_EMAIL": "activate",
#     "ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL": "activate",
#     # client: example.com/password-set/token
#     "PASSWORD_SET_PATH_ON_EMAIL": "password-set",
#     # client: example.com/password-reset/token
#     "PASSWORD_RESET_PATH_ON_EMAIL": "password-reset",
#     # email subjects templates
#     "EMAIL_SUBJECT_ACTIVATION": "email/activation_subject.txt",
#     "EMAIL_SUBJECT_ACTIVATION_RESEND": "email/activation_subject.txt",
#     "EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION": "email/activation_subject.txt",
#     "EMAIL_SUBJECT_PASSWORD_SET": "email/password_set_subject.txt",
#     "EMAIL_SUBJECT_PASSWORD_RESET": "email/password_reset_subject.txt",
#     # email templates
#     "EMAIL_TEMPLATE_ACTIVATION": "email/activation_email.html",
#     "EMAIL_TEMPLATE_ACTIVATION_RESEND": "email/activation_email.html",
#     "EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION": "email/activation_email.html",
#     "EMAIL_TEMPLATE_PASSWORD_SET": "email/password_set_email.html",
#     "EMAIL_TEMPLATE_PASSWORD_RESET": "email/password_reset_email.html",
#     "EMAIL_TEMPLATE_VARIABLES": {},
#     # query stuff
#     "USER_NODE_EXCLUDE_FIELDS": ["password", "is_superuser"],
#     "USER_NODE_FILTER_FIELDS": {
#         "email": ["exact"],
#         "email": ["exact", "icontains", "istartswith"],
#         "is_active": ["exact"],
#         "status__archived": ["exact"],
#         "status__verified": ["exact"],
#         "status__secondary_email": ["exact"],
#     },
#     # turn is_active to False instead
#     "ALLOW_DELETE_ACCOUNT": False,
#     # string path for email function wrapper, see the testproject example
#     "EMAIL_ASYNC_TASK": False,
#     # mutation error type
#     "CUSTOM_ERROR_TYPE": None,
#     # registration with no password
#     "ALLOW_PASSWORDLESS_REGISTRATION": False,
#     "SEND_PASSWORD_SET_EMAIL": False,
# }

# AUTH = type("AUTH", (object,), AUTH_COFIG)


# JWT_AUTH = {
#     "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
#     "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
#     "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_payload_handler",
#     "JWT_SECRET_KEY": SECRET_KEY,
#     "JWT_GET_USER_SECRET_KEY": None,
#     "JWT_PUBLIC_KEY": None,
#     "JWT_PRIVATE_KEY": None,
#     "JWT_ALGORITHM": "HS256",
#     "JWT_VERIFY": True,
#     "JWT_VERIFY_EXPIRATION": True,
#     "JWT_LEEWAY": 0,
#     "JWT_EXPIRATION_DELTA": datetime.timedelta(days=30),
#     "JWT_AUDIENCE": None,
#     "JWT_ISSUER": None,
#     "JWT_ALLOW_REFRESH": True,
#     "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=5),
#     "JWT_AUTH_HEADER_PREFIX": "Bearer",
#     "JWT_AUTH_COOKIE": None,
# }

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
#         },
#     },
#     "handlers": {
#         "console": {
#             "level": "NOTSET",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         },
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": "debug.log",
#         },
#     },
#     "loggers": {
#         "": {
#             "handlers": ["console"],
#             "level": "NOTSET",
#         },
#         "django.request": {
#             "handlers": ["console"],
#             "propagate": False,
#             "level": "ERROR",
#         },
#     },
# }
