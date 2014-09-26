# coding=utf-8
from django.core.management.base import NoArgsCommand
from ... import load


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        load.run()

