from django.db import models
from django.utils.translation import ugettext_lazy as _

from .timestamped import TimestampedModel


class EmailLogModel(TimestampedModel):

    STATUS_PENDING = 0
    STATUS_SENT = 1
    STATUS_NOT_SENT = 2
    STATUS_REQUEUED = 3

    CHOICE_STATUS = (
        (STATUS_PENDING, _('Pending')),
        (STATUS_SENT, _('Sent')),
        (STATUS_NOT_SENT, _('Not sent')),
        (STATUS_REQUEUED, _('Requeued')),
    )

    sender = models.CharField(max_length=254)
    recipient = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    body = models.TextField()
    status = models.PositiveSmallIntegerField(choices=CHOICE_STATUS, default=STATUS_PENDING)

    def __str__(self):
        return self.recipient

    class Meta:
        db_table = 'email_log'
        verbose_name = 'Email log'
