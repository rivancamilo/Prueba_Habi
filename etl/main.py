import pandas as pd
import xml.etree.ElementTree as et
import os

print('Hola, Mundo Docker!')

arbol = et.parse('./source/feed.xml') 
data2 = arbol.findall('listing') 
datos = []

for registro, indice in zip(data2, range(1, 6)): 
    estado = registro.find('state').text 
    ciudad = registro.find('city').text 
    colonia = registro.find('colony').text
    
    datos.append({'Estado':estado,
                  'Ciudad':ciudad,
                  'Colonia':colonia})
    
    
    print(f'los valores de i:{indice} - registro:{registro} - valor: {estado}')
    
#creamos un dataframe
df = pd.DataFrame(datos)

#exportanos el dataFrame
df.to_csv('./target/datos.csv', sep='|', index=False, encoding='utf-8')
    
    
directorio = "./target"
contenido = os.listdir(directorio)
print(contenido)
                       