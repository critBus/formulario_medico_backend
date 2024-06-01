import json
from typing import List

from django.shortcuts import redirect
from django.urls import reverse

from ..models import *
from .util_reporte_d import custom_export_report_by_name


#
def generar_reporte_paciente(modeladmin, request, queryset):
    entidades: List[Formulario] = queryset
    lista = []
    for entidad in entidades:
        data_licencia = {
            "id": entidad.id,
            "nombre": entidad.nombre,
            "fecha": entidad.fecha,
            "historia_clinica": entidad.historia_clinica,
            "remicion": entidad.remision,
        }

        lista.append(data_licencia)

    data = {"lista": lista}

    return custom_export_report_by_name(
        "Reporte Paciente",
        data,
        file="reporte",
    )
