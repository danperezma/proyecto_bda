import logging
import bapi
import estudiantes
import programas
import programas_estudiante
import pasantia
import tesis
import trabajo

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler and set its level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the console handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

programas.load_data()
estudiantes.load_data()
programas_estudiante.load_data()
pasantia.load_data()
tesis.load_data()
trabajo.load_data()
bapi.load_data()
