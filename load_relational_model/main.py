import bapi
import estudiantes
import programas
import programas_estudiante
import pasantia
import tesis
import trabajo
import dotenv
from logger import log
from dbConnection import conexion

dotenv.load_dotenv()

clear = False

if not clear:
    programas.load_data()
    estudiantes.load_data()
    programas_estudiante.load_data()
    pasantia.load_data()
    tesis.load_data()
    trabajo.load_data()
    bapi.load_data()

else:
    log("warning", "Clearing all data from all tables", None)
    try:
        cursor = conexion.cursor()

        # List of tables from which you want to delete data
        tables = ["trabajo", "bapi", "programa_estudiante",
                  "pasantia", "tesis", "estudiante", "programa"]

        for table in tables:
            delete_query = f"DELETE FROM {table}"
            cursor.execute(delete_query)
            log("info", f"All data deleted from table {table}", None)

        conexion.commit()
        log("info", "All data deleted from all tables", None)

    except Exception as e:
        log("error", f"Failed to delete all data {e}", str(e))
    finally:
        cursor.close()
