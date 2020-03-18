from django.db import models
from django.conf import settings

from .slugable import SlugableModel


class TranslatableModel(SlugableModel):

    CHOICE_LANGUAGES = getattr(settings, 'LANGUAGES', [])

    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=255, unique=True)
    language = models.CharField(max_length=4, choices=CHOICE_LANGUAGES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
