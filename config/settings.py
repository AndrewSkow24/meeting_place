import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8x!^5%_^7&*9(@#1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0p'

DEBUG = True

# Разрешаем все хосты
ALLOWED_HOSTS = ['*']

# Доверенные источники для CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://*.twc1.net',
    'http://*.twc1.net',
    'https://*.apps.timeweb.cloud',
    'https://andrewskow24-meeting-place-46f1.twc1.net',
]

# НАСТРОЙКИ MIDDLEWARE - ДОБАВЛЯЕМ НАШУ ПЕРВОЙ
MIDDLEWARE = [
    'core.middleware.DisableCSRFMiddleware',  # 👈 ЭТА СТРОКА САМАЯ ПЕРВАЯ!
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Остальные настройки
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

ROOT_URLCONF = 'meeting_place.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meeting_place.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [...]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files - создаём папки если их нет
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Безопасно добавляем STATICFILES_DIRS
static_dir = BASE_DIR / 'static'
if not static_dir.exists():
    static_dir.mkdir(parents=True, exist_ok=True)
STATICFILES_DIRS = [static_dir] if static_dir.exists() else []

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'