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
