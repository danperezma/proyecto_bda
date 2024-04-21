from faker import Faker
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from const import programas
import os
import random

load_dotenv()

fake = Faker()

def insertar_publicacion(publicacion):
    cliente = MongoClient(os.getenv('MONGODB_URI'))
    db = cliente['testdb']
    coleccion_publicacion = db['publicacion']
    coleccion_publicacion.insert_one(publicacion)
    # print(publicacion)

# Generar datos para estudiantes
def generar_datos_estudiante():
    estudiante = {
        "nombre": fake.name(),
        "email": fake.email(),
        "fechaNacimiento": fake.date_of_birth(minimum_age=18, maximum_age=25).strftime('%Y-%m-%d'),
        "género": random.choice(["masculino", "femenino", "prefiere no decir"]),
        "númeroTeléfono": fake.phone_number(),
        "estrato": random.randint(1, 6),
        "localidad": fake.city(),
        "historialAcadémico": [],
        # "educaciónAdicional": [],
        "proyectoGraduación": {}
    }


    # Generar historial académico
    for _ in range(random.choice(([1] * 15) + [2])):
        facultad = random.choice(programas["facultades"])
        departamento = random.choice(facultad["departamentos"])
        programa = random.choice(departamento["carreras"])
        nombre_programa = programa["nombre"]

        registro_académico = {
            "programa": nombre_programa,
            "idCarrera": programa["id"],
            "materias": []
        }
    for materia in programa["materias"]:
        nota = round(random.uniform(2.7, 5.0), 2)  # Generar nota entre 2.7 y 5.0
        registro_académico["materias"].append({"nombre": materia, "nota": nota})
    estudiante["historialAcadémico"].append(registro_académico)

    estudiante["proyectoGraduación"] = []
    # Generar proyecto de graduación
    for i in range(len(estudiante["historialAcadémico"])):
        tipo_proyecto = random.choice(["publicación", "práctica profesional", "bapi"])
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
                "materiasBapi": [ random.choice(estudiante["historialAcadémico"][i]["materias"])["nombre"] for _ in range(random.randint(1, 3))]
            }
    
    estudiante["proyectoGraduación"].append(proyecto_graduación)

    return estudiante

# Insertar datos de ejemplo en la base de datos
def insertar_datos_estudiante(coleccion, num_docs):
    datos = []
    for _ in range(num_docs):
        datos.append(generar_datos_estudiante())
    print(datos)
    coleccion.insert_many(datos)

if __name__ == "__main__":
    # Inicializar cliente de MongoDB
    cliente = MongoClient(os.getenv('MONGODB_URI')) 
    db = cliente['testdb']
    db['estudiante'].delete_many({})
    db['publicacion'].delete_many({})
    coleccion_estudiante = db['estudiante']
    insertar_datos_estudiante(coleccion_estudiante, 10)
    print("Datos de estudiantes insertados correctamente en la base de datos MongoDB.")
