import bapi
import estudiantes
import programas
import programas_estudiante
import pasantia
import tesis
import trabajo
from dbConnection import conexion

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
    def delete_all_data():
        try:
            cursor = conexion.cursor()

            # List of tables from which you want to delete data
            tables = ["bapi", "estudiante", "pasantia", "programa",
                      "programa_estudiante", "tesis", "trabajo"]

            for table in tables:
                delete_query = f"DELETE FROM {table}"
                cursor.execute(delete_query)
                print(f"All data deleted from table {table}")

            conexion.commit()
            print("All data deleted successfully.")
        except Exception as e:
            print(f"Error during data deletion: {e}")
        finally:
            cursor.close()

    delete_all_data()
