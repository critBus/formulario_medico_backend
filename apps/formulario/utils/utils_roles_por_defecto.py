from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django_reportbroD.models import ReportDefinition, ReportRequest

from config.utils.utils_permission import crear_rol

from ..models import NOMBRE_ROL_ADMINISTRADOR, NOMBRE_ROL_TRABAJADOR, Formulario

User = get_user_model()


def crear_roles_django_default():
    crear_rol(
        lista_modelos=[
            Formulario,
            ReportRequest,
            ReportDefinition,
            User,
            Group,
            Permission,
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[],
        nombre_rol=NOMBRE_ROL_ADMINISTRADOR,
    )
    crear_rol(
        lista_modelos=[
            Formulario,
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[],
        nombre_rol=NOMBRE_ROL_TRABAJADOR,
    )
