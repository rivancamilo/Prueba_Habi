from etl.ConexionDB import *
from decouple import config

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# Creamos una instancia de la clase ConexiónDB

conexion = ConexionDB( USER = config('DB_USER')
                        , PASS = config('DB_PASSWORD_ROOT')
                        , HOST = config('DB_HOST')
                        , DATABASE = config('DB_NAME') )

print(conexion)


