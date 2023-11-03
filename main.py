from views.main_menu import Main_Menu
from db.base_de_datos import BaseDeDatos

database = BaseDeDatos()

Main_Menu.menu_principal(database)
