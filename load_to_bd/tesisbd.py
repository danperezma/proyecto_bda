import csv
import mysql.connector
from datetime import datetime
import os
# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="proyecto"
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos MySQL")
    # Crear cursor
    cursor = conexion.cursor()

    # Nombre del archivo CSV
    archivo_csv = os.path.join("..", "tesis.csv")


    # Consulta para insertar datos en la tabla
    consulta = "INSERT INTO tesis (idEstudiante,idPrograma,nombreDirector,nombre, fechaPublicacion,tema) VALUES (%s, %s, %s, %s, %s, %s)"

    # Leer datos del archivo CSV e insertarlos en la base de datos
    with open(archivo_csv, newline="", encoding="utf-8") as csvfile:
        lector_csv = csv.DictReader(csvfile)
        for fila in lector_csv:
            # Suponiendo que tus columnas en la tabla se llaman igual que las columnas en el CSV
            # print(fila["fechaPublicacion"])
            datos = (fila['idEstudiante'], fila['idPrograma'], fila['nombreDirector'], fila['nombre'], datetime.strptime(fila['fechaPublicacion'], "%m/%d/%Y").strftime("%Y-%m-%d"), fila['tema'])  # Ajusta esto según la estructura de tu tabla
            cursor.execute(consulta, datos)

    # Confirmar la transacción
    conexion.commit()
    print("Datos insertados correctamente.")

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()
else:
    print("No se pudo conectar a la base de datos MySQL")
