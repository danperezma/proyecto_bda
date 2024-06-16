from faker import Faker
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from datetime import datetime
from const import programas
import os
import random
from logger import log

load_dotenv()

fake = Faker()


def insertar_publicacion(publicacion):
    log("info", f"Inserting publication: {publicacion}")
    try:
        cliente = MongoClient(os.getenv('MONGODB_URI'))
        db = cliente['testdb']
        coleccion_publicacion = db['publicacion']
        coleccion_publicacion.insert_one(publicacion)
        log("info", f"Publication inserted successfully: {publicacion}")
    except Exception as error:
        log("error", f"Error during publication insertion: {error}")

# Generar datos para estudiantes


def generar_datos_estudiante():
    log("info", "Generating student data")
    estudiante = {
        "nombre": fake.name(),
        "email": fake.email(),
        "fechaNacimiento": datetime.combine(fake.date_of_birth(minimum_age=18, maximum_age=25), datetime.min.time()),
        "género": random.choice(["masculino", "femenino", "prefiere no decir"]),
        "númeroTeléfono": fake.phone_number(),
        "estrato": random.randint(1, 6),
        "localidad": fake.city(),
        "historialAcadémico": [],
        "proyectoGraduación": {}
    }

    log("debug", f"Initial student data: {estudiante}")

    # Generar historial académico
    for _ in range(random.choice(([1] * 15) + [2])):
        facultad = random.choice(programas["facultades"])
        departamento = random.choice(facultad["departamentos"])
        programa = random.choice(departamento["carreras"])
        nombre_programa = programa["nombre"]

        registro_académico = {
            "facultad": facultad["nombre"],
            "departamento": departamento["nombre"],
            "programa": nombre_programa,
            "fechaGraduacion": estudiante["fechaNacimiento"].replace(year=estudiante["fechaNacimiento"].year + random.randint(20, 35)),
            "idCarrera": programa["id"],
            "materias": []
        }

        for materia in programa["materias"]:
            # Generar nota entre 2.7 y 5.0
            nota = round(random.uniform(2.7, 5.0), 2)
            registro_académico["materias"].append(
                {"nombre": materia, "nota": nota})

        estudiante["historialAcadémico"].append(registro_académico)

    log("debug", f"Student academic history: {
        estudiante['historialAcadémico']}")

    estudiante["proyectoGraduación"] = []
    # Generar proyecto de graduación
    for i in range(len(estudiante["historialAcadémico"])):
        tipo_proyecto = random.choice(
            ["publicación", "práctica profesional", "bapi"])
        if tipo_proyecto == "publicación":
            publicacion = {
                "id": fake.random_int(min=1, max=1000),
                "revista": fake.company(),
                "tema": fake.catch_phrase(),
                "formato": fake.random_element(elements=("artículo", "libro", "ponencia"))
            }
            insertar_publicacion(publicacion)
            proyecto_graduación = {
                "tipo": "publicación",
                "programa": estudiante["historialAcadémico"][i]["programa"],
                "nota": round(random.uniform(3.0, 5.0), 2),
                "idPublicación": publicacion["id"],
                "tema": publicacion["tema"],
            }
        elif tipo_proyecto == "práctica profesional":
            proyecto_graduación = {
                "tipo": "práctica profesional",
                "programa": estudiante["historialAcadémico"][i]["programa"],
                "organización": fake.company(),
                "salario": round(random.uniform(100, 1000), 2),
                "posición": fake.job()
            }
        elif tipo_proyecto == "bapi":
            proyecto_graduación = {
                "tipo": "bapi",
                "programa": estudiante["historialAcadémico"][i]["programa"],
                "pais": fake.country(),
                "materiasBapi": [random.choice(estudiante["historialAcadémico"][i]["materias"])["nombre"] for _ in range(random.randint(1, 3))]
            }

        estudiante["proyectoGraduación"].append(proyecto_graduación)

    log("debug", f"Student graduation project: {
        estudiante['proyectoGraduación']}")
    return estudiante

# Insertar datos de ejemplo en la base de datos


def insertar_datos_estudiante(coleccion, num_docs):
    log("info", f"Inserting {num_docs} student records into the database")
    datos = []
    for _ in range(num_docs):
        datos.append(generar_datos_estudiante())
    try:
        coleccion.insert_many(datos)
        log("info", "Student data inserted successfully")
    except Exception as error:
        log("error", f"Error during student data insertion: {error}")


if __name__ == "__main__":
    log("info", "Initializing MongoDB client")
    try:
        cliente = MongoClient(os.getenv('MONGODB_URI'))
        db = cliente['testdb']
        db['estudiante'].delete_many({})
        db['publicacion'].delete_many({})
        coleccion_estudiante = db['estudiante']
        insertar_datos_estudiante(coleccion_estudiante, 10)
        log("info", "Student data inserted successfully into MongoDB")
    except Exception as error:
        log("error", f"Error during MongoDB operations: {error}")
