import csv
import os
from loadBD import logger, conexion


def load_data():
    try:
        logger.info("Load PASANTIA data started")

        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            logger.info("Conexión exitosa a la base de datos MySQL")
            # Crear cursor
            cursor = conexion.cursor()

            # Nombre del archivo CSV
            archivo_csv = os.path.join("..", "pasantia.csv")

            # Consulta para insertar datos en la tabla
            consulta = "INSERT INTO pasantia (idEstudiante,idPrograma,nombreSupervisor,empresa,duracionContrato) VALUES (%s, %s, %s, %s, %s)"

            # Leer datos del archivo CSV e insertarlos en la base de datos
            with open(archivo_csv, newline="", encoding="utf-8") as csvfile:
                lector_csv = csv.DictReader(csvfile)
                for fila in lector_csv:
                    # Suponiendo que tus columnas en la tabla se llaman igual que las columnas en el CSV
                    datos = (fila['idEstudiante'], fila['idPrograma'], fila['nombreSupervisor'],
                             fila['empresa'], fila['duracionContrato'])  # Ajusta esto según la estructura de tu tabla
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
        logger.error(f"Error during internship data loading: {e}")
