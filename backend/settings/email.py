from .base import *

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

# EMAIL_HOST = "email-smtp.us-west-2.amazonaws.com"
# EMAIL_HOST_USER = "AKIA25QZGX7YMEKPSXCJ"
# EMAIL_HOST_PASSWORD = "BOzFt10+tz7y62O3PZc2FEhNn8IIo8udNZXdkvYuQT8B"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = "admin@encryptsecrets.com"
# FROM_EMAIL = "admin@encryptsecrets.com"
# TO_EMAIL = "admin@encryptsecrets.com"


EMAIL_HOST=env('EMAIL_HOST')
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_USE_TLS=env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL=env('DEFAULT_FROM_EMAIL')
FROM_EMAIL=env('FROM_EMAIL')
TO_EMAIL=env('TO_EMAIL')