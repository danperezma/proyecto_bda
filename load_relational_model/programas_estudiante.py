import csv
from datetime import datetime
from dbConnection import conexion
from logger import logger


def load_data():
    try:
        logger.info("Starting programa_estudiante data loading process")

        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            # Crear cursor
            cursor = conexion.cursor()

            # Nombre del archivo CSV
            archivo_csv = "../data/data_nuevo.csv"

            # Consulta para insertar datos en la tabla
            consulta = "INSERT INTO programa_estudiante (idEstudiante, idPrograma, fechaInicio, fechaFin, modalidadGrado) VALUES (%s, %s, %s, %s, %s)"

            # Leer datos del archivo CSV e insertarlos en la base de datos
            with open(archivo_csv, newline="", encoding="utf-8") as csvfile:
                lector_csv = csv.DictReader(csvfile)
                for fila in lector_csv:
                    # Suponiendo que tus columnas en la tabla se llaman igual que las columnas en el CSV
                    datos = (fila['idEstudiante'], fila['idPrograma'], datetime.strptime(fila['fechaInicio'], "%m/%d/%Y").strftime("%Y-%m-%d"), datetime.strptime(
                        fila['fechaFin'], "%m/%d/%Y").strftime("%Y-%m-%d"), fila['Modalidad Grado'])  # Ajusta esto según la estructura de tu tabla
                    cursor.execute(consulta, datos)

            # Confirmar la transacción
            conexion.commit()
            logger.info("Datos insertados correctamente.")

            # Cerrar cursor y conexión
            cursor.close()
        else:
            logger.error("No se pudo conectar a la base de datos MySQL")
    except Exception as e:
        logger.error(f"Error during program data loading: {e}")
