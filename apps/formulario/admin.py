from django.contrib import admin

from .models import *
from .utils.reportes import generar_reporte_paciente


# Register your models here.
@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fecha",
        "nombre",
        "remision",
        "historia_clinica",
    )
    search_fields = (
        "id",
        "remision",
        "fecha",
        "nombre",
    )
    list_filter = (
        "remision",
        "fecha",
        "historia_clinica",
    )
    ordering = (
        "-id",
        "remision",
        "fecha",
        "nombre",
        "historia_clinica",
    )
    date_hierarchy = "fecha"
    list_display_links = (
        "id",
        "fecha",
        "nombre",
        "remision",
        "historia_clinica",
    )
    actions = [generar_reporte_paciente]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "fecha",
                    "nombre",
                )
            },
        ),
        (
            "REMISIÓN",
            {
                "fields": (
                    "remision",
                    "historia_clinica",
                )
            },
        ),
        (
            "ANAMNESIS",
            {
                "fields": (
                    "motivo_de_consulta",
                    "primer_sintoma",
                    "tiempo_de_aparicion",
                    "otros_sintomas",
                ),
            },
        ),
        (
            "ANTECEDENTES",
            {
                "fields": (
                    "personales_de_riesgo",
                    "personales_patologicos",
                    "familiares_con_cancer",
                ),
            },
        ),
        (
            "EVALUACIÓN CLÍNICA",
            {
                "fields": (
                    "caracteristicas_de_la_lesion",
                    "region",
                    "tamanno_de_la_lesion",
                    "localizacion_en_labio",
                    "lengua_movil",
                    "suelo_de_Boca",
                    "encia",
                    "otras_partes_del_a_boca",
                    "glandulas_salibales",
                    "ardenopatia_cervical_derecha",
                    "ardenopatia_cervical_izquierda",
                    "extension_clinica_a",
                    "performance_status",
                ),
            },
        ),
        (
            "DATOS DEL PACIENTE",
            {
                "fields": (
                    "primer_apellido",
                    "segundo_apellido",
                    "nombre_del_paciente",
                    "sexo",
                    "edad",
                    "color_de_piel",
                    "carne_de_identidad",
                    "historia_clinica_numero",
                    "fecha_de_inscripcion",
                ),
            },
        ),
        (
            "EVALUCIÓN",
            {
                "fields": (
                    "creatinina",
                    "hemoglobina",
                    "imagen_rx_torax",
                    "imagen_us_abdomen",
                    "imagen_tac_cavidad_oral",
                    "otros_tac_faringe",
                    "otros_tac_cuello",
                    "otros_tac_torax",
                    "otros_rmn",
                ),
            },
        ),
        (
            "ANATOMÍA PATOLÓGICA",
            {
                "fields": (
                    "biopsia_numero",
                    "fecha_de_diagnostico",
                    "diagnostico_topografico",
                    "diagnostico_morfologico",
                    "diagnosticado_en",
                    "diagnostico_topografico_selecciona",
                    "diagnostico_morfologico_selecciona",
                    "diagnosticado_en_selecciona",
                    "grado_de_diferenciacion",
                    "base_del_diagnostico",
                    "otras",
                ),
            },
        ),
        (
            "ESTADIAMIENTO",
            {
                "fields": (
                    "etapa_clinica",
                    "metastasis_a_distancia",
                    "extension_clinica",
                ),
            },
        ),
        (
            "TRATAMIENTO",
            {
                "fields": (
                    "en_otro_centro",
                    "en_la_institucion",
                    "tratamiento_planificado",
                    "otro_tratamiento_planificado",
                    "inclusion_en_ec",
                    "en_caso_de_si",
                ),
            },
        ),
        (
            "DESCRIPCIÓN DEL TRATAMIENTO",
            {
                "fields": (
                    "tratamiento_quirurgico",
                    "tipo_de_cirugia",
                    "fecha_del_tratamiento_quirurgico",
                    "tratamiento_radioterapia",
                    "tipo_de_tratamiento_radioterap",
                    "fecha_del_inicio_del_tratamiento_radioterapeutico",
                    "fecha_del_final_del_tratamiento_radioterapeutico",
                    "dosis_total",
                    "gy_fraccion",
                    "tratamiento_quimioterapia",
                    "esquema_tratamiento",
                    "numero_de_ciclos",
                    "fecha_del_inicio_del_tratamiento_quimioterapeutico",
                    "fecha_del_final_del_tratamiento_quimioterapeutico",
                    "otro_tratamiento",
                    "cual_tratamiento",
                    "fecha_del_inicio_del_tratamiento",
                    "fecha_del_final_del_tratamiento",
                    "evaluacion_de_la_respuesta",
                    "fecha_evaluacion",
                    "observaciones",
                    "nombre_del_medico",
                    "registro_profesional",
                ),
            },
        ),
    )
