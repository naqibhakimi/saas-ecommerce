import datetime
from . base import *

AUTH_USER_MODEL = "apps_auth.SEUser"

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=9),
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(hours=9),
    "JWT_ALLOW_ANY_CLASSES": [
        # "apps_auth.mutations.Register",
        # "apps_auth.mutations.VerifyAccount",
        # "apps_auth.mutations.ResendActivationEmail",
        # "apps_auth.mutations.SendPasswordResetEmail",
        # "apps_auth.mutations.PasswordReset",
        # "apps_auth.mutations.ObtainJSONWebToken",
        # "apps_auth.mutations.VerifyToken",
        # "apps_auth.mutations.RefreshToken",
        # "apps_auth.mutations.RevokeToken",
        # "apps_auth.mutations.VerifySecondaryEmail",
        # "apps_auth.mutations.SlackAuthCode",
        # "apps_auth.mutations.VerifySecondaryEmail",
        # "graphql_social_auth.relay.SocialAuthJWT",
    ],
}


JWT_AUTH = {
    "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
    "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
    "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_payload_handler",
    "JWT_SECRET_KEY": SECRET_KEY,
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=30),
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
    "JWT_ALLOW_REFRESH": True,
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=5),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_AUTH_COOKIE": None,
}


# Auth Backends
AUTHENTICATION_BACKENDS = [
    # "graphql_jwt.backends.JSONWebTokenBackend",
    "apps.auth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


AUTH_COFIG = {
    # if allow to login without verification,
    # the register mutation will return a token
    "ALLOW_LOGIN_NOT_VERIFIED": False,
    # mutations fields options
    "LOGIN_ALLOWED_FIELDS": ["email"],
    "ALLOW_LOGIN_WITH_SECONDARY_EMAIL": True,
    # required fields on register, plus password1 and password2,
    # can be a dict like UPDATE_MUTATION_FIELDS setting
    "REGISTER_MUTATION_FIELDS": ["email"],
    "REGISTER_MUTATION_FIELDS_OPTIONAL": [],
    # optional fields on update account, can be list of fields
    "UPDATE_MUTATION_FIELDS": {"first_name": "String", "last_name": "String"},
    # tokens
    "EXPIRATION_ACTIVATION_TOKEN": datetime.timedelta(days=7),
    "EXPIRATION_PASSWORD_RESET_TOKEN": datetime.timedelta(hours=1),
    "EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN": datetime.timedelta(hours=1),
    "EXPIRATION_PASSWORD_SET_TOKEN": datetime.timedelta(hours=1),
    # email stuff
    "EMAIL_FROM": "test@email.com",
    "SEND_ACTIVATION_EMAIL": True,
    # client: example.com/activate/token
    "ACTIVATION_PATH_ON_EMAIL": "activate",
    "ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL": "activate",
    # client: example.com/password-set/token
    "PASSWORD_SET_PATH_ON_EMAIL": "password-set",
    # client: example.com/password-reset/token
    "PASSWORD_RESET_PATH_ON_EMAIL": "password-reset",
    # email subjects templates
    "EMAIL_SUBJECT_ACTIVATION": "email/activation_subject.txt",
    "EMAIL_SUBJECT_ACTIVATION_RESEND": "email/activation_subject.txt",
    "EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION": "email/activation_subject.txt",
    "EMAIL_SUBJECT_PASSWORD_SET": "email/password_set_subject.txt",
    "EMAIL_SUBJECT_PASSWORD_RESET": "email/password_reset_subject.txt",
    # email templates
    "EMAIL_TEMPLATE_ACTIVATION": "email/activation_email.html",
    "EMAIL_TEMPLATE_ACTIVATION_RESEND": "email/activation_email.html",
    "EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION": "email/activation_email.html",
    "EMAIL_TEMPLATE_PASSWORD_SET": "email/password_set_email.html",
    "EMAIL_TEMPLATE_PASSWORD_RESET": "email/password_reset_email.html",
    "EMAIL_TEMPLATE_VARIABLES": {},
    # query stuff
    "USER_NODE_EXCLUDE_FIELDS": ["password", "is_superuser"],
    "USER_NODE_FILTER_FIELDS": {
        "email": ["exact"],
        "email": ["exact", "icontains", "istartswith"],
        "is_active": ["exact"],
        "status__archived": ["exact"],
        "status__verified": ["exact"],
        "status__secondary_email": ["exact"],
    },
    # turn is_active to False instead
    "ALLOW_DELETE_ACCOUNT": False,
    # string path for email function wrapper, see the testproject example
    "EMAIL_ASYNC_TASK": False,
    # mutation error type
    "CUSTOM_ERROR_TYPE": None,
    # registration with no password
    "ALLOW_PASSWORDLESS_REGISTRATION": False,
    "SEND_PASSWORD_SET_EMAIL": False,
}

AUTH = type("AUTH", (object,), AUTH_COFIG)
