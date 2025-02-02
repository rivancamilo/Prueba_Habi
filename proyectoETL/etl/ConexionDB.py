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
    
    
    
