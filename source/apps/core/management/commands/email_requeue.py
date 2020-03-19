from django.core.management.base import BaseCommand

from source.apps.core.tasks.core.tasks import send_mail


class Command(BaseCommand):
    help = "Requeue emails"

    def handle(self, *args, **options):
        self.stdout.write("To be implemented ...")
