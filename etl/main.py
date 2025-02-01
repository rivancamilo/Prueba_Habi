import pandas as pd
import xml.etree.ElementTree as et


print('Hola, Mundo Docker!')

arbol = et.parse('./data/feed.xml') 
data2 = arbol.findall('listing') 

for registro, indice in zip(data2, range(1, 6)): 
    name = registro.find('state').text 
    id = registro.find('city').text 
    department = registro.find('colony').text
    
    
    print(f'los valores de i:{registro} - j:{indice} - valor: {name}')
    
