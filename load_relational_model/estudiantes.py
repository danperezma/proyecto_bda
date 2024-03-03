import csv
from datetime import datetime
from dbConnection import conexion
from loadBD import logger


def load_data():
    try:
        logger.info("Load student data started")

        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            logger.info("Conexión exitosa a la base de datos MySQL")
            # Crear cursor
            cursor = conexion.cursor()

            # Nombre del archivo CSV
            archivo_csv = "data_nuevo.csv"

            # Consulta para insertar datos en la tabla
            consulta = "INSERT INTO estudiante (idEstudiante, nombre, genero, email, telefono, fechaNacimiento) VALUES (%s, %s, %s, %s, %s, %s)"

            # Leer datos del archivo CSV e insertarlos en la base de datos
            with open(archivo_csv, newline="", encoding="utf-8") as csvfile:
                lector_csv = csv.DictReader(csvfile)
                for fila in lector_csv:
                    # Suponiendo que tus columnas en la tabla se llaman igual que las columnas en el CSV
                    datos = (fila['idEstudiante'], fila['nombre'], fila['sexo'], fila['email'], fila['telefono'], datetime.strptime(
                        fila['fechaNacimiento'], "%m/%d/%Y").strftime("%Y-%m-%d"))  # Ajusta esto según la estructura de tu tabla
                    cursor.execute(consulta, datos)

            # Confirmar la transacción
            conexion.commit()
            logger.info("Datos insertados correctamente.")

            # Cerrar cursor y conexión
            cursor.close()
            conexion.close()
        else:
            logger.error("No se pudo conectar a la base de datos MySQL")
    except Exception as e:
        logger.error(f"Error during student data loading: {e}")
