import mysql.connector
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)


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

        logging.info("Connected to the database")
        return conexion

    except mysql.connector.Error as err:
        # Log connection error
        logging.error(f"Failed to connect to the database: {err}")
        return None
