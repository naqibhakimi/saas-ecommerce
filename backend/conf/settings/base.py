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

from pathlib import Path


DEBUG = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# setup the enviroment

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
env = environ.Env(SITE_ID=int, BROKER_URL=str, USE_S3=bool)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = env("SECRET_KEY")

# # SECURITY WARNING: don't run with debug turned on in production!


APPEND_SLASH = True


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
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conf.urls"

WSGI_APPLICATION = "conf.wsgi.application"
ASGI_APPLICATION = "conf.asgi.application"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1
