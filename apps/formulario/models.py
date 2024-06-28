from turtle import mode

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

NOMBRE_ROL_ADMINISTRADOR = "Administrador"
NOMBRE_ROL_TRABAJADOR = "Trabajador"


def validate_noVacio(value):
    if len(str(value).strip()) == 0:
        raise ValidationError("Este campo no puede estar vacío.")


# Create your models here.
class Formulario(models.Model):
    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    nombre = models.CharField(verbose_name="Nombre", max_length=256, unique=True)
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
        default=False,
        verbose_name="Diagnóstico histológico",
    )

    motivo_consulta = models.CharField(
        verbose_name="Motivo de consulta",
        max_length=256,
        choices=[
            (
                "Aparición de lesión",
                "Aparición de lesión",
            ),
            (
                "Aumento de volumen",
                "Aumento de volumen",
            ),
            (
                "Nódulo cervical",
                "Nódulo cervical",
            ),
            (
                "Sangramiento",
                "Sangramiento",
            ),
            (
                "Odinofagia",
                "Odinofagia",
            ),
            (
                "Sialorrea",
                "Sialorrea",
            ),
            (
                "Dolor",
                "Dolor",
            ),
            (
                "Parálisis facial",
                "Parálisis facial",
            ),
            (
                "Otros síntomas",
                "Otros síntomas",
            ),
        ],
    )

    otros_sintomas = models.TextField(
        verbose_name="Otros Síntomas", null=True, blank=True
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

    tamanno_de_la_lesion = models.PositiveIntegerField(
        verbose_name="Tamaño de la lesión"
    )

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

    primer_apellido = models.CharField(
        verbose_name="Primer apellido",
        max_length=256,
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"), validate_noVacio],
    )

    segundo_apellido = models.CharField(
        verbose_name="Segundo apellido",
        max_length=256,
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"), validate_noVacio],
    )

    nombre_del_paciente = models.CharField(
        verbose_name="Nombre del paciente",
        max_length=256,
        validators=[RegexValidator(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"), validate_noVacio],
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
        verbose_name="Carné de identidad",
        max_length=11,
        validators=[RegexValidator(r"^[0-9]+$")],
    )

    historia_clinica_numero = models.PositiveIntegerField(
        verbose_name="Historia Clínica No", default=1, validators=[MinValueValidator(1)]
    )

    fecha_de_inscripcion = models.DateField(verbose_name="Fecha de inscripcion")

    creatinina = models.DecimalField(
        verbose_name="Creatinina",
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
    )

    hemoglobina = models.DecimalField(
        verbose_name="Hemoglobina",
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
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

    biopsia_numero = models.PositiveIntegerField(
        verbose_name="Biopsia No", default=1, validators=[MinValueValidator(1)]
    )

    fecha_de_diagnostico = models.DateField(verbose_name="Fecha de diagnóstico")

    diagnostico_topografico = models.CharField(
        verbose_name="Diagnóstico Topográfico", max_length=256
    )

    diagnostico_morfologico = models.CharField(
        verbose_name="Diagnóstico Morfológico", max_length=256
    )

    diagnosticado_en = models.CharField(verbose_name="Diagnóstico En", max_length=256)

    diagnostico_topografico_selecciona = models.CharField(
        verbose_name="Seleccione",
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

    diagnostico_morfologico_selecciona = models.CharField(
        verbose_name="Seleccione",
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

    diagnosticado_en_selecciona = models.CharField(
        verbose_name="Seleccione",
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

    grado_de_diferenciacion = models.CharField(
        verbose_name="Grado de diferenciación",
        max_length=256,
        choices=[
            (
                "Diferenciado",
                "Diferenciado",
            ),
            (
                "Indiferenciado",
                "Indiferenciado",
            ),
            (
                "Moderadamente diferenciado",
                "Moderadamente diferenciado",
            ),
            (
                "Poco diferenciado",
                "Poco diferenciado",
            ),
            (
                "No determinado",
                "No determinado",
            ),
            (
                "No procede",
                "No procede",
            ),
        ],
    )

    base_del_diagnostico = models.CharField(
        verbose_name="Base del diagnóstico",
        max_length=256,
        choices=[
            (
                "Desconocidas",
                "Desconocidas",
            ),
            (
                "E. clínico",
                "E. clínico",
            ),
            (
                "Inv. clínica",
                "Inv. clínica",
            ),
            (
                "Cirugía",
                "Cirugía",
            ),
            (
                "P. bio. Inmunológ",
                "P. bio. Inmunológ",
            ),
            (
                "Citología",
                "Citología",
            ),
            (
                "Citogenética",
                "Citogenética",
            ),
            (
                "Hematología",
                "Hematología",
            ),
            (
                "Histología",
                "Histología",
            ),
            (
                "Otras",
                "Otras",
            ),
        ],
    )

    otras = models.TextField(
        verbose_name="Otras",
        null=True,
        blank=True,
        help_text=" En csao de seleccionar Otras rellene este campo",
    )

    etapa_clinica = models.CharField(
        verbose_name="Etapa clínica",
        max_length=256,
        choices=[
            (
                "Desconocida",
                "Desconocida",
            ),
            (
                "In situ",
                "In situ",
            ),
            (
                "I",
                "I",
            ),
            (
                "Ia",
                "Ia",
            ),
            (
                "Ib",
                "Ib",
            ),
            (
                "Ic",
                "Ic",
            ),
            (
                "II",
                "II",
            ),
            (
                "IIa",
                "IIa",
            ),
            (
                "IIb",
                "IIb",
            ),
            (
                "IIc",
                "IIc",
            ),
            (
                "III",
                "III",
            ),
            (
                "IIIa",
                "IIIa",
            ),
            (
                "IIIb",
                "IIIb",
            ),
            (
                "IIIc",
                "IIIc",
            ),
            (
                "IV",
                "IV",
            ),
            (
                "IVa",
                "IVa",
            ),
            (
                "IVb",
                "IVb",
            ),
            (
                "IVc",
                "IVc",
            ),
            (
                "No procede",
                "No procede",
            ),
        ],
    )

    tnm_T = models.CharField(
        verbose_name="TNM T", max_length=256, blank=True, null=True
    )

    tnm_N = models.CharField(
        verbose_name="TNM N", max_length=256, blank=True, null=True
    )

    tnm_M = models.CharField(
        verbose_name="TNM M", max_length=256, blank=True, null=True
    )

    ptnm_pT = models.CharField(
        verbose_name="pTNM pT", max_length=256, blank=True, null=True
    )

    ptnm_pN = models.CharField(
        verbose_name="pTNM pN", max_length=256, blank=True, null=True
    )

    ptnm_pM = models.CharField(
        verbose_name="pTNM pM", max_length=256, blank=True, null=True
    )

    metastasis_a_distancia = models.CharField(
        verbose_name="Metástasis a distancia",
        max_length=256,
        choices=[
            (
                "Desconocida",
                "Desconocida",
            ),
            (
                "Ninguna",
                "Ninguna",
            ),
            (
                "Pulmón pleura",
                "Pulmón pleura",
            ),
            (
                "Hígado",
                "Hígado",
            ),
            (
                "Ovarios",
                "Ovarios",
            ),
            (
                "Hueso",
                "Hueso",
            ),
            (
                "Ganglios distales",
                "Ganglios distales",
            ),
            (
                "Cerebro",
                "Cerebro",
            ),
            (
                "Piel y TCS",
                "Piel y TCS",
            ),
        ],
    )

    extension_clinica = models.CharField(
        verbose_name="Extensión clínica",
        max_length=256,
        choices=[
            (
                "Desconocido",
                "Desconocido",
            ),
            (
                "In situ",
                "In situ",
            ),
            (
                "Ext. directa y linf. regionales",
                "Ext. directa y linf. regionales",
            ),
            (
                "Localizado",
                "Localizado",
            ),
            (
                "Metástasis a distancia",
                "Metástasis a distancia",
            ),
            (
                "Extensión directa",
                "Extensión directa",
            ),
            (
                "No aplicable",
                "No aplicable",
            ),
            (
                "Linfático regionales",
                "Linfático regionales",
            ),
        ],
    )

    en_otro_centro = models.CharField(
        verbose_name="En otro centro",
        max_length=256,
        choices=[
            (
                "No",
                "No",
            ),
            (
                "Parcial",
                "Parcial",
            ),
            (
                "Completo",
                "Completo",
            ),
        ],
    )

    en_la_institucion = models.CharField(
        verbose_name="En la institución",
        max_length=256,
        choices=[
            (
                "No",
                "No",
            ),
            (
                "Parcial",
                "Parcial",
            ),
            (
                "Completo",
                "Completo",
            ),
        ],
    )

    tratamiento_planificado = models.CharField(
        verbose_name="Tratamiento planificado",
        max_length=256,
        choices=[
            (
                "Desconocido",
                "Desconocido",
            ),
            (
                "Ninguno",
                "Ninguno",
            ),
            (
                "Radioterapia",
                "Radioterapia",
            ),
            (
                "Hormonoterapia",
                "Hormonoterapia",
            ),
            (
                "Cirugía",
                "Cirugía",
            ),
            (
                "Quimioterapia",
                "Quimioterapia",
            ),
            (
                "Inmunoterapia",
                "Inmunoterapia",
            ),
            (
                "Otro Tratamiento",
                "Otro Tratamiento",
            ),
        ],
    )

    otro_tratamiento_planificado = models.TextField(
        verbose_name="Que otro tratamiento se aplicó",
        null=True,
        blank=True,
        help_text=" En csao de seleccionar Otro rellene este campo",
    )

    inclusion_en_ec = models.BooleanField(verbose_name="Inclusión en EC", default=False)

    en_caso_de_si = models.CharField(
        verbose_name="En caso de ser sí; cuál es el código", max_length=256, null=True, blank=True
    )

    tratamiento_quirurgico = models.BooleanField(
        default=False,
        verbose_name="Tratamiento quirúrgico",
    )

    tipo_de_cirugia = models.TextField(
        verbose_name="Tipo de cirugía", null=True, blank=True
    )

    fecha_del_tratamiento_quirurgico = models.DateTimeField(
        null=True, blank=True, verbose_name="Fecha del tratamiento"
    )

    tratamiento_radioterapia = models.BooleanField(
        default=False,
        verbose_name="Tratamiento radioterapia",
    )

    tipo_de_tratamiento_radioterap = models.CharField(
        null=True,
        blank=True,
        verbose_name="Tipo de tratamiento radioterapeutico",
        max_length=256,
    )

    fecha_del_inicio_del_tratamiento_radioterapeutico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha del inicio del tratamiento radioterapeutico",
    )

    fecha_del_final_del_tratamiento_radioterapeutico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha del final del tratamiento radioterapeutico",
    )

    dosis_total = models.DecimalField(
        null=True,
        blank=True,
        verbose_name="Dosis total",
        decimal_places=2,
        max_digits=15,
        default=0,
    )

    gy_fraccion = models.DecimalField(
        null=True,
        blank=True,
        verbose_name="GY fracción",
        decimal_places=2,
        max_digits=15,
        default=0,
    )

    tratamiento_quimioterapia = models.BooleanField(
        default=False,
        verbose_name="Tratamiento quimioterapia",
    )

    esquema_tratamiento = models.CharField(
        null=True, blank=True, verbose_name="Esquema del tratamiento", max_length=256
    )

    numero_de_ciclos = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="No de ciclos", default=1
    )

    fecha_del_inicio_del_tratamiento_quimioterapeutico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha del inicio del tratamiento quimioterapeutico",
    )

    fecha_del_final_del_tratamiento_quimioterapeutico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha del final del tratamiento quimioterapeutico",
    )

    otro_tratamiento = models.BooleanField(
        default=False,
        verbose_name="Otro tratamiento",
    )

    cual_tratamiento = models.CharField(
        verbose_name="Cuál tratamiento", max_length=256, null=True, blank=True
    )

    fecha_del_inicio_del_tratamiento = models.DateField(
        null=True, blank=True, verbose_name="Fecha del inicio del tratamiento"
    )

    fecha_del_final_del_tratamiento = models.DateField(
        null=True, blank=True, verbose_name="Fecha del final del tratamiento"
    )

    evaluacion_de_la_respuesta = models.CharField(
        verbose_name="Evaluación de la respuesta",
        max_length=256,
        choices=[
            (
                "RC",
                "RC",
            ),
            (
                "RP",
                "RP",
            ),
            (
                "EE",
                "EE",
            ),
            (
                "EP",
                "EP",
            ),
            (
                "No procede",
                "No procede",
            ),
        ],
    )

    fecha_evaluacion = models.DateField(
        verbose_name="Fecha",
    )

    observaciones = models.TextField(
        verbose_name="Observaciones", null=True, blank=True
    )

    nombre_del_medico = models.CharField(verbose_name="Médico", max_length=256)

    registro_profesional = models.CharField(
        max_length=4,
        validators=[RegexValidator(r"^[0-9]{4}$")],
        verbose_name="Registro profesional",
    )

    def clean(self):
        super().clean()
        if self.base_del_diagnostico == "Otras" and esta_vacio(self.otras):
            raise ValidationError("En csao de seleccionar Otras rellene este campo 11")
        if self.tratamiento_planificado == "Otro" and esta_vacio(
            self.otro_tratamiento_planificado
        ):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 22")
        if self.inclusion_en_ec == True and esta_vacio(self.en_caso_de_si):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 33")
        if self.otro_tratamiento == True and esta_vacio(self.cual_tratamiento):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 44")

        if self.tratamiento_quirurgico == True and (
            esta_vacio(self.tipo_de_cirugia) or self.fecha is None
        ):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 55")
        if self.tratamiento_radioterapia == True and (
            self.fecha_del_final_del_tratamiento_radioterapeutico is None
            or self.fecha_del_inicio_del_tratamiento_radioterapeutico is None
            or esta_vacio(self.tipo_de_tratamiento_radioterap)
            or self.gy_fraccion is None
            or self.dosis_total is None
        ):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 66")
        if (
            self.fecha_del_final_del_tratamiento_radioterapeutico
            and self.fecha_del_inicio_del_tratamiento_radioterapeutico
        ):
            if (
                self.fecha_del_final_del_tratamiento_radioterapeutico
                <= self.fecha_del_inicio_del_tratamiento_radioterapeutico
            ):
                raise ValidationError(
                    "La fecha de inicio debe ser inferior a la fecha de fin 77"
                )
        if (
            self.fecha_del_final_del_tratamiento_quimioterapeutico
            and self.fecha_del_inicio_del_tratamiento_quimioterapeutico
        ):
            if (
                self.fecha_del_final_del_tratamiento_quimioterapeutico
                <= self.fecha_del_inicio_del_tratamiento_quimioterapeutico
            ):
                raise ValidationError(
                    "La fecha de inicio debe ser inferior a la fecha de fin 88"
                )
        if (
            self.fecha_del_final_del_tratamiento
            and self.fecha_del_inicio_del_tratamiento
        ):
            if (
                self.fecha_del_final_del_tratamiento
                <= self.fecha_del_inicio_del_tratamiento
            ):
                raise ValidationError(
                    "La fecha de inicio debe ser inferior a la fecha de fin 99"
                )
        if self.tratamiento_quimioterapia == True and (
            self.fecha_del_final_del_tratamiento_quimioterapeutico is None
            or self.fecha_del_inicio_del_tratamiento_quimioterapeutico is None
            or esta_vacio(self.esquema_tratamiento)
            or self.numero_de_ciclos is None
        ):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 00")

        if self.otro_tratamiento == True and (
            self.fecha_del_final_del_tratamiento is None
            or self.fecha_del_inicio_del_tratamiento is None
            or esta_vacio(self.cual_tratamiento)
        ):
            raise ValidationError("En csao de seleccionar Otro rellene este campo 101")


def esta_vacio(valor):
    return (not valor) or len(str(valor).strip()) == 0
