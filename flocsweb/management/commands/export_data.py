from django.conf import settings
from django.core.management.base import BaseCommand
from flocsweb.store import open_django_store


class Command(BaseCommand):
    help = "Export all data for analysis into CSV files."

    def handle(self, *args, **options):
        self.stdout.write('Creating export of all data in {0}'.format(settings.EXPORTED_DATA_DIR))
        with open_django_store() as store:
            store.export(dirpath=settings.EXPORTED_DATA_DIR)
