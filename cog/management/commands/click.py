import os
import sys

from django.core.management.base import BaseCommand


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
            print organisation
