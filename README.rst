==========================
Django Geolocation
==========================

Geolocation for Django>=1.6.1

Imports and manage spatial data.


Changelog
=========
0.1.0
-----

PENDING...

Notes
-----

PENDING...

Usage
-----

1. Run ``python setup.py install`` to install.

2. Modify your Django settings to use ``geolocation``:

3. Configure your geolocation related settings:
    BASE_DIR: Base directory for the django project (where the main settings file is located)
    GEOLOCATION_DATA_PATH: spatial data folder path (relative to BASE_DIR)
    ADM_DIVISION_MAX_LEVEL: max level for administrative divisions, according to the amount of spatial data.
    GEOLOCATION_COUNTRY_LEVEL_DATA_PATH: country level shapefile path (relative to GEOLOCATION_DATA_PATH)
    GEOLOCATION_FIRST_LEVEL_DIVISION_DATA_PATH: first level administrative division shapefile path (relative to GEOLOCATION_DATA_PATH)
    GEOLOCATION_SECOND_LEVEL_DIVISION_DATA_PATH: second level administrative division shapefile path (relative to GEOLOCATION_DATA_PATH)
    GEOLOCATION_THIRD_LEVEL_DIVISION_DATA_PATH: third level administrative division shapefile path (relative to GEOLOCATION_DATA_PATH)

4. Execute manage.py loadspatialdata command