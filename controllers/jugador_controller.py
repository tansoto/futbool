from views import jugador_menu as jug_menu
from models.jugadores import Jugadores
from models.equipos import Equipos
import controllers


class Jugador_Controller:
    def listar_jugadores(equipo):
        nomina = equipo.getNomina()
        for jugadores in nomina:
            print("----------Jugador: " + jugadores.getIdJugador() + "----------")
            print(
                "Nombre jugador:"
                + jugadores.getNombre()
                + "\n"
                + "Edad jugador: "
                + jugadores.getEdad()
                + "\n"
                + "Posicion jugador: "
                + jugadores.getPosicion()
                + "\n"
                + "Numero jugador: "
                + jugadores.getNumero()
                + "\n"
            )

    def crear_jugador(database):
        jugador = Jugadores()
        id_equipo = input(
            "Por favor ingrese el id del equipo al que pertenecera el jugador: ")
        existe = controllers.equipo_controller.Equipo_Controller.existe_equipo(database, id_equipo)
        if existe is False:
            print("El equipo indicado no existe volviendo al menu...")
        else:
            id_jugador = input("Por favor ingrese id del jugador: ")
            existe_jugador = Jugador_Controller.encontrar_jugador(database, id_jugador)
            if existe_jugador is False:
                jugador.setNombre(input("Por favor ingrese el nombre del jugador: "))
                jugador.setEdad(input("Por favor ingrese la edad del jugador: "))
                jugador.setPosicion(input("Por favor ingrese la posición del jugador: "))
                jugador.setNumero(input("Por favor ingrese el número del jugador: "))
                jugador.setEquipo(id_equipo)
                query= "insert into posicion (nombre) values ('" + jugador.getPosicion() + "') RETURNING id_posicion"#se crea la query para insertar la posicion
                posicion=database.post(query)#se ejecuta la query y se guarda el id de la posicion
                # se agrega el jugador a la nomina del equipo con la posicion en existe
                query = "insert into jugadores (nombre,edad,numero,id_equipo,id_posicion)values('" + jugador.getNombre() + "','" + jugador.getEdad() + "','"+jugador.getNumero() +"','"+ str(id_equipo)+ "','" + str(posicion) + "')"#se crea la query para insertar el jugador
                database.post(query)#se ejecuta la query
            else:
                print("El id ingresado ya se encuentra en uso volviendo al menu...")

        return jug_menu.Jugador_Menu.menu_jugadores(database)

    def encontrar_jugador(database, id_jugador):
        query = ("select count(id_jugador) from Jugadores where id_jugador = '" + id_jugador + "'")
        if database.get(query)[0][0] == 1:#cuenta cuantas veces encuentra ese id en la base de datos
            return True
        elif database.get(query)[0][0] == 0:
            return False
        else:
            print(database.get(query))

    def editar_jugador(database):
        id_jugador = input("Por favor ingrese id del jugador a editar: ")
        encontrar = Jugador_Controller.encontrar_jugador(database, id_jugador)
        if encontrar is False:
            print("Jugador no encontrado")
        else:
            pos_jugador = encontrar[0]
            jugador = encontrar[1]
            pos_equipo = controllers.equipo_controller.Equipo_Controller.existe_equipo(
                database, jugador.getEquipo()
            )
            nombre = input(
                "Ingrese el nuevo nombre del jugador (Actual: "
                + jugador.getNombre()
                + ",Enter para skip): "
            )
            if nombre != "":
                jugador.setNombre(nombre)
            edad = input(
                "Ingrese la nueva edad del jugador (Actual: "
                + jugador.getEdad()
                + ",Enter para skip): "
            )
            if edad != "":
                jugador.setEdad(edad)
            posicion = input(
                "Ingrese la nueva posicion del jugador (Actual: "
                + jugador.getPosicion()
                + ",Enter para skip): "
            )
            if posicion != "":
                jugador.setPosicion(posicion)
            numero = input(
                "Ingrese el nuevo numero del jugador (Actual: "
                + jugador.getNumero()
                + ",Enter para skip): "
            )
            if numero != "":
                jugador.setNumero(numero)
            equipo = input(
                "Ingrese el nuevo id de equipo del jugador (Actual: "
                + jugador.getEquipo()
                + ",Enter para skip): "
            )
            if equipo != "":
                pos = controllers.equipo_controller.Equipo_Controller.existe_equipo(
                    database, equipo
                )
                if pos is not False:
                    jugador.setEquipo(equipo)
                    database[pos].agregarJugador(jugador)  # revisarrr
                    print(
                        "\n\nlargoooooooooo lista equipos "
                        + str((database[pos_equipo].getNomina().index(jugador)))
                    )
                    print(
                        "\n\njugador a borrar lista equipos "
                        + str((database[pos_equipo].getNomina()[pos_jugador]))
                    )
                    database[pos_equipo].getNomina().pop(pos_jugador)
                    controllers.equipo_controller.Equipo_Controller.listar_equipos(
                        database
                    )
            # database[pos_equipo].getNomina().append(jugador)#revisar# error encontrado era donde se borraba quedaba en 0 la lista ademas se agregaba 2 veces
            print("Jugador editado correctamente")
        jug_menu.Jugador_Menu.menu_jugadores(database)
