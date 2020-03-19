from django.contrib import admin

from source.apps.core.models import MapsArcgisModel

from source.apps.core import paginator


@admin.register(MapsArcgisModel)
class MapsArcgisAdmin(admin.ModelAdmin):

    paginator = paginator.FasterDjangoPaginator

    list_display = ('name', 'created_at', )
    search_fields = ('name', )
    ordering = ('name',)
    readonly_fields = ('slug', 'created_at', 'updated_at', )
