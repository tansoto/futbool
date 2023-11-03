class Jugadores:
    def __init__(self):
        self.__id_jugador = None
        self.__nombre = None
        self.__edad = None
        self.__posicion = None
        self.__numero = None
        self.__id_equipo = None

    def setIdJugador(self, id_jugador):
        self.__id_jugador = id_jugador

    def getIdJugador(self):
        return self.__id_jugador

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setPosicion(self, posicion):
        self.__posicion = posicion

    def setNumero(self, numero):
        self.__numero = numero

    def setEquipo(self, equipo):
        self.__id_equipo = equipo

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getPosicion(self):
        return self.__posicion

    def getNumero(self):
        return self.__numero

    def getEquipo(self):
        return self.__id_equipo
