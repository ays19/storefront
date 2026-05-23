import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['sharar-prod.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQLDB'],
        'USER': os.environ['MYSQLUSER'],
        'PASSWORD': os.environ['MYSQLPASSWORD'],
        'HOST': os.environ['MYSQLHOST'],
        'PORT': os.environ['MYSQLPORT'],
        'CONN_MAX_AGE': 600,
    }
}