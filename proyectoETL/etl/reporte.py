from etl.ConexionDB import *
import os
import pandas as pd
from decouple import config

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# Creamos una instancia de la clase ConexiónDB

conexion = ConexionDB( USER = 'root'
                        , PASS = 'root'
                        , HOST = 'mysql'
                        , PORT = '3306'
                        , DATABASE = 'bdhabi' )


def generar_reporte_usuarios(rutaTarget):
    resultado = conexion.count_usuarios()
    reporte = f'Actualmente en la Base de datos se encuentran registrados:{resultado} usuarios'
    with open(f"{rutaTarget}usuarios.txt", "w") as f:
        f.write(reporte)

    #conexion.cerrar_conexion()
    
    
def generar_reporte_propiedades_x_usuario(rutaTarget):
    
    resultado = conexion.count_propiedades_x_usuario()
    df = pd.DataFrame(resultado, columns=['NUMERO_PROPIEDADES', 'ID_USUARIO','CORREO_CONTACTO'])
    df.to_csv(f'{rutaTarget}propiedades_x_usuario.csv', sep='|', index=False, encoding='utf-8')
    
    #conexion.cerrar_conexion()
    
    
def generar_reporte_propiedades_x_tipo_y_estado(rutaTarget):
    resultado = conexion.count_propiedades_x_tipo_y_estado()
    
    df = pd.DataFrame(resultado, columns=['TIPO_INMUEBLE', 'ESTADO','CANTIDAD'])
    df.to_csv(f'{rutaTarget}propiedades_x_tipo_y_estado.csv', sep='|', index=False, encoding='utf-8')
    
    conexion.cerrar_conexion()


