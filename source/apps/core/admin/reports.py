from django.contrib import admin

from leaflet.admin import LeafletGeoAdminMixin

from source.apps.core.models import ReportCsseGisModel
from source.apps.core import paginator


@admin.register(ReportCsseGisModel)
class ReportCsseGisAdmin(LeafletGeoAdminMixin, admin.ModelAdmin):

    paginator = paginator.FasterDjangoPaginator

    def has_image(self, obj):
        return obj.image.name is not None

    has_image.boolean = True

    map_width = '800px'
    list_display = ('country', 'state', 'confirmed', 'deaths', 'recovered', 'last_update', 'updated_at')
    search_fields = ('country', )
    ordering = ('country',)
    readonly_fields = ('created_at', 'updated_at', )
