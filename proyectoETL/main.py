from etl.preprocesamiento import extraccion_xml
from etl.pipeline import carga_datos
from etl.reporte import *
import os



def main():
    rutaSource = './source/feed.xml'
    rutaTarget = './target/'
    
    
    usuarios,propiedades = extraccion_xml(rutaSource)
    
    carga_datos(usuarios,propiedades)
    generar_reporte_usuarios(rutaTarget)
    generar_reporte_propiedades_x_usuario(rutaTarget)
    generar_reporte_propiedades_x_tipo_y_estado(rutaTarget)
    

if __name__ == "__main__":
    main()
    
    
    