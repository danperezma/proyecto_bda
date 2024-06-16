import os
import csv
from datetime import datetime
from dbConnection import conexion
from logger import log


def load_data():
    try:
        log("info", "Load student data started", None)

        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            # Crear cursor
            cursor = conexion.cursor()

            # Nombre del archivo CSV
            archivo_csv = os.path.join("../data/", "data_nuevo.csv")

            # Consulta para insertar datos en la tabla
            consulta = "INSERT INTO estudiante (idEstudiante, nombre, genero, email, telefono, fechaNacimiento) VALUES (%s, %s, %s, %s, %s, %s)"

            # Leer datos del archivo CSV e insertarlos en la base de datos
            with open(archivo_csv, newline="", encoding="utf-8") as csvfile:
                lector_csv = csv.DictReader(csvfile)
                for fila in lector_csv:
                    # Suponiendo que tus columnas en la tabla se llaman igual que las columnas en el CSV
                    datos = (fila['idEstudiante'], fila['nombre'], fila['sexo'], fila['email'], fila['telefono'], datetime.strptime(
                        # Ajusta esto según la estructura de tu tabla
                        fila['fechaNacimiento'], "%m/%d/%Y").strftime("%Y-%m-%d"))
                    cursor.execute(consulta, datos)

            # Confirmar la transacción
            conexion.commit()
            log("info", "Load student data finished", None)

            # Cerrar cursor y conexión
            cursor.close()
        else:
            log("error", "Failed to connect to the database", None)
    except Exception as e:
        log("error", f"Error during student data loading, {e}", str(e))
