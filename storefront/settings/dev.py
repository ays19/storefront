from .common import *


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-13p)axebk7x&91cylaxo*+6rnid%vtozwig+mnurj4!-x7#eq('

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'USER': 'root',
        'PASSWORD': 'Ays19@Ubuntu26',
        'HOST': 'localhost',
        'PORT': '3306',
        'CONN_MAX_AGE': 600,
    }
}

CELERY_BROKER_URL   = 'redis://localhost:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        'TIMEOUT': 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
