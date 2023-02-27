from .auth import *
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


SITE_PROTOCOL = env('SITE_PROTOCOL')
SITE_URL = env("SITE_URL")
