import os


"""
Django settings for myproject project.
Generated by 'django-admin startproject' using Django 4.2.5.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tr8mof9%0e-7g^s6i$_a#$1$3gl=$y_3rk$r**n$pp!p-mc6*@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = [
    '192.168.0.24'
    '127.0.0.1',
    'alex2023alex2023.pythonanywhere.com',
]

INTERNAL_IPS = [
'127.0.0.1',
]


# Application definition

INSTALLED_APPS = [

    'admin_adminlte.apps.AdminAdminlteConfig',         #для работы  плагина на изменение  админки
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'myapp2',
    'games_app',
    'games2_app',
    'blog_app',
    'debug_toolbar',
]

MIDDLEWARE = [

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGGING = {
    'version': 1,                               # версия логирования
    'disable_existing_loggers': False,          #сохранение предыдущих логов
    'formatters': {                             # настройка вида - формата логирования на выбор simple Или verbose
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {                               # обрабочики - где выводить логи
        'console': {                            # вывод в консоль
            'class': 'logging.StreamHandler',
            'formatter': 'verbose', # добавлен параметр formatter
        },
        'file': {                               # вывод в файл
            'class': 'logging.FileHandler',
            'filename': './log/django.log',                 #создаст файл изапишет туда логи
            'formatter': 'verbose',              # указываем формат verbose
            'encoding': 'utf-8'                 # чтобы в файле отображалась кириллица
        },
    },
    'loggers': {                            #инициализация логов
        'django': {                         #для Dj логов используем вывод в консоль и файл
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'games_app': {                      # для логов приложения games_app используем вывод в консоль и файл
            'handlers': ['console', 'file'],
            'level': 'INFO',                # записываются у=урони логов от info и выше
            'propagate': True,
        },
        'myapp': {                      # для логов приложения my_app используем вывод в консоль и файл
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# для работы  плагина на изменение  админки
LOGIN_REDIRECT_URL = "/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


