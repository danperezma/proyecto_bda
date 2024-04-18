from faker import Faker
from pymongo import MongoClient
from dotenv import load_dotenv
from const import programas
import os
import random

load_dotenv()

# Inicializar Faker
fake = Faker()

# Generar datos para profesores
def generar_datos_profesor():
    facultad = random.choice(programas["facultades"])
    nombre_facultad = facultad["nombre"]

    # Escoger aleatoriamente un departamento dentro de la facultad seleccionada
    departamento = random.choice(facultad["departamentos"])
    nombre_departamento = departamento["nombre"]
    profesor = {
        "nombre": fake.name(),
        "email": fake.email(),
        "fechaNacimiento": fake.date_of_birth(minimum_age=25, maximum_age=65).strftime('%Y-%m-%d'),
        "género": random.choice(["masculino", "femenino", "prefiere no decir"]),
        "númeroTeléfono": fake.phone_number(),
        "estrato": random.randint(1, 6),
        "localidad": fake.city(),
        "departamento": nombre_departamento,
        "facultad": nombre_facultad,
        "tipoContrato": random.choice(["tiempo completo", "ocasional", "catedratico"])
    }
    return profesor

# Insertar datos de ejemplo en la base de datos
def insertar_datos_profesor(coleccion, num_docs):
    datos = []
    for _ in range(num_docs):
        datos.append(generar_datos_profesor())
    print(datos)
    coleccion.insert_many(datos)

if __name__ == "__main__":
    # Inicializar cliente de MongoDB
    cliente = MongoClient(os.getenv('MONGODB_URI'))
    db = cliente['testdb']
    coleccion_profesor = db['profesor']
    coleccion_profesor.delete_many({})
    insertar_datos_profesor(coleccion_profesor, 5)
    # print("Datos de profesores insertados correctamente en la base de datos MongoDB.")
