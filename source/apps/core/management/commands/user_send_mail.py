# coding=utf-8
from django.core.management.base import BaseCommand
from source.apps.core.models.user.models import User
from source.apps.core.email import send_email


class Command(BaseCommand):
    help = 'Send mail to user'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('subject', type=str, help='Subject')
        parser.add_argument('template', type=str, help='Path to template')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(email=options['email'])
            send_email(
                to=user.email,
                subject=options['subject'],
                data={
                    'username': user.first_name,
                },
                template=options['template']
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR('ERROR: %s' % str(e)))
