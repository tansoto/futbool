class Equipos:

    def __init__(self):
        self.__id_equipo = None
        self.__nombre = None
        self.__ciudad = None
        self.__presidente = None
        self.__nomina = []

    def setIdEquipo(self, id_equipo):
        self.__id_equipo = id_equipo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCiudad(self, ciudad):
        self.__ciudad = ciudad

    def setPresidente(self, presidente):
        self.__presidente = presidente

    def agregarJugador(self, jugador):
        self.__nomina.append(jugador)

    def eliminarJugador(self, jugador):
        self.__nomina.remove(jugador)

    # def existeJugador(self, jugador):
    #     for elemento in self.__nomina:
    #         if elemento.getIdJugador == jugador.getIdJugador():
    #             return self.__nomina.index(elemento)
    #     return False

    def getIdEquipo(self):
        return self.__id_equipo

    def getNombre(self):
        return self.__nombre

    def getCiudad(self):
        return self.__ciudad

    def getPresidente(self):
        return self.__presidente

    def getNomina(self):
        return self.__nomina
