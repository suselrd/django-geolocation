# coding=utf-8
import os
from django.contrib.gis.gdal import OGRException
from django.contrib.gis.utils import LayerMapping
from django.contrib.sites.models import Site
from django.db.models.signals import pre_save
from .settings import (
    BASE_DIR,
    GEOLOCATION_DATA_PATH,
    ADM_DIVISION_MAX_LEVEL,
    GEOLOCATION_COUNTRY_LEVEL_DATA_PATH,
    GEOLOCATION_FIRST_LEVEL_DIVISION_DATA_PATH,
    GEOLOCATION_SECOND_LEVEL_DIVISION_DATA_PATH,
    GEOLOCATION_THIRD_LEVEL_DIVISION_DATA_PATH,
    GEOLOCATION_COUNTRY_LEVEL_MAPPING,
    GEOLOCATION_FIRST_LEVEL_DIVISION_MAPPING,
    GEOLOCATION_SECOND_LEVEL_DIVISION_MAPPING,
    GEOLOCATION_THIRD_LEVEL_DIVISION_MAPPING
)
from .models.areas import Country, AdmDivision


COUNTRY_SHP = os.path.abspath(os.path.join(BASE_DIR, '%s/%s' % (GEOLOCATION_DATA_PATH, GEOLOCATION_COUNTRY_LEVEL_DATA_PATH)))
FIRST_LEVEL_DIVISION_SHP = os.path.abspath(os.path.join(BASE_DIR, '%s/%s' % (GEOLOCATION_DATA_PATH, GEOLOCATION_FIRST_LEVEL_DIVISION_DATA_PATH)))
SECOND_LEVEL_DIVISION_SHP = os.path.abspath(os.path.join(BASE_DIR, '%s/%s' % (GEOLOCATION_DATA_PATH, GEOLOCATION_SECOND_LEVEL_DIVISION_DATA_PATH)))
THIRD_LEVEL_DIVISION_SHP = os.path.abspath(os.path.join(BASE_DIR, '%s/%s' % (GEOLOCATION_DATA_PATH, GEOLOCATION_THIRD_LEVEL_DIVISION_DATA_PATH)))


def fix_adm1_before_save(instance, raw, using, update_fields, **kwargs):
    instance.level = 1


def fix_adm2_before_save(instance, raw, using, update_fields, **kwargs):
    instance.level = 2
    try:
        instance.parent = AdmDivision.objects.get(country_iso=instance.country_iso,
                                                  level=1,
                                                  site=Site.objects.get_current(),
                                                  id_gadm=instance.parent_id_gadm)
    except AdmDivision.MultipleObjectsReturned:
        options = list(AdmDivision.objects.filter(country_iso=instance.country_iso,
                                             level=1,
                                             site=Site.objects.get_current(),
                                             id_gadm=instance.parent_id_gadm))

        print(" Multiple objects matching query for AdmDivision object's parent")
        print(" Child: %s" % instance)
        print(" Possible parents: ")
        count = 0
        for option in options:
            count += 1
            print (" %d - %s" % (count, option))

        while (True):
            choice = raw_input(" ? Please select a choice: ")
            try:
                choice = int(choice)
                assert choice >= 1
                assert choice <= count
                break
            except (ValueError, AssertionError):
                print(" ! Invalid choice.")

        instance.parent = options[choice-1]


def fix_adm3_before_save(instance, raw, using, update_fields, **kwargs):
    instance.level = 3
    try:
        instance.parent = AdmDivision.on_site.get(country_iso=instance.country_iso,
                                                  level=2,
                                                  site=Site.objects.get_current(),
                                                  id_gadm=instance.parent_id_gadm)
    except AdmDivision.MultipleObjectsReturned:
        options = list(AdmDivision.on_site.filter(country_iso=instance.country_iso,
                                                  level=2,
                                                  site=Site.objects.get_current(),
                                                  id_gadm=instance.parent_id_gadm))

        print(" Multiple objects matching query for AdmDivision object's parent")
        print(" Child: %s" % instance)
        print(" Possible parents: ")
        count = 0
        for option in options:
            count += 1
            print (" %d - %s" % (count, option))

        while (True):
            choice = raw_input(" ? Please select a choice: ")
            try:
                choice = int(choice)
                assert choice >= 1
                assert choice <= count
                break
            except (ValueError, AssertionError):
                print(" ! Invalid choice.")

        instance.parent = options[choice-1]


def run(verbose=True):
    lm = LayerMapping(Country, COUNTRY_SHP, GEOLOCATION_COUNTRY_LEVEL_MAPPING,
                      transform=False, unique='iso')

    lm.save(strict=True, verbose=verbose)

    try:
        # LEVEL 1
        pre_save.connect(fix_adm1_before_save, AdmDivision)

        lm = LayerMapping(AdmDivision, FIRST_LEVEL_DIVISION_SHP, GEOLOCATION_FIRST_LEVEL_DIVISION_MAPPING,
                          transform=False, unique=['country_iso', 'id_gadm', 'type'])

        lm.save(strict=True, verbose=verbose)

        pre_save.disconnect(fix_adm1_before_save, AdmDivision)

        if ADM_DIVISION_MAX_LEVEL >= 2:
            # LEVEL 2
            pre_save.connect(fix_adm2_before_save, AdmDivision)

            lm = LayerMapping(AdmDivision, SECOND_LEVEL_DIVISION_SHP, GEOLOCATION_SECOND_LEVEL_DIVISION_MAPPING,
                              transform=False, unique=['country_iso', 'parent_id_gadm', 'id_gadm', 'type'])

            lm.save(strict=True, verbose=verbose)

            pre_save.disconnect(fix_adm2_before_save, AdmDivision)

            if ADM_DIVISION_MAX_LEVEL >= 3:
                # LEVEL 3
                pre_save.connect(fix_adm3_before_save, AdmDivision)

                lm = LayerMapping(AdmDivision, THIRD_LEVEL_DIVISION_SHP, GEOLOCATION_THIRD_LEVEL_DIVISION_MAPPING,
                                  transform=False, unique=['country_iso', 'parent_id_gadm', 'id_gadm', 'type'])

                lm.save(strict=True, verbose=verbose)

                pre_save.disconnect(fix_adm3_before_save, AdmDivision)

    except OGRException as e:
        print e.message

