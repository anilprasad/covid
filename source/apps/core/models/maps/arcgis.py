from django.db import models
from django.urls import reverse

from source.apps.core.models.timestamped import TimestampedModel
from source.apps.core.models.slugable import SlugableModel
from source.apps.core.media import scramble_uploaded_filename


class MapsArcgisModel(TimestampedModel, SlugableModel):

    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=72)
    url = models.URLField()
    image = models.ImageField(null=True, blank=True, upload_to=scramble_uploaded_filename)

    def __str__(self):
        return '%s map' % self.name

    def get_absolute_url(self):
        return reverse('map_arcgis', kwargs={'country': self.slug})

    class Meta:
        db_table = 'maps_arcgis'
        verbose_name = 'Arcgis maps'
