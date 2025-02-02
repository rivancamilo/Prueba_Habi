## importamos las librerías

import mysql.connector
from mysql.connector import errorcode

class ConexionDB:
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Definimos el método constructor con los parámetros 
    # iniciales para establecer una conexión con Mysql
    def __init__(self, USER, PASS, HOST, DATABASE):
        self.USER = USER
        self.PASS = PASS
        self.HOST = HOST
        self.DATABASE = DATABASE
        self.conn = None
        
        try:
            self.conn = mysql.connector.connect(
                user=self.USER,
                password=self.PASS,
                host=self.HOST,
                database=self.DATABASE
            )
            self.conn.autocommit = False
            print(f"Estamos conectados a la Base de datos: {self.DATABASE}")
            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error el usuario o la contraseña son incorrectos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(f"La BD {self.DATABASE} a la que se está conectando NO existe")
            else:
                print(err)
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Método para ejecutar querys
    def ejecutar_query(self, query, params):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.lastrowid

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Método para confirmar los cambios en la base de datos
    def commit(self):
        self.conn.commit()

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Método para insertamos un nuevo usuario en el cual devolvemos el id del usuario
    def insert_usuario(self, correo_contacto):
        
        # ------------------------------------------------------------------
        # Validamos si el usuario ya existe con ese correo
        sql_query = "SELECT idusuario FROM usuarios WHERE correo_contacto = %s"
        cursor = self.conn.cursor()
        cursor.execute(sql_query, (correo_contacto,))
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"\t *****  El correo {correo_contacto} ya existe con idusuario {resultado[0]}")
            return resultado[0]  
        
        # ------------------------------------------------------------------
        # Query para insertar un nuevo usuario
        query = """
            INSERT INTO usuarios (correo_contacto) 
            VALUES (%s)
        """
        usuario_id = self.ejecutar_query(query, (correo_contacto,))
        self.commit()
        return usuario_id
    
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Método para insertar una nueva propiedad
    def insert_propiedad(self, estado, ciudad, colonia, calle, numero_exterior, tipo_inmueble, 
                         transaccion, precio, codigo_proveedor, telefono_contacto, idusuario):
        
        query = """
            INSERT INTO propiedades (estado, ciudad, colonia, calle, numero_exterior, tipo_inmueble, 
                                    transaccion, precio, codigo_proveedor, telefono_contacto, idusuario) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        propiedad_id = self.ejecutar_query(query, (estado, ciudad, colonia, calle, numero_exterior, tipo_inmueble, 
                                               transaccion, precio, codigo_proveedor, telefono_contacto, idusuario))
        self.commit()
        return propiedad_id
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Método para cerrar la conexión en la base de datos
    def cerrar_conexion(self):
        if self.conn:
            self.conn.close()
            print("La conexión se cerró, correctamente ")
    
    
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ---------     Preguntas del negocio   ----------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------