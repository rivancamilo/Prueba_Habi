from etl.ConexionDB import *
from decouple import config

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# Creamos una instancia de la clase ConexiónDB

conexion = ConexionDB( USER = config('DB_USER')
                        , PASS = config('DB_PASSWORD_ROOT')
                        , HOST = config('DB_HOST')
                        , DATABASE = config('DB_NAME') )

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# Insertamos los datos en la base de datos
def carga_datos(usuarios,propiedades):
    for (_, rowUser), (_, rowPropiedad) in zip(usuarios.iterrows(), propiedades.iterrows()):
        
        id_UserBD = conexion.insert_usuario(rowUser.correo_contacto)
        print(f'Hemos insertado el correo {rowUser.correo_contacto} con id{id_UserBD}')
        
        id_propiedadBD = conexion.insert_propiedad(rowPropiedad.estado, rowPropiedad.ciudad, rowPropiedad.colonia, 
                                                   rowPropiedad.calle, rowPropiedad.numero_exterior, rowPropiedad.tipo_inmueble, 
                                                   rowPropiedad.transaccion, rowPropiedad.precio, rowPropiedad.codigo_proveedor, 
                                                   rowPropiedad.telefono_contacto, id_UserBD)
        print('\n************************************************************')
        print(f'Hemos insertado una nueva propiedad con id: {id_propiedadBD}')
    
    # ------------------------------------------------------------------   
    # Cerramos la conexión de la base de datos
    conexion.cerrar_conexion()
        