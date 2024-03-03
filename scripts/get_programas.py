import csv

# Datos de los programas
programas_info = {
    "Administracion de Empresas": {"nivel": "Pregrado", "departamento": "Administración de Empresas", "facultad": "Facultad de Ciencias Económicas"},
    "Antropologia": {"nivel": "Pregrado", "departamento": "Antropología", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Arquitectura": {"nivel": "Pregrado", "departamento": "Arquitectura", "facultad": "Facultad de Arquitectura y Diseño"},
    "Arte": {"nivel": "Pregrado", "departamento": "Arte", "facultad": "Facultad de Artes y Humanidades"},
    "Biologia": {"nivel": "Pregrado", "departamento": "Biología", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Ciencias Ambientales": {"nivel": "Pregrado", "departamento": "Ciencias Ambientales", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Ciencias de la Computacion": {"nivel": "Pregrado", "departamento": "Ciencias de la Computación", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Ciencias Politicas": {"nivel": "Pregrado", "departamento": "Ciencias Políticas", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Comunicacion Social": {"nivel": "Pregrado", "departamento": "Comunicación Social", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Contaduria Publica": {"nivel": "Pregrado", "departamento": "Contaduría Pública", "facultad": "Facultad de Ciencias Económicas"},
    "Derecho": {"nivel": "Pregrado", "departamento": "Derecho", "facultad": "Facultad de Derecho"},
    "Diseno Grafico": {"nivel": "Pregrado", "departamento": "Diseño Gráfico", "facultad": "Facultad de Artes y Humanidades"},
    "Economia": {"nivel": "Pregrado", "departamento": "Economía", "facultad": "Facultad de Ciencias Económicas"},
    "Educacion": {"nivel": "Pregrado", "departamento": "Educación", "facultad": "Facultad de Ciencias de la Educación"},
    "Enfermeria": {"nivel": "Pregrado", "departamento": "Enfermería", "facultad": "Facultad de Ciencias de la Salud"},
    "Fisica": {"nivel": "Pregrado", "departamento": "Física", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Geografia": {"nivel": "Pregrado", "departamento": "Geografía", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Historia": {"nivel": "Pregrado", "departamento": "Historia", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Ingenieria Agricola": {"nivel": "Pregrado", "departamento": "Ingeniería Agrícola", "facultad": "Facultad de Ingeniería Agronómica"},
    "Ingenieria Ambiental": {"nivel": "Pregrado", "departamento": "Ingeniería Ambiental", "facultad": "Facultad de Ingeniería Civil y Ambiental"},
    "Ingenieria Biomedica": {"nivel": "Pregrado", "departamento": "Ingeniería Biomédica", "facultad": "Facultad de Ingeniería Biomédica"},
    "Ingenieria Civil": {"nivel": "Pregrado", "departamento": "Ingeniería Civil", "facultad": "Facultad de Ingeniería Civil y Ambiental"},
    "Ingenieria de Alimentos": {"nivel": "Pregrado", "departamento": "Ingeniería de Alimentos", "facultad": "Facultad de Ingeniería de Alimentos"},
    "Ingenieria de Minas": {"nivel": "Pregrado", "departamento": "Ingeniería de Minas", "facultad": "Facultad de Ingeniería de Minas"},
    "Ingenieria de Sistemas y Computacion": {"nivel": "Pregrado", "departamento": "Ingeniería de Sistemas y Computación", "facultad": "Facultad de Ingeniería y Ciencias Básicas"},
    "Ingenieria Electrica": {"nivel": "Pregrado", "departamento": "Ingeniería Eléctrica", "facultad": "Facultad de Ingeniería Eléctrica y Electrónica"},
    "Ingenieria Industrial": {"nivel": "Pregrado", "departamento": "Ingeniería Industrial", "facultad": "Facultad de Ingeniería Industrial"},
    "Ingenieria Mecanica": {"nivel": "Pregrado", "departamento": "Ingeniería Mecánica", "facultad": "Facultad de Ingeniería Mecánica"},
    "Ingenieria Quimica": {"nivel": "Pregrado", "departamento": "Ingeniería Química", "facultad": "Facultad de Ingeniería Química"},
    "Lenguas Modernas": {"nivel": "Pregrado", "departamento": "Lenguas Modernas", "facultad": "Facultad de Ciencias Humanas y de la Educación"},
    "Matematicas": {"nivel": "Pregrado", "departamento": "Matemáticas", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Medicina": {"nivel": "Pregrado", "departamento": "Medicina", "facultad": "Facultad de Ciencias de la Salud"},
    "Microbiologia": {"nivel": "Pregrado", "departamento": "Microbiología", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Musica": {"nivel": "Pregrado", "departamento": "Música", "facultad": "Facultad de Artes y Humanidades"},
    "Nutricion y Dietetica": {"nivel": "Pregrado", "departamento": "Nutrición y Dietética", "facultad": "Facultad de Ciencias de la Salud"},
    "Odontologia": {"nivel": "Pregrado", "departamento": "Odontología", "facultad": "Facultad de Odontología"},
    "Pedagogia": {"nivel": "Pregrado", "departamento": "Pedagogía", "facultad": "Facultad de Ciencias de la Educación"},
    "Psicologia": {"nivel": "Pregrado", "departamento": "Psicología", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Quimica": {"nivel": "Pregrado", "departamento": "Química", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Sociologia": {"nivel": "Pregrado", "departamento": "Sociología", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Trabajo Social": {"nivel": "Pregrado", "departamento": "Trabajo Social", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Arquitectura Paisajista (Maestria)": {"nivel": "Maestría", "departamento": "Arquitectura", "facultad": "Facultad de Arquitectura y Diseño"},
    "Biologia Molecular y Biotecnologia (Maestria)": {"nivel": "Maestría", "departamento": "Biología", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Ciencias de la Informacion y la Comunicacion (Maestria)": {"nivel": "Maestría", "departamento": "Ciencias de la Información y la Comunicación", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Desarrollo Sostenible (Maestria)": {"nivel": "Maestría", "departamento": "Desarrollo Sostenible", "facultad": "Facultad de Ciencias Económicas"},
    "Economia (Maestria)": {"nivel": "Maestría", "departamento": "Economía", "facultad": "Facultad de Ciencias Económicas"},
    "Educacion (Maestria)": {"nivel": "Maestría", "departamento": "Educación", "facultad": "Facultad de Ciencias de la Educación"},
    "Estudios Latinoamericanos (Maestria)": {"nivel": "Maestría", "departamento": "Estudios Latinoamericanos", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Fisica (Maestria)": {"nivel": "Maestría", "departamento": "Física", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Genetica y Biologia Molecular (Maestria)": {"nivel": "Maestría", "departamento": "Genética y Biología Molecular", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Gestion y Desarrollo Urbanos (Maestria)": {"nivel": "Maestría", "departamento": "Gestión y Desarrollo Urbanos", "facultad": "Facultad de Arquitectura y Diseño"},
    "Historia (Maestria)": {"nivel": "Maestría", "departamento": "Historia", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Ingenieria Biomedica (Maestria)": {"nivel": "Maestría", "departamento": "Ingeniería Biomédica", "facultad": "Facultad de Ingeniería Biomédica"},
    "Ingenieria Civil y Ambiental (Maestria)": {"nivel": "Maestría", "departamento": "Ingeniería Civil y Ambiental", "facultad": "Facultad de Ingeniería Civil y Ambiental"},
    "Ingenieria de Materiales (Maestria)": {"nivel": "Maestría", "departamento": "Ingeniería de Materiales", "facultad": "Facultad de Ingeniería y Ciencias Básicas"},
    "Ingenieria de Sistemas y Computacion (Maestria)": {"nivel": "Maestría", "departamento": "Ingeniería de Sistemas y Computación", "facultad": "Facultad de Ingeniería y Ciencias Básicas"},
    "Linguistica (Maestria)": {"nivel": "Maestría", "departamento": "Lingüística", "facultad": "Facultad de Ciencias Humanas y de la Educación"},
    "Matematicas (Maestria)": {"nivel": "Maestría", "departamento": "Matemáticas", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Musica (Maestria)": {"nivel": "Maestría", "departamento": "Música", "facultad": "Facultad de Artes y Humanidades"},
    "Neurociencias (Maestria)": {"nivel": "Maestría", "departamento": "Neurociencias", "facultad": "Facultad de Ciencias de la Salud"},
    "Odontologia (Maestria)": {"nivel": "Maestría", "departamento": "Odontología", "facultad": "Facultad de Odontología"},
    "Planificacion Urbana y Regional (Maestria)": {"nivel": "Maestría", "departamento": "Planificación Urbana y Regional", "facultad": "Facultad de Arquitectura y Diseño"},
    "Quimica (Maestria)": {"nivel": "Maestría", "departamento": "Química", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Salud Publica (Maestria)": {"nivel": "Maestría", "departamento": "Salud Pública", "facultad": "Facultad de Ciencias de la Salud"},
    "Sociologia (Maestria)": {"nivel": "Maestría", "departamento": "Sociología", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Trabajo Social (Maestria)": {"nivel": "Maestría", "departamento": "Trabajo Social", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Arquitectura (Doctorado)": {"nivel": "Doctorado", "departamento": "Arquitectura", "facultad": "Facultad de Arquitectura y Diseño"},
    "Biologia (Doctorado)": {"nivel": "Doctorado", "departamento": "Biología", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Ciencias de la Informacion y la Comunicacion (Doctorado)": {"nivel": "Doctorado", "departamento": "Ciencias de la Información y la Comunicación", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Derecho (Doctorado)": {"nivel": "Doctorado", "departamento": "Derecho", "facultad": "Facultad de Derecho"},
    "Educacion (Doctorado)": {"nivel": "Doctorado", "departamento": "Educación", "facultad": "Facultad de Ciencias de la Educación"},
    "Estudios Urbanos y Regionales (Doctorado)": {"nivel": "Doctorado", "departamento": "Estudios Urbanos y Regionales", "facultad": "Facultad de Ciencias Sociales y Humanas"},
    "Fisica (Doctorado)": {"nivel": "Doctorado", "departamento": "Física", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Ingenieria Civil (Doctorado)": {"nivel": "Doctorado", "departamento": "Ingeniería Civil", "facultad": "Facultad de Ingeniería Civil y Ambiental"},
    "Linguistica (Doctorado)": {"nivel": "Doctorado", "departamento": "Lingüística", "facultad": "Facultad de Ciencias Humanas y de la Educación"},
    "Matematicas (Doctorado)": {"nivel": "Doctorado", "departamento": "Matemáticas", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Medicina (Doctorado)": {"nivel": "Doctorado", "departamento": "Medicina", "facultad": "Facultad de Ciencias de la Salud"},
    "Neurociencias (Doctorado)": {"nivel": "Doctorado", "departamento": "Neurociencias", "facultad": "Facultad de Ciencias de la Salud"},
    "Quimica (Doctorado)": {"nivel": "Doctorado", "departamento": "Química", "facultad": "Facultad de Ciencias Naturales y Matemáticas"},
    "Sociologia (Doctorado)": {"nivel": "Doctorado", "departamento": "Sociología", "facultad": "Facultad de Ciencias Sociales y Humanas"}
}

# Nombre del archivo CSV
nombre_archivo = "programas.csv"

# Encabezados del archivo CSV
encabezados = ["idPrograma", "nombre", "nivel", "departamento", "facultad", "sede"]

# Abrir archivo CSV en modo escritura
with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=encabezados)

    # Escribir encabezados
    writer.writeheader()

    # Escribir datos de los programas
    for id_programa, (nombre_programa, info) in enumerate(programas_info.items(), start=1):
        programa = {
            "idPrograma": id_programa,
            "nombre": nombre_programa,
            "nivel": info["nivel"],
            "departamento": info["departamento"],
            "facultad": info["facultad"],
            "sede": "Bogota"
        }
        writer.writerow(programa)

print(f"Se ha generado el archivo CSV '{nombre_archivo}' con la información de los programas.")