import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


def send_email(**kwargs):

    message = kwargs.get('message')
    template = kwargs.get('template')
    data = kwargs.get('data', {})
    to = kwargs.get('to')
    subject = kwargs.get('subject')
    from_email = os.environ.get('APP_DEFAULT_FROM_EMAIL')

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

    send_status = msg.send()

    return send_status
