from django.apps import AppConfig
from django.db.models.signals import post_migrate


def config_app(sender, **kwargs):
    from .utils.utils_roles_por_defecto import crear_roles_django_default
    from .utils.util_reporte_d import load_automatic_reports
    from .utils.generador_datos import generar_datos_aleatorios
    from django.conf import settings

    crear_roles_django_default()
    load_automatic_reports()
    if settings.LOAD_EXAMPLE_DATA:
        generar_datos_aleatorios(10)


class FormularioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.formulario"

    def ready(self):
        post_migrate.connect(config_app, sender=self)
