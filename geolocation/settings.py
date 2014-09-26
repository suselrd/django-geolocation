# coding=utf-8
import os
from django.conf import settings

BASE_DIR = getattr(settings, 'BASE_DIR', os.path.dirname(__file__))

GEOLOCATION_DATA_PATH = getattr(settings, 'GEOLOCATION_DATA_PATH', 'data/')
ADM_DIVISION_MAX_LEVEL = getattr(settings, 'ADM_DIVISION_MAX_LEVEL', 1)
GEOLOCATION_COUNTRY_LEVEL_DATA_PATH = getattr(settings, 'GEOLOCATION_COUNTRY_LEVEL_DATA_PATH', 'adm0.shp')
GEOLOCATION_FIRST_LEVEL_DIVISION_DATA_PATH = getattr(settings, 'GEOLOCATION_FIRST_LEVEL_DIVISION_DATA_PATH', 'adm1.shp')
GEOLOCATION_SECOND_LEVEL_DIVISION_DATA_PATH = getattr(settings, 'GEOLOCATION_SECOND_LEVEL_DIVISION_DATA_PATH', 'adm2.shp')
GEOLOCATION_THIRD_LEVEL_DIVISION_DATA_PATH = getattr(settings, 'GEOLOCATION_THIRD_LEVEL_DIVISION_DATA_PATH', 'adm3.shp')


country_mapping = {
    'id_gadm': 'ID_0',
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
GEOLOCATION_COUNTRY_LEVEL_MAPPING = getattr(settings, 'GEOLOCATION_COUNTRY_LEVEL_MAPPING', country_mapping)


admdivision_1_mapping = {
    'id_gadm': 'ID_1',
    'country_iso': 'ISO',
    'country': {
        'id_gadm': 'ID_0',
    },
    'name': 'NAME_1',
    'name_var': 'VARNAME_1',
    'name_non_latin': 'NL_NAME_1',
    'type': 'TYPE_1',
    'type_en': 'ENGTYPE_1',
    'geom': 'MULTIPOLYGON',
}

GEOLOCATION_FIRST_LEVEL_DIVISION_MAPPING = getattr(settings, 'GEOLOCATION_FIRST_LEVEL_DIVISION_MAPPING', admdivision_1_mapping)

admdivision_2_mapping = {
    'id_gadm': 'ID_2',
    'country_iso': 'ISO',
    'country': {
        'id_gadm': 'ID_0',
    },
    'parent_id_gadm': 'ID_1',
    'name': 'NAME_2',
    'name_var': 'VARNAME_2',
    'name_non_latin': 'NL_NAME_2',
    'type': 'TYPE_2',
    'type_en': 'ENGTYPE_2',
    'geom': 'MULTIPOLYGON',
}

GEOLOCATION_SECOND_LEVEL_DIVISION_MAPPING = getattr(settings, 'GEOLOCATION_SECOND_LEVEL_DIVISION_MAPPING', admdivision_2_mapping)

admdivision_3_mapping = {
    'id_gadm': 'ID_3',
    'country_iso': 'ISO',
    'country': {
        'id_gadm': 'ID_0',
    },
    'parent_id_gadm': 'ID_2',
    'name': 'NAME_3',
    'name_var': 'VARNAME_3',
    'name_non_latin': 'NL_NAME_3',
    'type': 'TYPE_3',
    'type_en': 'ENGTYPE_3',
    'geom': 'MULTIPOLYGON',
}

GEOLOCATION_THIRD_LEVEL_DIVISION_MAPPING = getattr(settings, 'GEOLOCATION_THIRD_LEVEL_DIVISION_MAPPING', admdivision_3_mapping)
