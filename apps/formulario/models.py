from turtle import mode

from django.db import models


# Create your models here.
class Formulario(models.Model):
    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    nombre = models.CharField(verbose_name="Nombre", max_length=256)
    fecha = models.DateField(
        verbose_name="Fecha",
    )
    remision = models.CharField(
        verbose_name="REMISIÓN",
        max_length=256,
        choices=[
            (
                "No remitido",
                "No remitido",
            ),
            (
                "Atención primaria",
                "Atención primaria",
            ),
            (
                "Programa de control",
                "Programa de control",
            ),
            (
                "Atención secundaria",
                "Atención secundaria",
            ),
        ],
    )
    historia_clinica = models.BooleanField(
        default=True,
        verbose_name="Diagnóstico histológico",
    )

    motivo_consulta = models.CharField(
        verbose_name="Motivo de consulta",
        max_length=256,
        default="No motivo de consulta",
    )

    primer_sintoma = models.CharField(verbose_name="Primer síntoma", max_length=256)

    tiempo_de_aparicion = models.CharField(
        verbose_name="Tiempo de aparición",
        max_length=256,
        choices=[
            (
                "Días",
                "Días",
            ),
            (
                "Meses",
                "Meses",
            ),
            (
                "Años",
                "Años",
            ),
        ],
    )
    otros_sintomas = models.TextField(
        verbose_name="Otros Síntomas", null=True, blank=True
    )

    personales_de_riesgo = models.CharField(
        verbose_name="Antecedentes personales de riesgos",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Tabaquismo",
                "Tabaquismo",
            ),
            (
                "Exposición a irritantes",
                "Exposición a irritantes",
            ),
            (
                "Ingestión bebidas alcohólicas",
                "Ingestión bebidas alcohólicas",
            ),
            (
                "Trauma región de la lesión",
                "Trauma región de la lesión",
            ),
            (
                "Mala higiene bucal",
                "Mala higiene bucal",
            ),
            (
                "Uso de prótesis",
                "Uso de prótesis",
            ),
        ],
    )
    personales_patologicos = models.CharField(
        verbose_name="Antevedentes personales patológicos",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Leucoplasias",
                "Leucoplasias",
            ),
            (
                "Queratosis",
                "Queratosis",
            ),
            (
                "Avitaminosis",
                "Avitaminosis",
            ),
            (
                "Tuberculosis",
                "Tuberculosis",
            ),
            (
                "Sífilis",
                "Sífilis",
            ),
            (
                "Infección crónica",
                "Infección crónica",
            ),
            (
                "VIH",
                "VIH",
            ),
            (
                "Neoplasia maligna",
                "Neoplasia maligna",
            ),
        ],
    )

    familiares_con_cancer = models.CharField(
        verbose_name="Familiares con cáncer",
        max_length=256,
        choices=[
            (
                "Si",
                "Si",
            ),
            (
                "No",
                "No",
            ),
            (
                "Desconocido",
                "Desconocido",
            ),
        ],
    )

    caracteristicas_de_la_lesion = models.CharField(
        verbose_name="Características de la lesión",
        max_length=256,
        choices=[
            (
                "Vegetante",
                "Vegetante",
            ),
            (
                "Infiltrante",
                "Infiltrante",
            ),
            (
                "Úlcero-vegetante",
                "Úlcero-vegetante",
            ),
            (
                "Úlcero-infiltrante",
                "Úlcero-infiltrante",
            ),
            (
                "Necrosante",
                "Necrosante",
            ),
            (
                "Plana",
                "Plana",
            ),
            (
                "Submucosa",
                "Submucosa",
            ),
            (
                "Nodular",
                "Nodular",
            ),
        ],
    )

    region = models.CharField(
        verbose_name="Región",
        max_length=256,
        choices=[
            (
                "Derecha",
                "Derecha",
            ),
            (
                "Central",
                "Central",
            ),
            (
                "Izquierda",
                "Izquierda",
            ),
        ],
    )

    tamanno_de_la_lesion = models.DateField(verbose_name="Tamaño de la lesión")

    localizacion_en_labio = models.CharField(
        verbose_name="Localización (Labio)",
        max_length=256,
        choices=[
            (
                "Labio superior",
                "Labio superior",
            ),
            (
                "Mucosa superior",
                "Mucosa superior",
            ),
            (
                "Comisuras labiales",
                "Comisuras labiales",
            ),
            (
                "Labio inferior",
                "Labio inferior",
            ),
            (
                "Mucosa inferior",
                "Mucosa inferior",
            ),
        ],
    )

    lengua_movil = models.CharField(
        verbose_name="Lengua móvil",
        max_length=256,
        choices=[
            (
                "Cara central",
                "Cara central",
            ),
            (
                "Cara dorsal",
                "Cara dorsal",
            ),
            (
                "Punta",
                "Punta",
            ),
            (
                "Borde",
                "Borde",
            ),
        ],
    )

    suelo_de_Boca = models.CharField(
        verbose_name="Suelo de Boca",
        max_length=256,
        choices=[
            (
                "Parte anterior",
                "Parte anterior",
            ),
            (
                "Parte lateral",
                "Parte lateral",
            ),
        ],
    )

    encia = models.CharField(
        verbose_name="Encía",
        max_length=256,
        choices=[
            (
                "Superior",
                "Superior",
            ),
            (
                "Inferior",
                "Inferior",
            ),
        ],
    )

    otras_partes_del_a_boca = models.CharField(
        verbose_name="Otras Partes (Boca)",
        max_length=256,
        choices=[
            (
                "Carrillo",
                "Carrillo",
            ),
            (
                "Vesíbulo",
                "Vesíbulo",
            ),
            (
                "Paladar duro",
                "Paladar duro",
            ),
            (
                "Espacio retromolar",
                "Espacio retromolar",
            ),
        ],
    )

    glandulas_salibales = models.CharField(
        verbose_name="Glándulas salivales",
        max_length=256,
        choices=[
            (
                "Parótida",
                "Parótida",
            ),
            (
                "Sublingual",
                "Sublingual",
            ),
            (
                "Submaxilar",
                "Submaxilar",
            ),
            (
                "Otra",
                "Otra",
            ),
        ],
    )

    ardenopatia_cervical_derecha = models.CharField(
        verbose_name="Ardenopatía cervical derecha",
        max_length=256,
        choices=[
            (
                "No",
                "No",
            ),
            (
                "Nivel I",
                "Nivel I",
            ),
            (
                "Nivel II",
                "Nivel II",
            ),
            (
                "Nivel III",
                "Nivel III",
            ),
            (
                "Nivel IV",
                "Nivel IV",
            ),
            (
                "Nivel V",
                "Nivel V",
            ),
        ],
    )
    ardenopatia_cervical_izquierda = models.CharField(
        verbose_name="Ardenopatía cervical izquierda",
        max_length=256,
        choices=[
            (
                "No",
                "No",
            ),
            (
                "Nivel I",
                "Nivel I",
            ),
            (
                "Nivel II",
                "Nivel II",
            ),
            (
                "Nivel III",
                "Nivel III",
            ),
            (
                "Nivel IV",
                "Nivel IV",
            ),
            (
                "Nivel V",
                "Nivel V",
            ),
        ],
    )

    extension_clinica_a = models.CharField(
        verbose_name="Extensión clínica a",
        max_length=256,
        choices=[
            (
                "No",
                "No",
            ),
            (
                "Suelo de boca",
                "Suelo de boca",
            ),
            (
                "Laringe",
                "Laringe",
            ),
            (
                "Labio",
                "Labio",
            ),
            (
                "Otras partes de la cavidad oral",
                "Otras partes de la cavidad oral",
            ),
            (
                "Mesofaringe",
                "Mesofaringe",
            ),
            (
                "Hipofaringe",
                "Hipofaringe",
            ),
            (
                "Encía",
                "Encía",
            ),
            (
                "Nasofaringe",
                "Nasofaringe",
            ),
            (
                "Piel y partes blandas",
                "Piel y partes blandas",
            ),
            (
                "Hueso",
                "Hueso",
            ),
            (
                "Otras",
                "Otras",
            ),
        ],
    )

    performance_status = models.CharField(
        verbose_name="Performance status",
        max_length=256,
        choices=[
            (
                "0",
                "0",
            ),
            (
                "1",
                "1",
            ),
            (
                "2",
                "2",
            ),
            (
                "3",
                "3",
            ),
            (
                "4",
                "4",
            ),
        ],
    )

    primer_apellido = models.CharField(verbose_name="Primer apellido", max_length=256)

    segundo_apellido = models.CharField(verbose_name="Segundo apellido", max_length=256)

    nombre_del_paciente = models.CharField(
        verbose_name="Nombre del paciente", max_length=256
    )

    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=256,
        choices=[
            (
                "Femenino",
                "Femenino",
            ),
            (
                "Masculino",
                "Masculino",
            ),
        ],
    )

    edad = models.PositiveIntegerField(verbose_name="Edad (en años)")

    color_de_piel = models.CharField(
        verbose_name="Color de la piel",
        max_length=256,
        choices=[
            (
                "Blanca",
                "Blanca",
            ),
            (
                "Negra",
                "Negra",
            ),
            (
                "Mestiza",
                "Mestiza",
            ),
        ],
    )

    carne_de_identidad = models.CharField(
        verbose_name="Carné de identidad", max_length=256
    )

    historia_clinica_numero = models.CharField(
        verbose_name="Historia clínica número:", max_length=256
    )

    fecha_de_inscripcion = models.PositiveIntegerField(
        verbose_name="Fecha de Inscripción"
    )

    creatinina = models.DecimalField(
        verbose_name="Creatinina",
        decimal_places=2,
        max_digits=15,
    )

    hemoglobina = models.DecimalField(
        verbose_name="Hemoglobina",
        decimal_places=2,
        max_digits=15,
    )

    imagen_rx_torax = models.CharField(
        verbose_name="Imagen del Torax",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )
    imagen_us_abdomen = models.CharField(
        verbose_name="Imagen del Abdomen",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )
    imagen_tac_cavidad_oral = models.CharField(
        verbose_name="Imagen de la Cavidad Oral",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )

    otros_tac_faringe = models.CharField(
        verbose_name="Otros TAC Faringe",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )
    otros_tac_cuello = models.CharField(
        verbose_name="Otros TAC Cuello",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )
    otros_tac_torax = models.CharField(
        verbose_name="Otros TAC Tórax",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )
    otros_rmn = models.CharField(
        verbose_name="Otros RMN",
        max_length=256,
        choices=[
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Positivo",
                "Positivo",
            ),
            (
                "Negativo",
                "Negativo",
            ),
        ],
    )
    biopsia_numero = models.PositiveIntegerField(verbose_name="Biopsia No")

    fecha_de_diagnostico = models.DateField(verbose_name="Fecha de diagnóstico")

    diagnostico_topografico = models.CharField(
        verbose_name="Diagnóstico Topográfico", max_length=256
    )
