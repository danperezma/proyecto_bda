-- CREATE DATABASE proyecto;

USE proyecto;
DROP TABLE IF EXISTS bapi;
DROP TABLE IF EXISTS pasantia;
DROP TABLE IF EXISTS tesis;
DROP TABLE IF EXISTS trabajo;
DROP TABLE IF EXISTS programa_estudiante;
DROP TABLE IF EXISTS programa;
DROP TABLE IF EXISTS estudiante;

CREATE TABLE estudiante(
	idEstudiante INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    genero ENUM("MALE", "FEMALE", "OTHER", "I PREFFER NOT SAY"),
    email VARCHAR(50),
    telefono BIGINT,
    FechaNacimiento DATE
);

CREATE TABLE programa(
	idPrograma INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nivel ENUM("pregrado", "maestria", "doctorado"),
    facultad VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    sede VARCHAR(100) NOT NULL
);

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

CREATE TABLE trabajo(
	idTrabajo INT PRIMARY KEY,
	idEstudiante INT,
    fechaInicio DATE,
    fechaFin DATE,
    compania VARCHAR(50),
    pais VARCHAR(50),
    sector VARCHAR(50),
    salario INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiante(idEstudiante)
);

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

CREATE TABLE bapi(
	idEstudiante INT,
    idPrograma INT,
    PRIMARY KEY(idPrograma, idEstudiante),
    FOREIGN KEY (idEstudiante) REFERENCES estudiante(idEstudiante),
    FOREIGN KEY (idPrograma) REFERENCES programa(idPrograma)
);