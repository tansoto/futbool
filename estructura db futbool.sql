CREATE TABLE Ciudad (
    id_ciudad SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE Equipos (
    id_equipo SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    presidente VARCHAR(255),
    id_ciudad INT,
    FOREIGN KEY (id_ciudad) REFERENCES Ciudad(id_ciudad)
);

CREATE TABLE Posicion (
    id_posicion SERIAL PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE Jugadores (
    id_jugador SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT,
    numero INT,
    id_equipo INT,
    id_posicion INT,
    FOREIGN KEY (id_equipo) REFERENCES Equipos(id_equipo),
    FOREIGN KEY (id_posicion) REFERENCES Posicion(id_posicion)
);
