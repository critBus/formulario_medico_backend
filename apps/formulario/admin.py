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
            "Remision",
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
                    "motivo_consulta",
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
    )
