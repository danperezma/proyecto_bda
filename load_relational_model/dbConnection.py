import os
import mysql.connector
import dotenv
from logger import logger
from logger import log


dotenv.load_dotenv()


def createConexion():
    try:
        db_host = os.getenv("DB_HOST")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_database = os.getenv("DB_DATABASE")

        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        log("info", "Connected to the database", connection)
        return connection

    except mysql.connector.Error as err:
        # Log connection error
        log("error", "Failed to connect to the database", str(err))
        return None


conexion = createConexion()
