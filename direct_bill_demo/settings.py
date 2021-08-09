"""Django and other settings for the direct_bill_demo service."""

import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

SECRET_KEY = "some fake secret key"

ALLOWED_HOSTS = ["*"]

APPEND_SLASH = False

INSTALLED_APPS = [
    "sslserver",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "checkout",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "direct_bill_demo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [f"{BASE_DIR}/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        },
    }
]

WSGI_APPLICATION = "direct_bill_demo.wsgi.application"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

USE_TZ = True
TIME_ZONE = "UTC"

USE_I18N = False
USE_L10N = False

STATIC_URL = "/static/"
STATIC_ROOT = "/tmp/staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

BOOST_API_URL = os.environ["BOOST_API_URL"]
BOOST_API_AUTHORIZATION_TOKEN = os.environ["BOOST_API_AUTHORIZATION_TOKEN"]
BOOST_USER_HEADER = os.environ["BOOST_USER_HEADER"]
STRIPE_PUBLISHABLE_KEY = os.environ["STRIPE_PUBLISHABLE_KEY"]
