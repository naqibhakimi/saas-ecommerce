# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

import datetime

from .base import *

AUTH_USER_MODEL = "secure_auth.SecureUser"

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=9),
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(hours=9),
    "JWT_ALLOW_ANY_CLASSES": [
        "secure_auth.mutations.Register",
        "secure_auth.mutations.VerifyAccount",
        "secure_auth.mutations.ResendActivationEmail",
        "secure_auth.mutations.SendPasswordResetEmail",
        "secure_auth.mutations.PasswordReset",
        "secure_auth.mutations.ObtainJSONWebToken",
        "secure_auth.mutations.VerifyToken",
        "secure_auth.mutations.RefreshToken",
        "secure_auth.mutations.RevokeToken",
        "secure_auth.mutations.VerifySecondaryEmail",
        "secure_auth.mutations.SlackAuthCode",
        "secure_auth.mutations.VerifySecondaryEmail",
        "graphql_social_auth.relay.SocialAuthJWT",
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
    "graphql_jwt.backends.JSONWebTokenBackend",
    "secure_auth.backends.GraphQLAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
    'secure_auth.slack.SlackOAuth2',
    'secure_auth.slack.GoogleOAuth2',
    
]

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

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
    
    
SOCIAL_AUTH_SLACK_KEY = env('SLACK_CLIENT_ID')
SOCIAL_AUTH_SLACK_SECRET = env('SLACK_CLIENT_SECRET')

GOOGLE_RECAPTCHA_SECRET_KEY=env('GOOGLE_RECAPTCHA_SECRET_KEY')

# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.auth_allowed',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
# )
            