import os
import logging

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

from source.apps.core.models.email import EmailLogModel

logger = logging.getLogger(__name__)


def send_email(**kwargs):

    message = kwargs.get('message')
    template = kwargs.get('template')
    data = kwargs.get('data', {})
    to = kwargs.get('to')
    subject = kwargs.get('subject')
    from_email = kwargs.get('sender', os.environ.get('APP_DEFAULT_FROM_EMAIL'))

    if 'public_url' not in data:
        data['public_url'] = settings.APP_FRONTEND_URL

    if 'APP_NAME' not in data:
        data['APP_NAME'] = settings.APP_NAME

    data['domain'] = settings.APP_FRONTEND_URL

    if type(to) == str:
        to = [to]

    if type(to) == tuple:
        to = list(to)

    if not message:
        html = get_template('%s' % template)
        html_content = html.render(data)
    else:
        html_content = message

    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=f"{data['APP_NAME']} <{from_email}>",
        to=to
    )
    msg.attach_alternative(html_content, "text/html")

    sending_status = msg.send()

    log_email(**{
        'sender': from_email,
        'recipient': to,
        'subject': subject,
        'body': html_content,
        'status': EmailLogModel.STATUS_SENT if sending_status != 0 else EmailLogModel.STATUS_NOT_SENT
    })

    return sending_status


def log_email(**kwargs):
    try:
        instance, created = EmailLogModel.objects.get_or_create(
            sender=kwargs.get('sender'),
            recipient=','.join(kwargs.get('recipient')),
            subject=kwargs.get('subject'),
            body=kwargs.get('body')
        )

        instance.status = kwargs.get('status')
        instance.save(update_fields=['status'])

    except Exception as e:
        logger.error(str(e))

