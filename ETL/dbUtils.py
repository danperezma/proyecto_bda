import os
import mysql.connector
from dotenv import load_dotenv
from logger import log

load_dotenv()


def createConexion():
    try:
        db_host = os.getenv("DB_HOST")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_database = os.getenv("DB_DATABASE")

        conexion = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        log("info", "Connected to the database", None)
        return conexion

    except mysql.connector.Error as err:
        # Log connection error
        log("error", f"Failed to connect to the database {err}")
        return None


def processObj():
    pass


def insertData(con, table, data_dict):
    if data_dict is None or len(data_dict) == 0:
        return

    cursor = con.cursor()

    try:
        # Prepare column names and values for insertion
        columns = ', '.join(data_dict.keys())
        values = ', '.join(['%s'] * len(data_dict))

        # Insert data into the table using parameterized query
        insert_query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(insert_query, list(data_dict.values()))

        con.commit()  # Commit the transaction

        log("info", f"Data inserted into {table} successfully")

        return cursor.lastrowid
    except mysql.connector.Error as error:
        log("error", f"Error inserting data into {table}. Error was {error}")
        con.rollback()  # Rollback changes if an error occurs
    finally:
        cursor.close()


def insertIfNotExists(con, table, id_column, id_value, data_dict):
    if data_dict is None or len(data_dict) == 0:
        return

    log("info", f"Inserting data into {table}. {id_column}: {id_value}")

    cursor = con.cursor()

    try:
        # Check if the row with the given id exists
        cursor.execute(
            f"SELECT * FROM {table} WHERE {id_column} = %s", (id_value,))
        if cursor.fetchone() is None:
            # Prepare column names and values for insertion
            data_dict.pop(id_column)
            columns = ', '.join(data_dict.keys())
            values = ', '.join(['%s'] * len(data_dict))

            # Insert data into the table using parameterized query
            insert_query = f"INSERT INTO {
                table} ({id_column}, {columns}) VALUES (%s, {values})"
            cursor.execute(insert_query, (id_value, *data_dict.values()))

            con.commit()  # Commit the transaction

    except mysql.connector.Error as error:
        log("error", f"Error inserting data into {table}. Error was {error}")
        con.rollback()  # Rollback changes if an error occurs
    finally:
        log("info",
            f"Data inserted into {table} successfully. {id_column}: {id_value}")
        cursor.close()


conexion = createConexion()
