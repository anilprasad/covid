from django.core.management.base import BaseCommand

from source.apps.core.models import ReportCsseGisModel


class Command(BaseCommand):
    help = "CLI task for manually synchronizing reports from CSSEGIS repository"

    def handle(self, *args, **options):
        try:
            ReportCsseGisModel.sync()
            self.stdout.write("Done ...")
        except Exception as e:
            self.stderr.write('Sync error: %s' % str(e))
