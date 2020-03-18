from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'source.apps.core'

    def ready(self):
        import source.apps.core.signals.user
