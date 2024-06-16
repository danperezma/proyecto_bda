from faker import Faker
from pymongo import MongoClient
from dotenv import load_dotenv
from const import programas
from datetime import datetime
import os
import random
from logger import log
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
        "fechaNacimiento": datetime.combine(fake.date_of_birth(minimum_age=27, maximum_age=65), datetime.min.time()),
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
    log("info", "Iniciando proceso de generación de datos de profesores")

    datos = []
    for _ in range(num_docs):
        profesor = generar_datos_profesor()
        datos.append(profesor)

    log("info", f"Generados {num_docs} registros de datos de profesores")
    print(datos)  # Opcional: Imprimir datos en la consola

    log("info", f"Insertando datos de profesores en la colección '{
        coleccion.name}'")
    coleccion.insert_many(datos)

    log("info", "Inserción de datos de profesores completada")


if __name__ == "__main__":
    # Inicializar cliente de MongoDB
    log("info", "Inicializando cliente de MongoDB")
    cliente = MongoClient(os.getenv('MONGODB_URI'))
    db = cliente['testdb']
    coleccion_profesor = db['profesor']
    log("info", "Cliente de MongoDB inicializado correctamente")

    # Eliminar datos existentes en la colección
    log("info", "Eliminando datos existentes en la colección 'profesor'")
    coleccion_profesor.delete_many({})
    log("info", "Eliminación de datos completada")

    # Insertar datos de ejemplo
    insertar_datos_profesor(coleccion_profesor, 5)

    # Cerrar conexión a MongoDB
    log("info", "Cerrando conexión a MongoDB")
    cliente.close()
    log("info", "Conexión a MongoDB cerrada")
