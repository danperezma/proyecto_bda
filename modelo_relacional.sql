-- CREATE DATABASE proyecto;

USE proyecto;

-- DROP TABLE estudiante;
CREATE TABLE estudiante(
	idEstudiante INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    genero ENUM("MALE", "FEMALE", "OTHER", "I PREFFER NOT SAY"),
    email VARCHAR(50),
    telefono INT,
    FechaNacimiento DATE
);

-- DROP TABLE programa;
CREATE TABLE programa(
	idPrograma INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nivel ENUM("pregrado", "maestria", "doctorado"),
    facultad VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sede VARCHAR(100) NOT NULL
);

-- DROP TABLE programa_estudiante;
CREATE TABLE programa_estudiante(
	idEstudiante INT,
    idPrograma INT,
    fechaInicio DATE,
    fechaFin DATE,
    modalidadGrado ENUM("tesis", "bapi", "pasantia"),
	PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES estudiante(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES programa(idPrograma)
);

-- DROP TABLE trabajo;
CREATE TABLE trabajo(
	idTrabajo INT PRIMARY KEY,
    fechaInicio DATE,
    fechaFin DATE,
    compañia VARCHAR(50),
    pais VARCHAR(50),
    sector VARCHAR(50),
    salario INT
);

-- DROP TABLE tesis;
CREATE TABLE tesis(
	idEstudiante INT,
    idPrograma INT,
	nombreDirector VARCHAR(100),
    nombre VARCHAR(255),
    fechaPublicacion DATE,
    tema VARCHAR(100),
    PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES estudiante(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES programa(idPrograma)
);

-- DROP TABLE pasantia;
CREATE TABLE pasantia(
	idEstudiante INT,
    idPrograma INT,
	nombreSupervisor VARCHAR(100),
    empresa VARCHAR(255),
    duracionContrato INT,
    PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES estudiante(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES programa(idPrograma)
);

-- DROP TABLE bapi;
CREATE TABLE bapi(
	idEstudiante INT,
    idPrograma INT,
    PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES estudiante(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES programa(idPrograma)
);