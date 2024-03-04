import os
import csv
from dbConnection import conexion
from logger import logger


def load_data():
    logger.info("Loading BAPI data started")
    try:
        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            # Crear cursor
            cursor = conexion.cursor()

            # Nombre del archivo CSV
            archivo_csv = os.path.join("../data/", "bapi.csv")

            # Consulta para insertar datos en la tabla
            consulta = "INSERT INTO bapi (idEstudiante, idPrograma) VALUES (%s, %s)"

            # Leer datos del archivo CSV e insertarlos en la base de datos
            with open(archivo_csv, newline="", encoding="utf-8") as csvfile:
                lector_csv = csv.DictReader(csvfile)
                for fila in lector_csv:
                    # Suponiendo que tus columnas en la tabla se llaman igual que las columnas en el CSV
                    # print(fila["fechaPublicacion"])
                    # Ajusta esto según la estructura de tu tabla
                    datos = (fila['idEstudiante'], fila['idPrograma'])
                    cursor.execute(consulta, datos)

            # Confirmar la transacción
            conexion.commit()
            logger.info("Datos insertados correctamente.")

            # Cerrar cursor y conexión
            cursor.close()
        else:
            logger.error("No se pudo conectar a la base de datos MySQL")
    except Exception as e:
        logger.error(f"Error during data loading: {e}")
