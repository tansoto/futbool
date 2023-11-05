from views import jugador_menu as jug_menu
from models.jugadores import Jugadores
from models.equipos import Equipos
import controllers


class Jugador_Controller:
    def listar_jugadores(database,id_equipo):
        nomina = database.get("select * from jugadores where id_equipo = '" + str(id_equipo) + "'")
        for jugador in nomina:
            print("----------Jugador id: " + str(jugador[0]) + "----------")
        
            print("Nombre:"+str(jugador[1]))
            print("Edad: "+str(jugador[2]))
            print("Numero: "+str(jugador[3]))
            query= ("select nombre from posicion where id_posicion = '" + str(jugador[5]) + "'")
            nombre_posicion= database.get(query)
            print("Posicion: "+str(nombre_posicion[0][0])) 
            print("Id_equipo: "+str(jugador[4]))  
            

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
            nombre = input("Ingrese el nuevo nombre del jugador (Actual: "+ database.get("select nombre from Jugadores where id_jugador = '" + id_jugador + "'")[0][0] + ",Enter para skip): ")
            if nombre != "":
                query = ("update Jugadores set nombre = '" + nombre +"' where id_jugador = '" + id_jugador + "'")
                database.update(query)
            edad = str(input("Ingrese la nueva edad del jugador (Actual: "+ str(database.get("select edad from Jugadores where id_jugador = '" + str(id_jugador) + "'")[0][0]) + ",Enter para skip): "))
            if edad != "":
                query = ("update Jugadores set edad = '" + edad +"' where id_jugador = '" + id_jugador + "'")
                database.update(query)
            id_posicion = database.get("select id_posicion from Jugadores where id_jugador = '" + id_jugador + "'")
            nombre_posicion = str(database.get("select nombre from Posicion where id_posicion = '" + str(id_posicion) + "'"))[0][0]
            posicion = str(input("Ingrese la nueva posicion del jugador (Actual: "+ nombre_posicion + ",Enter para skip): "))
            if posicion != "":
                query = "insert into Posicion (nombre) values ('" + posicion + "') RETURNING id_posicion"
                # inserta ciudad y ya que pidio el returning resukltado es el id de la ciudad
                resultado = database.post(query)
                query = ("update Jugadores set id_posicion = '" + str(resultado) +"' where id_jugador = '" + str(id_jugador) + "'")
                database.update(query)
            numero = input(
                "Ingrese el nuevo numero del jugador (Actual: "+ str(database.get("select numero from Jugadores where id_jugador = '" + id_jugador + "'")[0][0]) + ",Enter para skip): ")
            if numero != "":
                query = ("update Jugadores set numero = '" + numero +"' where id_jugador = '" + id_jugador + "'")
                database.update(query)
            id_equipo = database.get("select id_equipo from Jugadores where id_jugador = '" + str(id_jugador) + "'")[0][0]
            nombre_equipo = database.get("select nombre from Equipos where id_equipo = '" + str(id_equipo) + "'")[0][0]
            id_nuevo_equipo = input("Ingrese el nuevo id de equipo del jugador (Actual: "+ nombre_equipo+ ",Enter para skip): ")
            if id_nuevo_equipo != "":
                existe_nuevo_equipo = controllers.equipo_controller.Equipo_Controller.existe_equipo(database, id_nuevo_equipo)
                if existe_nuevo_equipo is not False:
                    # inserta equipo y ya que pidio el returning resukltado es el id de la ciudad
                    query = ("update Jugadores set id_equipo = '" + str(id_nuevo_equipo) +"' where id_jugador = '" + str(id_jugador) + "'")
                    database.update(query)
                    print("Jugador editado correctamente")
        jug_menu.Jugador_Menu.menu_jugadores(database)
