from faker import Faker
from ..models import Formulario
import random
from datetime import datetime, timedelta

fake = Faker('es_ES')

def generar_datos_aleatorios(cantidad=1):
    """
    Genera datos aleatorios para el modelo Formulario.
    
    Args:
        cantidad (int): Cantidad de registros a generar. Por defecto es 1.
        
    Returns:
        list: Lista de objetos Formulario creados
    """
    formularios = []
    
    for _ in range(cantidad):
        # Generar fechas aleatorias
        fecha_actual = datetime.now()
        fecha_aleatoria = fake.date_between(start_date='-5y', end_date='today')
        fecha_inscripcion = fake.date_between(start_date='-1y', end_date='today')
        fecha_diagnostico = fake.date_between(start_date=fecha_inscripcion, end_date='today')
        
        # Generar datos del paciente
        primer_apellido = fake.last_name()
        segundo_apellido = fake.last_name()
        nombre_paciente = fake.first_name()
        sexo = random.choice(['Femenino', 'Masculino'])
        edad = random.randint(18, 90)
        color_piel = random.choice(['Blanca', 'Negra', 'Mestiza'])
        carne_identidad = fake.numerify('###########')
        historia_clinica_numero = random.randint(1, 9999)
        
        # Generar datos médicos
        creatinina = round(random.uniform(0.5, 2.0), 2)
        hemoglobina = round(random.uniform(10.0, 18.0), 2)
        
        # Generar datos de diagnóstico
        diagnostico_topografico = fake.word()
        diagnostico_morfologico = fake.word()
        diagnosticado_en = fake.company()
        
        # Crear el formulario
        formulario = Formulario.objects.create(
            nombre=f"Formulario {fake.unique.random_number(digits=5)}",
            fecha=fecha_aleatoria,
            fecha_de_diagnostico=fecha_diagnostico,
            fecha_evaluacion=fecha_aleatoria,
            remision=random.choice(['No remitido', 'Atención primaria', 'Programa de control', 'Atención secundaria']),
            historia_clinica=random.choice([True, False]),
            motivo_consulta=random.choice([
                'Aparición de lesión', 'Aumento de volumen', 'Nódulo cervical', 'Sangramiento',
                'Odinofagia', 'Sialorrea', 'Dolor', 'Parálisis facial', 'Otros síntomas'
            ]),
            primer_sintoma=fake.word(),
            tiempo_de_aparicion=random.choice(['Días', 'Meses', 'Años']),
            personales_de_riesgo=random.choice([
                'Ninguno', 'Tabaquismo', 'Exposición a irritantes', 'Ingestión bebidas alcohólicas',
                'Trauma región de la lesión', 'Mala higiene bucal', 'Uso de prótesis'
            ]),
            personales_patologicos=random.choice([
                'Ninguno', 'Leucoplasias', 'Queratosis', 'Avitaminosis', 'Tuberculosis',
                'Sífilis', 'Infección crónica', 'VIH', 'Neoplasia maligna'
            ]),
            familiares_con_cancer=random.choice(['Si', 'No', 'Desconocido']),
            caracteristicas_de_la_lesion=random.choice([
                'Vegetante', 'Infiltrante', 'Úlcero-vegetante', 'Úlcero-infiltrante',
                'Necrosante', 'Plana', 'Submucosa', 'Nodular'
            ]),
            region=random.choice(['Derecha', 'Central', 'Izquierda']),
            tamanno_de_la_lesion=random.randint(1, 10),
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            nombre_del_paciente=nombre_paciente,
            sexo=sexo,
            edad=edad,
            color_de_piel=color_piel,
            carne_de_identidad=carne_identidad,
            historia_clinica_numero=historia_clinica_numero,
            fecha_de_inscripcion=fecha_inscripcion,
            creatinina=creatinina,
            hemoglobina=hemoglobina,
            diagnostico_topografico=diagnostico_topografico,
            diagnostico_morfologico=diagnostico_morfologico,
            diagnosticado_en=diagnosticado_en,
            grado_de_diferenciacion=random.choice([
                'Diferenciado', 'Indiferenciado', 'Moderadamente diferenciado',
                'Poco diferenciado', 'No determinado', 'No procede'
            ]),
            base_del_diagnostico=random.choice([
                'Desconocidas', 'E. clínico', 'Inv. clínica', 'Cirugía',
                'P. bio. Inmunológ', 'Citología', 'Citogenética', 'Hematología',
                'Histología', 'Otras'
            ]),
            etapa_clinica=random.choice([
                'Desconocida', 'In situ', 'I', 'Ia', 'Ib', 'Ic', 'II', 'IIa',
                'IIb', 'IIc', 'III', 'IIIa', 'IIIb', 'IIIc', 'IV', 'IVa',
                'IVb', 'IVc', 'No procede'
            ]),
            nombre_del_medico=fake.name(),
            registro_profesional=fake.numerify('####')
        )
        
        formularios.append(formulario)
    
    return formularios 