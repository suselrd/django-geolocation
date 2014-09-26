# coding=utf-8
import os

DEBUG = True

SITE_ID = 1

SECRET_KEY = 'blabla'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.gis',
    'south',
    'geolocation',
    'geolocation.tests'
]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# GEOLOCATION DATA
GEOLOCATION_DATA_PATH = '../geolocation/tests/data/MEX/'
ADM_DIVISION_MAX_LEVEL = 2
