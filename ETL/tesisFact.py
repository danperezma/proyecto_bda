from datetime import datetime
from logger import logger
from dbUtils import conexion, insertIfNotExists, insertData


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


def process_data_and_save():
    try:
        logger.info("Processing TESIS_FACT")

        cursor = conexion.cursor()

        select_query = "SELECT * FROM tesis"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        for row in rows:
            idEstudiante, idPrograma, nombreDirector, nombre, fechaPublicacion, tema = row

            estudiante = createStudentData(idEstudiante, cursor)
            insertIfNotExists(conexion, "ESTUDIANTE_DIM",
                              "idEstudiante", estudiante["idEstudiante"], estudiante)

            programa = createProgramData(idPrograma, cursor)
            insertIfNotExists(conexion, "PROGRAMA_DIM",
                              "idPrograma", programa["idPrograma"], programa)

            tesis = {
                "idEstudiante": idEstudiante,
                "idPrograma": idPrograma,idEstudiante
                "nombreDirector": nombreDirector,
                "nombre": nombre,
                "fechaPublicacion": fechaPublicacion,
                "tema": tema
            }

            insertData(conexion, "TESIS_FACT", tesis)

        conexion.commit()
        logger.info("Data processed and saved successfully")
    except Exception as e:
        logger.error(f"Error in processing TESIS_FACT: {e}")


process_data_and_save()
