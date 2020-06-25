from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    def ready(self, *args, **kwargs):
        from . import signals 
        super().ready()
