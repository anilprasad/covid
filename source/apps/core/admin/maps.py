from django.contrib import admin

from source.apps.core.models import MapsArcgisModel

from source.apps.core import paginator


@admin.register(MapsArcgisModel)
class MapsArcgisAdmin(admin.ModelAdmin):

    paginator = paginator.FasterDjangoPaginator

    def has_image(self, obj):
        return obj.image.name is not None

    has_image.boolean = True

    list_display = ('name', 'has_image', 'created_at', 'updated_at')
    search_fields = ('name', )
    ordering = ('name',)
    readonly_fields = ('slug', 'created_at', 'updated_at', )
