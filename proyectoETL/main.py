from etl.preprocesamiento import extraccion_xml
from etl.pipeline import carga_datos
from etl.reporte import *

def main():
    rutaSource = './source/feed.xml'
    rutaTarget = './target/'
    
    usuarios,propiedades = extraccion_xml(rutaSource)
    carga_datos(usuarios,propiedades)
    
    print('Hola, Mundo Docker!')
    print(usuarios)
    
    

if __name__ == "__main__":
    main()