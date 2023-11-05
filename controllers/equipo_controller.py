from controllers.jugador_controller import Jugador_Controller
from models.equipos import Equipos
from views import equipo_menu as eq_menu
import controllers


class Equipo_Controller:
    def existe_equipo(database, id_equipo):
        query = ("select count(id_equipo) from equipos where id_equipo = '" + id_equipo + "'")
        if database.get(query)[0][0] == 1:#obtiene el valor de la query y lo compara con 1, si es 1 retorna True, si es 0 retorna False
            return True
        elif database.get(query)[0][0] == 0:
            return False
        else:
            print(database.get(query))

    def crear_equipo(database):
        equipo = Equipos()


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

        return eq_menu.Equipo_Menu.menu_equipos(database)

    def editar_equipo(database):
        id_equipo = input("Por favor indique la id del equipo a modificar: ")
        if Equipo_Controller.existe_equipo(database, id_equipo) is False:
            print("El equipo no existe")
        else:
            nombre = input("Ingrese el nuevo Nombre (Actual: " + database.get("select nombre from Equipos where id_equipo = '" + id_equipo + "'")[0][0]+ ",Enter para skip): ")
            if nombre != "":
                query= ("update Equipos set nombre = '" + nombre + "' where id_equipo = '" + id_equipo + "'")
                database.update(query)
            #muestra la ciudad actual del equipo y pregunta si desea cambiarla
            id_ciudad =database.get("select id_ciudad from Equipos where id_equipo = '" + id_equipo + "'")[0][0]
            nombre_ciudad=database.get("select nombre from Ciudad where id_ciudad = '" + str(id_ciudad) + "'")[0][0]
            ciudad = input("Ingrese la nueva Ciudad (Actual: " +nombre_ciudad+ ",Enter para skip): ")
            if ciudad != "":
                query = "insert into Ciudad (nombre) values ('" + ciudad + "') RETURNING id_ciudad"
                resultado = database.post(query)  # inserta ciudad y ya que pidio el returning resukltado es el id de la ciudad
                query = ("update Equipos set id_ciudad = '" + str(resultado) + "' where id_equipo = '" + str(id_equipo) + "'")
                database.update(query)
            #muestra el presidente actual del equipo y pregunta si desea cambiarlo
            presidente = input("Ingrese el nuevo presidente (Actual: " + database.get("select presidente from Equipos where id_equipo = '" + id_equipo + "'")[0][0]+ ",Enter para skip): ")
            if presidente != "":
                query = ("update Equipos set presidente = '" + presidente + "' where id_equipo = '" + id_equipo + "'")
                database.update(query)
            print("Equipo editado exitosamente")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def listar_equipos(database):
        query = ("select * from Equipos")
        equipos = database.get(query)
        for equipo in equipos:
            query = ("select nombre from Ciudad where id_ciudad = '" + str(equipo[3]) + "'")#es el id de la ciudad en la tabla equipo
            ciudad = database.get(query)
            print("********** Equipo: " + str(equipo[0]) + "********** ")
            print("nombre: "+ str(equipo[1])+ "\n"+ "Presidente: "+ str(equipo[2])+ "\n"+ "Ciudad: "+ str(ciudad[0][0])+"\n" )
            print("Jugadores en el equipo: " + str(equipo[1]))
            controllers.jugador_controller.Jugador_Controller.listar_jugadores(database,equipo[0])
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
                query = ("delete from Equipos where id_equipo = '" + id_equipo + "'") #borra el equipo con el id indicado 
                database.delete(query)
                print("Equipo eliminado")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def ver_equipo(database):
        id_equipo = input("Ingrese el ID del equipo a consultar: ")
        if Equipo_Controller.existe_equipo(database, id_equipo) is False:
            print("El equipo consultado no existe")
        else:
            query = ("select * from Equipos where id_equipo = '" + id_equipo + "'")
            equipo = database.get(query)

            for elemento in equipo:
                query = ("select nombre from Ciudad where id_ciudad = '" + str(elemento[3]) + "'")#es el id de la ciudad en la tabla equipo
                ciudad = database.get(query)
                print("********** Equipo: " + str(elemento[0]) + "********** ")
                print("nombre: "+ str(elemento[1])+ "\n"+ "Presidente: "+ str(elemento[2])+ "\n"+ "Ciudad: "+ str(ciudad[0][0])+"\n" )
                print("Jugadores en el equipo: " + str(elemento[1]))
                #controllers.jugador_controller.Jugador_Controller.listar_jugadores(equipo)
            #controllers.jugador_controller.Jugador_Controller.listar_jugadores(equipo)
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def buscar_jugador_en_equipo(database):
        id_jugador = input("Ingrese el ID del jugador a consultar: ")
        existe_jugador = Jugador_Controller.encontrar_jugador(database, id_jugador)
        id_equipo = input("Ingrese el ID del equipo a consultar: ")
        pos_equipo = Equipo_Controller.existe_equipo(database,id_equipo)
        if pos_equipo is False:
            print("NO hay equipo")
        else:
            if existe_jugador is False:
                print("NO hay jugador")
            else:
                query = ("select * from Jugadores where id_jugador = '" + id_jugador + "'")
                jugador = database.get(query)
                for atributos in jugador:#recorre los campos del jugador
                    print("\n\n\n")
                    if str(id_equipo) == str(atributos[4]):#si coinciden los id de equipo
                        print("Nombre: "+str(atributos[1])+ " pertenece al equipo")
                    else:
                        print(" no pertenece al equipo: ")
        print("\n\n\n")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def eliminar_jugador(database):
        id_jugador = input("Por favor ingrese id del jugador a eliminar: ")
        encontrar = Jugador_Controller.encontrar_jugador(database, id_jugador)
        if encontrar is False:
            print("Jugador no encontrado")
        else:
            #print("El siguiente Jugador sera eliminado: " + database[existe].getNombre())
            respuesta = str(input("¿Desea continuar? S/N: "))
            if respuesta.upper() == "S":
                query = ("delete from Jugadores where id_jugador = '" + id_jugador + "'") #borra el jugadorcon el id indicado 
                database.delete(query)
                print("Jugador eliminado")
        return eq_menu.Equipo_Menu.menu_equipos(database)

    def ver_jugador(database):
        id_jugador = input("Ingrese el ID del jugador a consultar: ")
        existe_jugador = Jugador_Controller.encontrar_jugador(database, id_jugador)
        id_equipo = input("Ingrese el ID del equipo a consultar: ")
        existe = Equipo_Controller.existe_equipo(database, id_equipo)
        if existe is False:
            print("NO hay equipo")

        else:
            if existe_jugador is False:
                print("NO hay jugador")

            else:
                query= ("select * from Jugadores where id_jugador = '" + id_jugador + "'")
                jugador = database.get(query)
                for atributos in jugador:#recorre los campos del jugador
                    print("\n\n\n")
                    print("Nombre:"+str(atributos[1]))
                    print("Edad: "+str(atributos[2]))
                    print("Numero: "+str(atributos[3]))
                    query= ("select nombre from posicion where id_posicion = '" + str(atributos[5]) + "'")
                    nombre_posicion= database.get(query)
                    print("Posicion: "+str(nombre_posicion[0][0])) 
                    print("Id_equipo: "+str(atributos[4]))  
                    print("\n\n\n") 
                    return eq_menu.Equipo_Menu.menu_equipos(database)

            print("No pertenece al equipo: ")
        return eq_menu.Equipo_Menu.menu_equipos(database)
