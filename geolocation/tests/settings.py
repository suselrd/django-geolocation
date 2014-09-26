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
GEOLOCATION_DATA_PATH = '../geolocation/tests/data/CUB/'
ADM_DIVISION_MAX_LEVEL = 1

GEOLOCATION_COUNTRY_LEVEL_MAPPING = {
    'id_gadm': 'GADMID',
    'iso': 'ISO',
    'iso2': 'ISO2',
    'name_iso': 'NAME_ISO',
    'name': 'NAME_ENGLI',
    'name_local': 'NAME_LOCAL',
    'name_var': 'NAME_VARIA',
    'name_non_latin': 'NAME_NONLA',
    'valid_from': 'VALIDFR',
    'valid_to': 'VALIDTO',
    'geom': 'MULTIPOLYGON',
}