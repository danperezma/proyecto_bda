-- This is a mysql script to create the star model for the graduated students

USE proyecto;

-- Drop tables if they exist to avoid errors
DROP TABLE IF EXISTS ESTUDIANTE_DIM;
DROP TABLE IF EXISTS PROGRAMA_DIM;
DROP TABLE IF EXISTS TIEMPO_DIM;
DROP TABLE IF EXISTS GRADO_FACT;
DROP TABLE IF EXISTS TRABAJO_FACT;
DROP TABLE IF EXISTS TESIS_FACT;


CREATE TABLE TIEMPO_DIM(
  idTiempo INT AUTO_INCREMENT PRIMARY KEY,
  fechaInicio DATE,
  fechaFin DATE,
  duracionDias INT,
  duracionMeses INT,
  duracionAnios INT
);

CREATE TABLE ESTUDIANTE_DIM(
  idEstudiante INT PRIMARY KEY,
  nombre VARCHAR(50),
  sexo VARCHAR(50),
  correo VARCHAR(50),
  telefono VARCHAR(20),
  fechaNacimiento DATE,
  edad INT
);

CREATE TABLE PROGRAMA_DIM(
  idPrograma INT PRIMARY KEY,
  nombrePrograma VARCHAR(50),
  nivelPrograma ENUM("pregrado", "maestria", "doctorado"),
  facultadPrograma VARCHAR(50),
  departamentoPrograma VARCHAR(50),
  sedePrograma VARCHAR(50)
);

CREATE TABLE GRADO_FACT(
  idEstudiante INT,
    idPrograma INT,
    modalidadGrado ENUM("tesis", "bapi", "pasantia"),
    idTiempo INT,
    PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES ESTUDIANTE_DIM(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES PROGRAMA_DIM(idPrograma),
    FOREIGN KEY (idTiempo) REFERENCES TIEMPO_DIM(idTiempo)
);


CREATE TABLE TRABAJO_FACT(
  idTrabajo INT PRIMARY KEY,
  idEstudiante INT,
  idPrograma INT,
  idTiempo INT,
    fechaInicio DATE,
    fechaFin DATE,
    compania VARCHAR(50),
    pais VARCHAR(50),
    sector VARCHAR(50),
    salario INT,
    FOREIGN KEY (idEstudiante) REFERENCES ESTUDIANTE_DIM(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES PROGRAMA_DIM(idPrograma),
    FOREIGN KEY (idTiempo) REFERENCES TIEMPO_DIM(idTiempo)

);

CREATE TABLE TESIS_FACT(
  idEstudiante INT,
    idPrograma INT,
    nombreDirector VARCHAR(100),
    nombre VARCHAR(255),
    fechaPublicacion DATE,
    tema VARCHAR(100),
    PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES ESTUDIANTE_DIM(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES PROGRAMA_DIM(idPrograma)
);