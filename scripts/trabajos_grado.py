import csv

# Diccionario de programas con su respectivo ID
programas = [
    "Administracion de Empresas",
    "Antropologia",
    "Arquitectura",
    "Arte",
    "Biologia",
    "Ciencias Ambientales",
    "Ciencias de la Computacion",
    "Ciencias Politicas",
    "Comunicacion Social",
    "Contaduria Publica",
    "Derecho",
    "Diseno Grafico",
    "Economia",
    "Educacion",
    "Enfermeria",
    "Fisica",
    "Geografia",
    "Historia",
    "Ingenieria Agricola",
    "Ingenieria Ambiental",
    "Ingenieria Biomedica",
    "Ingenieria Civil",
    "Ingenieria de Alimentos",
    "Ingenieria de Minas",
    "Ingenieria de Sistemas y Computacion",
    "Ingenieria Electrica",
    "Ingenieria Industrial",
    "Ingenieria Mecanica",
    "Ingenieria Quimica",
    "Lenguas Modernas",
    "Matematicas",
    "Medicina",
    "Microbiologia",
    "Musica",
    "Nutricion y Dietetica",
    "Odontologia",
    "Pedagogia",
    "Psicologia",
    "Quimica",
    "Sociologia",
    "Trabajo Social",
    "Arquitectura Paisajista (Maestria)",
    "Biologia Molecular y Biotecnologia (Maestria)",
    "Ciencias de la Informacion y la Comunicacion (Maestria)",
    "Desarrollo Sostenible (Maestria)",
    "Economia (Maestria)",
    "Educacion (Maestria)",
    "Estudios Latinoamericanos (Maestria)",
    "Fisica (Maestria)",
    "Genetica y Biologia Molecular (Maestria)",
    "Gestion y Desarrollo Urbanos (Maestria)",
    "Historia (Maestria)",
    "Ingenieria Biomedica (Maestria)",
    "Ingenieria Civil y Ambiental (Maestria)",
    "Ingenieria de Materiales (Maestria)",
    "Ingenieria de Sistemas y Computacion (Maestria)",
    "Linguistica (Maestria)",
    "Matematicas (Maestria)",
    "Musica (Maestria)",
    "Neurociencias (Maestria)",
    "Odontologia (Maestria)",
    "Planificacion Urbana y Regional (Maestria)",
    "Quimica (Maestria)",
    "Salud Publica (Maestria)",
    "Sociologia (Maestria)",
    "Trabajo Social (Maestria)",
    "Arquitectura (Doctorado)",
    "Biologia (Doctorado)",
    "Ciencias de la Informacion y la Comunicacion (Doctorado)",
    "Derecho (Doctorado)",
    "Educacion (Doctorado)",
    "Estudios Urbanos y Regionales (Doctorado)",
    "Fisica (Doctorado)",
    "Ingenieria Civil (Doctorado)",
    "Linguistica (Doctorado)",
    "Matematicas (Doctorado)",
    "Medicina (Doctorado)",
    "Neurociencias (Doctorado)",
    "Quimica (Doctorado)",
    "Sociologia (Doctorado)"
]

# Funcion para leer datos de un archivo CSV y devolver un diccionario donde las claves son los IDs de estudiante
def leer_datos_csv(nombre_archivo):
    datos = {}
    with open(nombre_archivo, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Si el archivo es de datos.csv, usar la columna 'Programa'
            if 'Programa' in row:
                datos[row['idEstudiante']] = row
            # Si el archivo es de pasantias.csv o tesis.csv, usar la columna 'idPrograma'
            elif 'idPrograma' in row:
                datos[row['idEstudiante']] = {'idPrograma': row['idPrograma']}
    return datos

# Funcion para escribir datos en un archivo CSV
def escribir_csv(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', newline='') as csvfile:
        fieldnames = datos[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in datos:
            writer.writerow(row)

# Funcion para asignar ID de programa basado en el diccionario de programas
def asignar_id_programa(programa):
    return programas.index(programa) + 1  # Retorna 'P00' si el programa no esta en el diccionario

# Leer datos de los archivos CSV
datos = leer_datos_csv('..\\data_nuevo.csv')
# pasantia = leer_datos_csv('pasantias.csv')
# tesis = leer_datos_csv('tesis.csv')

# Filtrar datos basados en IDs de estudiante y modalidad de grado
bapi = []
tesis_nuevos = []
pasantia_nuevos = []
for id_estudiante, estudiante in datos.items():
    if estudiante['Modalidad Grado'] == 'bapi':
        bapi.append({'idEstudiante': id_estudiante, 'idPrograma': asignar_id_programa(estudiante['Programa'])})
    # elif estudiante['Modalidad Grado'] == 'tesis':
    #     tesis_nuevos.append({'idEstudiante': id_estudiante, 'idPrograma': asignar_id_programa(estudiante["Programa"])})
    # else:
    #     pasantia_nuevos.append({'idEstudiante': id_estudiante, 'idPrograma': asignar_id_programa(estudiante["Programa"])})
    # data_nuevo.append({'idEstudiante': id_estudiante, 'idPrograma': asignar_id_programa(estudiante["Programa"]), 'Programa':estudiante['Programa']})

# Escribir datos filtrados en los archivos CSV de salida
escribir_csv('bapi.csv', bapi)
# escribir_csv('data_nuevo.csv', data_nuevo)
# escribir_csv('tesis_nuevos.csv', tesis_nuevos)
# escribir_csv('pasantia_nuevos.csv', pasantia_nuevos)
