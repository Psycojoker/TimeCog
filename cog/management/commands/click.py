import os
import sys
import yaml
import yamlordereddictloader

from django.core.management.base import BaseCommand

from cog import click


class Command(BaseCommand):
    help = 'Click to cog'

    def handle(self, *args, **options):
        if not os.path.exists("organisations"):
            print "organisations folder doesn't exists, end"
            sys.exit(0)

        organisations = filter(lambda x: x.endswith(("yaml", "yml")), os.listdir("organisations"))

        if not organisations:
            print "No organisations files, end"
            sys.exit(0)

        for organisation in organisations:
            click(organisation, yaml.load(open(os.path.join("organisations", organisation)), Loader=yamlordereddictloader.Loader))
