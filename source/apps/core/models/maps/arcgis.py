from django.db import models

from source.apps.core.models.timestamped import TimestampedModel
from source.apps.core.models.slugable import SlugableModel


class MapsArcgisModel(TimestampedModel, SlugableModel):

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=72)
    url = models.URLField()

    def __str__(self):
        return '%s map' % self.name

    class Meta:
        db_table = 'maps_arcgis'
        verbose_name = 'Arcgis maps'
