from datetime import datetime
from logger import log
from dbUtils import conexion, insertIfNotExists, insertData


def months_difference(start_date, end_date):
    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


def createProgramData(idPrograma, cursor):
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

    return programa


def createStudentData(idEstudiante, cursor):
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
    return estudiante


def createTimeData(fechaInicio, fechaFin):
    tiempo = {
        "fechaInicio": fechaInicio,
        "fechaFin": fechaFin,
        "duracionDias": (fechaFin - fechaInicio).days,
        "duracionMeses": months_difference(fechaFin - fechaInicio),
        "duracionAnios": (fechaFin - fechaInicio).year
    }
    return tiempo


def process_data_and_save():
    try:
        log("info", "Processing TRABAJO_FACT")
        cursor = conexion.cursor()

        select_query = "SELECT * FROM trabajo"
        cursor.execute(select_query)

        rows = cursor.fetchall()

        for row in rows:

            idTrabajo, idEstudiante, fechaInicio, fechaFin, compania, pais, sector, salario = row

            studentProgramQuery = f"SELECT idPrograma FROM programa_estudiante WHERE idEstudiante = {
                idEstudiante}"
            cursor.execute(studentProgramQuery)

            programIds = []

            for program in cursor.fetchall():
                idPrograma = program[0]
                programIds.append(idPrograma)

                programa = createProgramData(idPrograma, cursor)
                insertIfNotExists(conexion, "PROGRAMA_DIM",
                                  "idPrograma", programa["idPrograma"], programa)

            # Insert student in ESTUDIANTE_DIM
            estudiante = createStudentData(idEstudiante, cursor)
            insertIfNotExists(conexion, "ESTUDIANTE_DIM",
                              "idEstudiante", estudiante["idEstudiante"], estudiante)

            tiempo = createTimeData(fechaInicio, fechaFin)
            tiempoId = insertData(conexion, "TIEMPO_DIM", tiempo)

            for idPrograma in programIds:
                trabajo = {
                    "idTrabajo": idTrabajo,
                    "idEstudiante": idEstudiante,
                    "idPrograma": idPrograma,
                    "idTiempo": tiempoId,
                    "fechaInicio": fechaInicio,
                    "fechaFin": fechaFin,
                    "compania": compania,
                    "pais": pais,
                    "sector": sector,
                    "salario": salario
                }
                insertData(conexion, "TRABAJO_FACT", trabajo)

        log("info", "Data processed and saved successfully")
    except Exception as e:
        log("error", f"Error in processing TRABAJO_FACT: {e}")


process_data_and_save()
