from controllers.jugador_controller import Jugador_Controller
from views import main_menu


class Jugador_Menu:
    def menu_jugadores(database):
        print("Bienvenido al mantenedor de jugadores")
        print("1.- Crear jugador")
        print("2.- Editar jugador")
        print("3.- Volver al menú principal")
        opcion = input("Por favor ingrese una opción: ")
        match opcion:
            case "1":
                Jugador_Controller.crear_jugador(database)
            case "2":
                Jugador_Controller.editar_jugador(database)
            case "3":
                return main_menu.Main_Menu.menu_principal(database)
            case _:
                print("Opción no válida")
                return Jugador_Menu.menu_jugadores(database)
