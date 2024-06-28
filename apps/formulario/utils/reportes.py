import json
from typing import List

from django.shortcuts import redirect
from django.urls import reverse

from ..models import *
from .util_reporte_d import custom_export_report_by_name


def obtener_datos_para_reporte(formulario: Formulario):
    return {
        "id": str(formulario.id),
        "nombre":str(formulario.nombre),
        "fecha":str(formulario.fecha),
        "historia_clinica":str("sí" if formulario.historia_clinica else "no"),
        "motivo_consulta":str(formulario.motivo_consulta),
        "remicion":str(formulario.remision),
        "otros_sintomas":str(formulario.otros_sintomas),
        "primer_sintoma":str(formulario.primer_sintoma),
        "tiempo_de_aparicion":str(formulario.tiempo_de_aparicion),
        "personales_de_riesgo":str(formulario.personales_de_riesgo),
        "personales_patologicos":str(formulario.personales_patologicos),
        "familiares_con_cancer":str(formulario.familiares_con_cancer),
        "caracteristicas_de_la_lesion":str(formulario.caracteristicas_de_la_lesion),
        "region":str(formulario.region),
        "tamanno_de_la_lesion":str(formulario.tamanno_de_la_lesion),
        "localizacion_en_labio":str(formulario.localizacion_en_labio),
        "lengua_movil":str(formulario.lengua_movil),
        "suelo_de_Boca":str(formulario.suelo_de_Boca),
        "encia":str(formulario.encia),
        "otras_partes_del_a_boca":str(formulario.otras_partes_del_a_boca),
        "glandulas_salibales":str(formulario.glandulas_salibales),
        "ardenopatia_cervical_derecha":str(formulario.ardenopatia_cervical_derecha),
        "ardenopatia_cervical_izquierda":str(formulario.ardenopatia_cervical_izquierda),
        "extension_clinica_a":str(formulario.extension_clinica_a),
        "performance_status":str(formulario.performance_status),
        "primer_apellido":str(formulario.primer_apellido),
        "segundo_apellido":str(formulario.segundo_apellido),
        "nombre_del_paciente":str(formulario.nombre_del_paciente),
        "sexo":str(formulario.sexo),
        "edad":str(formulario.edad),
        "color_de_piel":str(formulario.color_de_piel),
        "carne_de_identidad":str(formulario.carne_de_identidad),
        "historia_clinica_numero":str(formulario.historia_clinica_numero),
        "fecha_de_inscripcion":str(formulario.fecha_de_inscripcion),
        "creatinina":str(formulario.creatinina),
        "hemoglobina":str(formulario.hemoglobina),
        "imagen_rx_torax":str(formulario.imagen_rx_torax),
        "imagen_us_abdomen":str(formulario.imagen_us_abdomen),
        "imagen_tac_cavidad_oral":str(formulario.imagen_tac_cavidad_oral),
        "otros_tac_faringe":str(formulario.otros_tac_faringe),
        "otros_tac_cuello":str(formulario.otros_tac_cuello),
        "otros_tac_torax":str(formulario.otros_tac_torax),
        "otros_rmn":str(formulario.otros_rmn),
        "biopsia_numero":str(formulario.biopsia_numero),
        "fecha_de_diagnostico":str(formulario.fecha_de_diagnostico),
        "diagnostico_topografico":str(formulario.diagnostico_topografico),
        "diagnostico_morfologico":str(formulario.diagnostico_morfologico),
        "diagnosticado_en":str(formulario.diagnosticado_en),
        "diagnostico_topografico_selecciona":str(formulario.diagnostico_topografico_selecciona),
        "diagnostico_morfologico_selecciona":str(formulario.diagnostico_morfologico_selecciona),
        "diagnosticado_en_selecciona":str(formulario.diagnosticado_en_selecciona),
        "grado_de_diferenciacion":str(formulario.grado_de_diferenciacion),
        "base_del_diagnostico":str(formulario.base_del_diagnostico),
        "otras":str(formulario.otras),
        "etapa_clinica":str(formulario.etapa_clinica),
        "tnm_T":str(formulario.tnm_T),
        "tnm_N":str(formulario.tnm_N),
        "tnm_M":str(formulario.tnm_M),
        "ptnm_pT":str(formulario.ptnm_pT),
        "ptnm_pN":str(formulario.ptnm_pN),
        "ptnm_pM":str(formulario.ptnm_pM),
        "metastasis_a_distancia":str(formulario.metastasis_a_distancia),
        "extension_clinica":str(formulario.extension_clinica),
        "en_otro_centro":str(formulario.en_otro_centro),
        "en_la_institucion":str(formulario.en_la_institucion),
        "tratamiento_planificado":str(formulario.tratamiento_planificado),
        "otro_tratamiento_planificado":str(formulario.otro_tratamiento_planificado),
        "inclusion_en_ec":str("sí" if formulario.inclusion_en_ec else "no"),
        "en_caso_de_si":str(formulario.en_caso_de_si),
        "tratamiento_quirurgico":str("sí"if formulario.tratamiento_quirurgico else "no"),
        "tipo_de_cirugia":str(formulario.tipo_de_cirugia),
        "fecha_del_tratamiento_quirurgico":str(formulario.fecha_del_tratamiento_quirurgico),
        "tratamiento_radioterapia":str( "sí"if formulario.tratamiento_radioterapia else "no"),
        "tipo_de_tratamiento_radioterap":str(formulario.tipo_de_tratamiento_radioterap),
        "fecha_del_inicio_del_tratamiento_radioterapeutico":str(formulario.fecha_del_inicio_del_tratamiento_radioterapeutico),
        "fecha_del_final_del_tratamiento_radioterapeutico":str(formulario.fecha_del_final_del_tratamiento_radioterapeutico),
        "dosis_total":str(formulario.dosis_total),
        "gy_fraccion":str(formulario.gy_fraccion),
        "tratamiento_quimioterapia":str("sí"if formulario.tratamiento_quimioterapia else "no"),
        "esquema_tratamiento":str(formulario.esquema_tratamiento),
        "numero_de_ciclos":str(formulario.numero_de_ciclos),
        "fecha_del_inicio_del_tratamiento_quimioterapeutico":str(formulario.fecha_del_inicio_del_tratamiento_quimioterapeutico),
        "fecha_del_final_del_tratamiento_quimioterapeutico":str(formulario.fecha_del_final_del_tratamiento_quimioterapeutico),
        "otro_tratamiento":str("sí" if formulario.otro_tratamiento else "no"),
        "cual_tratamiento":str(formulario.cual_tratamiento),
        "fecha_del_inicio_del_tratamiento":str(formulario.fecha_del_inicio_del_tratamiento),
        "fecha_del_final_del_tratamiento":str(formulario.fecha_del_final_del_tratamiento),
        "evaluacion_de_la_respuesta":str(formulario.evaluacion_de_la_respuesta),
        "observaciones":str(formulario.observaciones),
        "nombre_del_medico":str(formulario.nombre_del_medico),
        "registro_profesional":str(formulario.registro_profesional),
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
        "Reporte Clinico",
        obtener_datos_para_reporte_desde_queryset(queryset),
        file="reporte",
    )


def crear_reporte_paciente(queryset):
    return custom_export_report_by_name(
        "Reporte Paciente",
        obtener_datos_para_reporte_desde_queryset(queryset),
        file="reporte",
    )
