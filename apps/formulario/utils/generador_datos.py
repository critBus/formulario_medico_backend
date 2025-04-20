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
        fecha_evaluacion = fake.date_between(start_date=fecha_diagnostico, end_date='today')
        
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
        
        # Generar datos de imágenes
        opciones_imagen = ['Ninguno', 'Positivo', 'Negativo']
        imagen_rx_torax = random.choice(opciones_imagen)
        imagen_us_abdomen = random.choice(opciones_imagen)
        imagen_tac_cavidad_oral = random.choice(opciones_imagen)
        otros_tac_faringe = random.choice(opciones_imagen)
        otros_tac_cuello = random.choice(opciones_imagen)
        otros_tac_torax = random.choice(opciones_imagen)
        otros_rmn = random.choice(opciones_imagen)
        
        # Generar datos de localización
        localizacion_en_labio = random.choice([
            'Labio superior', 'Mucosa superior', 'Comisuras labiales',
            'Labio inferior', 'Mucosa inferior'
        ])
        lengua_movil = random.choice([
            'Cara central', 'Cara dorsal', 'Punta', 'Borde'
        ])
        suelo_de_Boca = random.choice(['Parte anterior', 'Parte lateral'])
        encia = random.choice(['Superior', 'Inferior'])
        otras_partes_del_a_boca = random.choice([
            'Carrillo', 'Vesíbulo', 'Paladar duro', 'Espacio retromolar'
        ])
        glandulas_salibales = random.choice([
            'Parótida', 'Sublingual', 'Submaxilar', 'Otra'
        ])
        
        # Generar datos de adenopatía
        niveles_adenopatia = ['No', 'Nivel I', 'Nivel II', 'Nivel III', 'Nivel IV', 'Nivel V']
        ardenopatia_cervical_derecha = random.choice(niveles_adenopatia)
        ardenopatia_cervical_izquierda = random.choice(niveles_adenopatia)
        
        # Generar datos de extensión clínica
        extension_clinica_a = random.choice([
            'No', 'Suelo de boca', 'Laringe', 'Labio', 'Otras partes de la cavidad oral',
            'Mesofaringe', 'Hipofaringe', 'Encía', 'Nasofaringe', 'Piel y partes blandas',
            'Hueso', 'Otras'
        ])
        
        # Generar datos de performance status
        performance_status = random.choice(['0', '1', '2', '3', '4'])
        
        # Generar datos de TNM
        tnm_values = ['T1', 'T2', 'T3', 'T4', 'N0', 'N1', 'N2', 'N3', 'M0', 'M1']
        tnm_T = random.choice(tnm_values)
        tnm_N = random.choice(tnm_values)
        tnm_M = random.choice(tnm_values)
        ptnm_pT = random.choice(tnm_values)
        ptnm_pN = random.choice(tnm_values)
        ptnm_pM = random.choice(tnm_values)
        
        # Generar datos de metástasis
        metastasis_a_distancia = random.choice([
            'Desconocida', 'Ninguna', 'Pulmón pleura', 'Hígado', 'Ovarios',
            'Hueso', 'Ganglios distales', 'Cerebro', 'Piel y TCS'
        ])
        
        # Generar datos de extensión clínica
        extension_clinica = random.choice([
            'Desconocido', 'In situ', 'Ext. directa y linf. regionales',
            'Localizado', 'Metástasis a distancia', 'Extensión directa',
            'No aplicable', 'Linfático regionales'
        ])
        
        # Generar datos de tratamiento
        tratamiento_planificado = random.choice([
            'Desconocido', 'Ninguno', 'Radioterapia', 'Hormonoterapia',
            'Cirugía', 'Quimioterapia', 'Inmunoterapia', 'Otro Tratamiento'
        ])
        
        # Generar datos de inclusión en EC
        inclusion_en_ec = random.choice([True, False])
        en_caso_de_si = fake.word() if inclusion_en_ec else None
        
        # Generar datos de tratamiento quirúrgico
        tratamiento_quirurgico = random.choice([True, False])
        tipo_de_cirugia = fake.sentence() if tratamiento_quirurgico else None
        fecha_del_tratamiento_quirurgico = fake.date_between(start_date=fecha_diagnostico, end_date='today') if tratamiento_quirurgico else None
        
        # Generar datos de radioterapia
        tratamiento_radioterapia = random.choice([True, False])
        tipo_de_tratamiento_radioterap = fake.word() if tratamiento_radioterapia else None
        fecha_inicio_radioterapia = fake.date_between(start_date=fecha_diagnostico, end_date='today') if tratamiento_radioterapia else None
        fecha_fin_radioterapia = fake.date_between(start_date=fecha_inicio_radioterapia, end_date='today') if tratamiento_radioterapia else None
        dosis_total = round(random.uniform(20.0, 80.0), 2) if tratamiento_radioterapia else None
        gy_fraccion = round(random.uniform(1.0, 3.0), 2) if tratamiento_radioterapia else None
        
        # Generar datos de quimioterapia
        tratamiento_quimioterapia = random.choice([True, False])
        esquema_tratamiento = fake.word() if tratamiento_quimioterapia else None
        numero_de_ciclos = random.randint(1, 12) if tratamiento_quimioterapia else None
        fecha_inicio_quimio = fake.date_between(start_date=fecha_diagnostico, end_date='today') if tratamiento_quimioterapia else None
        fecha_fin_quimio = fake.date_between(start_date=fecha_inicio_quimio, end_date='today') if tratamiento_quimioterapia else None
        
        # Generar datos de otro tratamiento
        otro_tratamiento = random.choice([True, False])
        cual_tratamiento = fake.word() if otro_tratamiento else None
        fecha_inicio_otro = fake.date_between(start_date=fecha_diagnostico, end_date='today') if otro_tratamiento else None
        fecha_fin_otro = fake.date_between(start_date=fecha_inicio_otro, end_date='today') if otro_tratamiento else None
        
        # Generar datos de evaluación
        evaluacion_de_la_respuesta = random.choice(['RC', 'RP', 'EE', 'EP', 'No procede'])
        
        # Crear el formulario
        formulario = Formulario.objects.create(
            nombre=f"Formulario {fake.unique.random_number(digits=5)}",
            fecha=fecha_aleatoria,
            fecha_de_diagnostico=fecha_diagnostico,
            fecha_evaluacion=fecha_evaluacion,
            remision=random.choice(['No remitido', 'Atención primaria', 'Programa de control', 'Atención secundaria']),
            historia_clinica=random.choice([True, False]),
            motivo_consulta=random.choice([
                'Aparición de lesión', 'Aumento de volumen', 'Nódulo cervical', 'Sangramiento',
                'Odinofagia', 'Sialorrea', 'Dolor', 'Parálisis facial', 'Otros síntomas'
            ]),
            otros_sintomas=fake.text() if random.choice([True, False]) else None,
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
            localizacion_en_labio=localizacion_en_labio,
            lengua_movil=lengua_movil,
            suelo_de_Boca=suelo_de_Boca,
            encia=encia,
            otras_partes_del_a_boca=otras_partes_del_a_boca,
            glandulas_salibales=glandulas_salibales,
            ardenopatia_cervical_derecha=ardenopatia_cervical_derecha,
            ardenopatia_cervical_izquierda=ardenopatia_cervical_izquierda,
            extension_clinica_a=extension_clinica_a,
            performance_status=performance_status,
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
            imagen_rx_torax=imagen_rx_torax,
            imagen_us_abdomen=imagen_us_abdomen,
            imagen_tac_cavidad_oral=imagen_tac_cavidad_oral,
            otros_tac_faringe=otros_tac_faringe,
            otros_tac_cuello=otros_tac_cuello,
            otros_tac_torax=otros_tac_torax,
            otros_rmn=otros_rmn,
            biopsia_numero=random.randint(1, 9999),
            diagnostico_topografico=diagnostico_topografico,
            diagnostico_morfologico=diagnostico_morfologico,
            diagnosticado_en=diagnosticado_en,
            diagnostico_topografico_selecciona=random.choice(['Ninguno', 'Positivo', 'Negativo']),
            diagnostico_morfologico_selecciona=random.choice(['Ninguno', 'Positivo', 'Negativo']),
            diagnosticado_en_selecciona=random.choice(['Ninguno', 'Positivo', 'Negativo']),
            grado_de_diferenciacion=random.choice([
                'Diferenciado', 'Indiferenciado', 'Moderadamente diferenciado',
                'Poco diferenciado', 'No determinado', 'No procede'
            ]),
            base_del_diagnostico=random.choice([
                'Desconocidas', 'E. clínico', 'Inv. clínica', 'Cirugía',
                'P. bio. Inmunológ', 'Citología', 'Citogenética', 'Hematología',
                'Histología', 'Otras'
            ]),
            otras=fake.text() if random.choice([True, False]) else None,
            etapa_clinica=random.choice([
                'Desconocida', 'In situ', 'I', 'Ia', 'Ib', 'Ic', 'II', 'IIa',
                'IIb', 'IIc', 'III', 'IIIa', 'IIIb', 'IIIc', 'IV', 'IVa',
                'IVb', 'IVc', 'No procede'
            ]),
            tnm_T=tnm_T,
            tnm_N=tnm_N,
            tnm_M=tnm_M,
            ptnm_pT=ptnm_pT,
            ptnm_pN=ptnm_pN,
            ptnm_pM=ptnm_pM,
            metastasis_a_distancia=metastasis_a_distancia,
            extension_clinica=extension_clinica,
            en_otro_centro=random.choice(['No', 'Parcial', 'Completo']),
            en_la_institucion=random.choice(['No', 'Parcial', 'Completo']),
            tratamiento_planificado=tratamiento_planificado,
            otro_tratamiento_planificado=fake.text() if tratamiento_planificado == 'Otro Tratamiento' else None,
            inclusion_en_ec=inclusion_en_ec,
            en_caso_de_si=en_caso_de_si,
            tratamiento_quirurgico=tratamiento_quirurgico,
            tipo_de_cirugia=tipo_de_cirugia,
            fecha_del_tratamiento_quirurgico=fecha_del_tratamiento_quirurgico,
            tratamiento_radioterapia=tratamiento_radioterapia,
            tipo_de_tratamiento_radioterap=tipo_de_tratamiento_radioterap,
            fecha_del_inicio_del_tratamiento_radioterapeutico=fecha_inicio_radioterapia,
            fecha_del_final_del_tratamiento_radioterapeutico=fecha_fin_radioterapia,
            dosis_total=dosis_total,
            gy_fraccion=gy_fraccion,
            tratamiento_quimioterapia=tratamiento_quimioterapia,
            esquema_tratamiento=esquema_tratamiento,
            numero_de_ciclos=numero_de_ciclos,
            fecha_del_inicio_del_tratamiento_quimioterapeutico=fecha_inicio_quimio,
            fecha_del_final_del_tratamiento_quimioterapeutico=fecha_fin_quimio,
            otro_tratamiento=otro_tratamiento,
            cual_tratamiento=cual_tratamiento,
            fecha_del_inicio_del_tratamiento=fecha_inicio_otro,
            fecha_del_final_del_tratamiento=fecha_fin_otro,
            evaluacion_de_la_respuesta=evaluacion_de_la_respuesta,
            observaciones=fake.text() if random.choice([True, False]) else None,
            nombre_del_medico=fake.name(),
            registro_profesional=fake.numerify('####')
        )
        
        formularios.append(formulario)
    
    return formularios 