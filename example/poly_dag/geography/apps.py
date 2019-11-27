from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GeographyConfig(AppConfig):
    name = "poly_dag.geography"
    verbose_name = _("Geography")

    def ready(self):
        try:
            import poly_dag.geography.signals  # noqa F401
        except ImportError:
            pass
