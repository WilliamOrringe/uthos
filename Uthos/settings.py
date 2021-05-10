"""
Django settings for Uthos project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# get the real secret key from environment variables
# or use the alternative (only in local development)
SECRET_KEY = os.getenv(
    "DJANGO_4UMS_SECRET_KEY",
    "afk0df';>j34SD+[.;'/*&^%)*FAjkd@';oxj8ff33=Lnakfj&",
)

# settings that require deployment
if "DJANGO_AWS_4UMS_DEPLOYED" in os.environ:
    ALLOWED_HOSTS = ["4ums.co.uk"]
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    DEBUG = False
else:
    ALLOWED_HOSTS = ["*"]
    DEBUG = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "backend",
    "frontend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Uthos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "frontend/build/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "SoftwareDev.wsgi.application"

# Logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": os.getenv(
                "LOG_FILE_PATH", os.path.join(BASE_DIR, "django.log")
            ),
            "encoding": "utf-8",
            "formatter": "simple",
        },
    },
    "formatters": {
        "simple": {
            "format": "{asctime} - [{levelname}] {message}",
            "style": "{",
        }
    },
    "loggers": {
        "root": {
            "handlers": ["file"],
            "level": os.getenv("LOG_LEVEL", "INFO"),
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(os.path.join(BASE_DIR, "db.sqlite3")),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "public/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend/build/static")]


# Override the default user model.

AUTH_USER_MODEL = "backend.User"


# Point values.

LIKE_POST_PTS = 50  # Points gained when someone likes your post
LIKE_COMMENT_PTS = 60  # Points gained when someone likes a comment on your post
MAKE_COMMENT_PTS = 10  # Points gained when someone makes a comment on your post
CHOOSE_CORRECT_ANSWER_PTS = 20  # Points gained when you approve an answer
CORRECT_ANSWER_PTS = 200  # Points gained when your answer gets approved
JOIN_COMMUNITY_PTS = 10  # Points gained when someone joins your community
