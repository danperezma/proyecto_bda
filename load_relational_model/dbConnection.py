import os
import mysql.connector
from dotenv import load_dotenv
from logger import logger

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

        logger.info("Connected to the database")
        return conexion

    except mysql.connector.Error as err:
        # Log connection error
        logger.error(f"Failed to connect to the database: {err}")
        return None


conexion = createConexion()
