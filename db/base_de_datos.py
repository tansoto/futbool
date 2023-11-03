import psycopg2


class BaseDeDatos:
    # constructor
    def __init__(self):
        self.__db_params = {
            "dbname": "futbool",
            "user": "postgres",
            "password": "123456789",
            "host": "localhost",
            "port": "5432",
        }

    # metodo para traer los datos de la base de datos
    def get(self, query):
        try:
            conn = psycopg2.connect(**self.__db_params)

            cursor = conn.cursor()

            cursor.execute(query)

            result = cursor.fetchall()

            cursor.close()
            conn.close()

        except psycopg2.Error as e:
            result = e
        return result

    # metodo para insertar datos en la base de datos
    def post(self, query):
        try:
            conn = psycopg2.connect(**self.__db_params)

            cursor = conn.cursor()

            cursor.execute(query)

            conn.commit()
            id_del_ingresado = cursor.fetchone()[0]  # aqui se obtiene el id del registro que se acaba de ingresar
            print("id del ingresado:", id_del_ingresado)
            cursor.close()
            conn.close()
            if id_del_ingresado is None:#si se ejecuta una query donde no se retorna un id, se retorna True para seguir su flujo
                return True
            else:#si se ejecuta una query donde se retorna un id, se retorna el id correspondiente
                return id_del_ingresado
        except psycopg2.Error as e:
            if e == "no results to fetch":#significa que fetch no se ejecuto correctamente ya que la query no tiene un returning
                return True
            print("Error al conectar a la base de datos:", e)
            return False

    # metodo para actualizar datos en la base de datos
    def update(self, query):
        try:
            conn = psycopg2.connect(**self.__db_params)

            cursor = conn.cursor()

            cursor.execute(query)

            conn.commit()  # aqui se hace el commit para que se guarden los cambios en la base de datos

            cursor.close()
            conn.close()

            return True
        except psycopg2.Error as e:
            print("Error al conectar a la base de datos:", e)

    def delete(self, query):
        try:
            conn = psycopg2.connect(**self.__db_params)

            cursor = conn.cursor()

            cursor.execute(query)

            conn.commit()

            cursor.close()
            conn.close()

            return True
        except psycopg2.Error as e:
            print("Error al conectar a la base de datos:", e)
