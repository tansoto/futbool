from controllers.jugador_controller import Jugador_Controller
from models.equipos import Equipos
from views import equipo_menu as eq_menu
import controllers


class Equipo_Controller:
    def existe_equipo(database, id_equipo):
        query = ("select count(id_equipo) from Equipos where id_equipo = '" + id_equipo + "'")
        if database.get(query)[0][0] == 1:
            return True
        elif database.get(query)[0][0] == 0:
            return False
        else:
            print(database.get(query))

    def crear_equipo(database):
        equipo = Equipos()
        id_equipo = input("Por favor ingrese id del equipo: ")
        existe = Equipo_Controller.existe_equipo(database, id_equipo)
        if existe is False:
            nombre = input("Por favor ingrese el nombre del equipo: ")
            equipo.setNombre(nombre)
            ciudad = input("Por favor ingrese la ciudad del equipo: ")
            equipo.setCiudad(ciudad)
            presidente = input("Por favor ingrese el presidente del equipo: ")
            equipo.setPresidente(presidente)
            query = "insert into Ciudad (nombre) values ('" + equipo.getCiudad() + "') RETURNING id_ciudad"
            resultado = database.post(query)  # inserta ciudad y ya que pidio el returning resukltado es el id de la ciudad
            query = ("insert into Equipos (nombre,presidente,id_ciudad) values ('"+ equipo.getNombre()+ "','"+ equipo.getPresidente()+ "','"+ str(resultado)+ "') RETURNING id_equipo")
            database.post(query)  # inserta equipo
            print("Equipo creado exitosamente")
        else:
            print("El id ingresado ya se encuentra en uso")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def editar_equipo(database):
        id_equipo = input("Por favor indique la id del equipo a modificar: ")
        if Equipo_Controller.existe_equipo(database, id_equipo) is False:
            print("El equipo no existe")
        else:
            pos = Equipo_Controller.existe_equipo(database, id_equipo)
            nombre = input(
                "Ingrese el nuevo nombre del equipo (Actual: "
                + database[pos].getNombre()
                + ",Enter para skip): "
            )
            if nombre != "":
                database[pos].setNombre(nombre)
            ciudad = input(
                "Ingrese la nueva ciudad del equipo (Actual: "
                + database[pos].getCiudad()
                + ",Enter para skip): "
            )
            if ciudad != "":
                database[pos].setCiudad(ciudad)
            presidente = input(
                "Ingrese el nuevo presidente (Actual: "
                + database[pos].getPresidente()
                + ",Enter para skip): "
            )
            if presidente != "":
                database[pos].setPresidente(presidente)
            print("Equipo editado exitosamente")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def listar_equipos(database):
        for equipo in database:
            print("********** Equipo: " + equipo.getIdEquipo() + "********** ")
            print(
                "nombre: "
                + equipo.getNombre()
                + "\n"
                + "ciudad: "
                + equipo.getCiudad()
                + "\n"
                + "presidente: "
                + equipo.getPresidente()
                + "\n"
            )
            print("Jugadores en el equipo: " + equipo.getIdEquipo())
            controllers.jugador_controller.Jugador_Controller.listar_jugadores(equipo)
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def eliminar_equipo(database):
        id_equipo = input("Ingrese el ID del equipo a eliminar: ")
        existe = Equipo_Controller.existe_equipo(database, id_equipo)
        if existe is False:
            print("El id indicado no existe")
        else:
            #print("El siguiente equipo sera eliminado: " + database[existe].getNombre())
            respuesta = str(input("¿Desea continuar? S/N: "))
            if respuesta.upper() == "S":
                #database.remove(database[existe])
                query = ("delete from Equipos where id_equipo = '" + id_equipo + "'") #borra el equipo con el id indicado 
                database.delete(query)
                print("Equipo eliminado")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def ver_equipo(database):
        id_equipo = input("Ingrese el ID del equipo a consultar: ")
        if Equipo_Controller.existe_equipo(database, id_equipo) is False:
            print("El equipo consultado no existe")
        else:
            equipo = database[Equipo_Controller.existe_equipo(database, id_equipo)]
            print(
                "Nombre: "
                + equipo.getNombre()
                + "\n"
                + "Ciudad: "
                + equipo.getCiudad()
                + "\n"
                + "Presidente: "
                + equipo.getPresidente()
                + "\n"
            )
            controllers.jugador_controller.Jugador_Controller.listar_jugadores(equipo)
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def buscar_jugador_en_equipo(database):
        id_jugador = input("Ingrese el ID del jugador a consultar: ")
        existe_jugador = Jugador_Controller.encontrar_jugador(database, id_jugador)
        pos_equipo = Equipo_Controller.existe_equipo(
            database, input("Ingrese el ID del equipo a consultar: ")
        )
        equipo = database[pos_equipo]
        if pos_equipo is False:
            print("NO hay equipo")

        else:
            if existe_jugador is False:
                print("NO hay jugador")

            else:
                for jugador in equipo.getNomina():
                    if jugador.getIdJugador() == id_jugador:
                        print(
                            "El jugador: "
                            + jugador.getNombre()
                            + " pertenece al equipo: "
                            + equipo.getNombre()
                        )
                        return eq_menu.Equipo_Menu.menu_equipos(database)

            print(" no pertenece al equipo: ")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def eliminar_jugador(database):
        id_jugador = input("Por favor ingrese id del jugador a eliminar: ")
        encontrar = Jugador_Controller.encontrar_jugador(database, id_jugador)
        if encontrar is False:
            print("Jugador no encontrado")
        else:
            pos_jugador = encontrar[0]
            jugador = encontrar[1]
            pos_equipo = controllers.equipo_controller.Equipo_Controller.existe_equipo(
                database, jugador.getEquipo()
            )
            equipo = jugador.getEquipo()
            pos = controllers.equipo_controller.Equipo_Controller.existe_equipo(
                database, equipo
            )
            if pos is not False:
                print("\n\n Se mete a borrar")
                database[pos_equipo].getNomina().pop(pos_jugador)
                controllers.equipo_controller.Equipo_Controller.listar_equipos(database)
            print("Jugador eliminado correctamente")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def ver_jugador(database):
        id_jugador = input("Ingrese el ID del jugador a consultar: ")
        existe_jugador = Jugador_Controller.encontrar_jugador(database, id_jugador)
        pos_equipo = Equipo_Controller.existe_equipo(
            database, input("Ingrese el ID del equipo a consultar: ")
        )
        equipo = database[pos_equipo]
        if pos_equipo is False:
            print("NO hay equipo")

        else:
            if existe_jugador is False:
                print("NO hay jugador")

            else:
                for jugador in equipo.getNomina():
                    if jugador.getIdJugador() == id_jugador:
                        print("\n")
                        print("\n")
                        print("\n")
                        print("Nombre del jugador: " + jugador.getNombre())

                        print("Edad del jugador: " + jugador.getEdad())

                        print("Posicion del jugador: " + jugador.getPosicion())

                        print("Numero del jugador: " + jugador.getNumero())

                        print("Id de equipo del jugador: " + jugador.getEquipo())
                        print("\n")
                        print("\n")
                        print("\n")
                        return eq_menu.Equipo_Menu.menu_equipos(database)

            print("No pertenece al equipo: ")
        return eq_menu.Equipo_Menu.menu_equipos(database)
