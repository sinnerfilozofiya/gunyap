from django.apps import AppConfig


class KurumsalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kurumsal'


def ready(self):
        import kurumsal.signals  # Sinyali buraya dahil ediyoruz