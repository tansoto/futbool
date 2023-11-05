from .jugador_menu import Jugador_Menu
from .equipo_menu import Equipo_Menu



class Main_Menu:

    def menu_principal(database):
        print("Bienvenido al sistema de plantilla equipos/jugadores futbol")
        print("1.- Menú Equipos")
        print("2.- Menú Jugadores")
        print("3.- Salir")
        opcion = input("Por favor ingrese una opción: ")
        match opcion:
            case "1":
                Equipo_Menu.menu_equipos(database)
            case "2":
                Jugador_Menu.menu_jugadores(database)
            case "3":
                exit()
            case _:
                print("Opción erronea") 
                Main_Menu.menu_principal(database)
                
