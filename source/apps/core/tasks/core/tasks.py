from celery import shared_task
from celery.signals import task_failure

from django.utils import log

from source.apps.core import email
from source.apps.core.logger import log

from source.apps.core.models.reports.cssegis import ReportCsseGisModel


@shared_task
#def send_mail(request=None, user=None, template=None, data=None, to=None, subject=None, message=None):
def send_mail(**kwargs):
    """ send mail function, subject and template_name as argument in list """

    # if settings.DEBUG:
    #     return None

    return email.send_email(**kwargs)


@task_failure.connect
def process_failure_signal(exception, traceback, sender, task_id,
                           signal, args, kwargs, einfo, **kw):
    """Catch any task failure signals from within our worker processes and log
    them as exceptions, so they appear in Sentry and ordinary logging
    output."""

    exc_info = (type(exception), exception, traceback)
    log.error(
        u'Celery TASK exception: {0.__name__}: {1}'.format(*exc_info),
        exc_info=exc_info,
        extra={
            'data': {
                'task_id': task_id,
                'sender': sender,
                'args': args,
                'kwargs': kwargs
            }
        })


@shared_task
def cssegis_sync():
    ReportCsseGisModel.sync()
