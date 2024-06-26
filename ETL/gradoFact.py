from datetime import datetime
from logger import log
from dbUtils import conexion, insertIfNotExists, insertData


def months_difference(start_date, end_date):
    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


def process_data_and_save():
    try:
        log("info", "Processing GRADO_FACT")
        cursor = conexion.cursor()

        select_query = "SELECT idEstudiante, idPrograma, fechaInicio, fechaFin, modalidadGrado FROM programa_estudiante"

        cursor.execute(select_query)

        rows = cursor.fetchall()

        for row in rows:

            idEstudiante, idPrograma, fechaInicio, fechaFin, modalidad = row

            # Insert student in ESTUDIANTE_DIM
            cursor.execute(
                f"SELECT idEstudiante, nombre, genero, email, telefono, FechaNacimiento FROM estudiante WHERE idEstudiante = {idEstudiante}")

            estudiante_data = cursor.fetchone()

            today_date = datetime.now().year

            estudiante = {
                "idEstudiante": estudiante_data[0],
                "nombre": estudiante_data[1],
                "sexo": estudiante_data[2],
                "correo": estudiante_data[3],
                "telefono": estudiante_data[4],
                "fechaNacimiento": estudiante_data[5],
                "edad": today_date - estudiante_data[5].year
            }

            insertIfNotExists(conexion, "ESTUDIANTE_DIM",
                              "idEstudiante", estudiante["idEstudiante"], estudiante)

            # Insert program in PROGRAMA_DIM
            cursor.execute(
                f"SELECT * FROM programa WHERE idPrograma = {idPrograma}")

            programa_data = cursor.fetchone()

            programa = {
                "idPrograma": programa_data[0],
                "nombrePrograma": programa_data[1],
                "nivelPrograma": programa_data[2],
                "facultadPrograma": programa_data[3],
                "departamentoPrograma": programa_data[4],
                "sedePrograma": programa_data[5]
            }

            insertIfNotExists(conexion, "PROGRAMA_DIM",
                              "idPrograma", programa["idPrograma"], programa)

            # Create time obj to insert in TIEMPO_DIM

            tiempo = {
                "fechaInicio": fechaInicio,
                "fechaFin": fechaFin,
                "duracionDias": (fechaFin - fechaInicio).days,
                "duracionMeses": abs(months_difference(fechaFin, fechaInicio)),
                "duracionAnios": fechaFin.year - fechaInicio.year
            }

            tiempo_id = insertData(conexion, "TIEMPO_DIM", tiempo)

            log("debug", "try to create map fact")

            # Insert fact data
            fact = {
                "idEstudiante": idEstudiante,
                "idPrograma": programa.get("idPrograma", -1),
                "idTiempo": tiempo_id,
                "modalidadGrado": modalidad,
            }

            log("debug", f"Map created: {fact}")

            insertData(conexion, "GRADO_FACT", fact)

        conexion.commit()
        log("info", "Data processing finished")
    except Exception as error:
        log("error", f"Error during data processing: {error}")
    finally:
        log("info", "Data processing finished")
        cursor.close()


process_data_and_save()
