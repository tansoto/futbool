from controllers.equipo_controller import Equipo_Controller
from views import main_menu


class Equipo_Menu:
    def menu_equipos(database):
        # os.system("cls")
        print("Bienvenido al mantenedor de equipos")
        print("1.- Crear equipo")
        print("2.- Editar equipo")
        print("3.- Eliminar equipo")
        print("4.- Ver equipo")
        print("5.- Listar equipos")
        print("6.- Buscar jugador en equipo")
        print("7.- eliminar jugador de equipo")
        print("8.- Ver jugador")
        print("9.- Volver al menú principal")

        opcion = input("Por favor ingrese una opción: ")
        match opcion:
            case "1":
                Equipo_Controller.crear_equipo(database)
            case "2":
                Equipo_Controller.editar_equipo(database)
            case "3":
                Equipo_Controller.eliminar_equipo(database)
            case "4":
                Equipo_Controller.ver_equipo(database)
            case "5":
                Equipo_Controller.listar_equipos(database)
            case "6":
                return Equipo_Controller.buscar_jugador_en_equipo(database)
            case "7":
                return Equipo_Controller.eliminar_jugador(database)
            case "8":
                return Equipo_Controller.ver_jugador(database)
            case "9":
                return main_menu.Main_Menu.menu_principal(database)
            case _:
                print("Opción no válida")
                return Equipo_Menu.menu_equipos(database)
