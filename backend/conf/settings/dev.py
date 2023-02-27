from .auth import *
from .base import *
from .cors_header import *
from .database import *
from .email import *
from .graphene import *
from .i18n import *
from .media import *
from .static import *
from .template import *
from .logging import *
from .template import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


AUTH_USER_MODEL = "secure_auth.SecureUser"

SITE_PROTOCOL = env('SITE_PROTOCOL')
SITE_URLS = env("SITE_URLS")
