import re

from django.contrib import admin
from django.utils.safestring import mark_safe

from source.apps.core.models.email import EmailLogModel


def requeue_selected(modeladmin, request, queryset):
    queryset.update(status=EmailLogModel.STATUS_REQUEUED)


@admin.register(EmailLogModel)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'status', 'created_at', 'updated_at')
    search_fields = ('recipient', 'subject', )
    list_filter = ('status', )
    ordering = ('-created_at', )
    readonly_fields = ('sender', 'recipient', 'subject', 'custom_body', )
    exclude = ('body',)

    actions = [requeue_selected, ]

    def custom_body(self, obj):
        content = '<iframe id="emailContent" src="about:blank"></iframe>' \
                  '<script type="text/javascript">' \
                  'var doc = document.getElementById(\'emailContent\').contentWindow.document;' \
                  'doc.open();' \
                  'doc.write(\''+obj.body.replace("'","\"").replace("\n","")+'\');' \
                  'doc.close();' \
                  '</script>'

        return mark_safe(content)

    custom_body.allow_tags = True

    def updated_at(self, obj):
        return obj.updated_at

    updated_at.short_description = 'Resent at'
