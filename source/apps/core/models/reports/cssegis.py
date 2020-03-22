from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from source.apps.core.models.timestamped import TimestampedModel


class ReportCsseGisManager(models.Manager):
    def fetch(self):
        import csv
        import requests
        from django.core.cache import cache

        source = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/' \
                 'csse_covid_19_data/csse_covid_19_daily_reports/%s.csv' % datetime.now().date().strftime('%m-%d-%Y')

        cached_data = cache.get('csse_covid')

        if cached_data:
            csv_data = cached_data
        else:
            req = requests.get(source)
            if req.status_code == 200:
                csv_data = req.text
                cache.set('csse_covid', csv_data, 3600 * 12)
            else:
                csv_data = None

        if csv_data:
            output = csv.DictReader(csv_data.split('\n'), delimiter=',')

        return output if csv_data else None


class ReportCsseGisModel(TimestampedModel):
    """
    A model for storing data from
    https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports
    """

    default_map_center = Point(x=112.2707, y=30.9756)  # Hubei, China

    state = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('Province/State'))
    country = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('Country/Region'))
    last_update = models.DateTimeField(null=True, blank=True, verbose_name=_('Last Update'))
    confirmed = models.PositiveIntegerField(default=0, verbose_name=_('Confirmed'))
    deaths = models.PositiveIntegerField(default=0, verbose_name=_('Deaths'))
    recovered = models.PositiveIntegerField(default=0, verbose_name=_('Recovered'))
    location = PointField(default=default_map_center)

    objects = models.Manager()
    remote = ReportCsseGisManager()

    def __str__(self):
        return 'Reports for %s' % self.country

    @cached_property
    def location_name(self):
        if self.state and self.country:
            return f'{self.country}, {self.state}'
        else:
            return self.country

    def save(self, *args, **kwargs):
        if self.last_update:
            self.last_update = datetime.strptime(self.last_update, '%Y-%m-%dT%H:%M:%S').astimezone(tz=timezone.utc)
        super().save(*args, **kwargs)

    @staticmethod
    def sync():
        """
        Synchronize
        """
        result = ReportCsseGisModel.remote.fetch()
        line_count = 0

        for row in result:
            instance, created = ReportCsseGisModel.objects.get_or_create(
                state=row['Province/State'],
                country=row['Country/Region'],
                location=Point(x=float(row['Longitude']), y=float(row['Latitude']))
            )

            instance.last_update = row['Last Update']
            instance.confirmed = row['Confirmed']
            instance.deaths = row['Deaths']
            instance.recovered = row['Recovered']
            instance.save()

            line_count += 1

    class Meta:
        db_table = 'report_cssegis'
        verbose_name = 'CSSEGIS Report'
        unique_together = ('country', 'location', )
        ordering = ('country', 'state', )
