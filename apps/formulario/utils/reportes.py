import json
from typing import List

from django.shortcuts import redirect
from django.urls import reverse

from ..models import *
from .util_reporte_d import custom_export_report_by_name


def obtener_datos_para_reporte(formulario: Formulario):
    return {
        "id": formulario.id,
        "nombre": formulario.nombre,
        "fecha": formulario.fecha,
        "historia_clinica": formulario.historia_clinica,
        "remicion": formulario.remision,
    }


def obtener_datos_para_reporte_desde_queryset(queryset):
    entidades: List[Formulario] = queryset
    lista = []
    for entidad in entidades:
        data_licencia = obtener_datos_para_reporte(entidad)

        lista.append(data_licencia)

    return {"lista": lista}


def crear_reporte_completo_paciente(queryset):
    return custom_export_report_by_name(
        "Reporte Paciente",
        obtener_datos_para_reporte_desde_queryset(queryset),
        file="reporte",
    )


def crear_reporte_paciente(queryset):
    return custom_export_report_by_name(
        "Reporte Paciente",
        obtener_datos_para_reporte_desde_queryset(queryset),
        file="reporte",
    )
