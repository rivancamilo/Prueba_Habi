import pandas as pd
import xml.etree.ElementTree as et
import re


# creamos una funcion para limpiar los textos
def limpiar_texto(texto: str):
    # Convertir a minúsculas
    texto = texto.lower()
    # Eliminar caracteres especiales dejando solo letras y espacios
    texto = re.sub(r'[^a-záéíóúüñ ]', '', texto)
    return texto


# Creamos una funcion para sacar las propiedades del XML
def extraccion_xml(archivo):
    
    idPropiedad = 9999
    usuarios = []
    propiedades = []
    
    arbol = et.parse(archivo) 
    data2 = arbol.findall('listing')
    for indice,registro in enumerate(data2, start=1):
    #for registro,indice in zip(data2, range(1, 5)): ###para pruebas
        estado = limpiar_texto(registro.find('state').text)
        ciudad = limpiar_texto(registro.find('city').text)
        colonia = limpiar_texto(registro.find('colony').text)
        calle = registro.find('street').text
        numero_exterior = registro.find('external_num').text
        tipo_inmueble = limpiar_texto(registro.find('type').text)
        transaccion = limpiar_texto(registro.find('purpose').text)
        precio = registro.find('price').text
        codigo_proveedor = registro.find('code').text
        correo_contacto = registro.find('mail_contact').text
        telefono_contacto = registro.find('phone_contact').text
        
        
        usuarios.append({'idusuario': indice, 
                         'correo_contacto': correo_contacto
                         })
        
        
        propiedades.append({'idpropiedad':idPropiedad+indice,'estado':estado,
                            'ciudad':ciudad,'colonia':colonia,
                            'calle':calle,'numero_exterior':numero_exterior,
                            'tipo_inmueble':tipo_inmueble,'transaccion':transaccion,
                            'precio':precio,'codigo_proveedor':codigo_proveedor,
                            'telefono_contacto':telefono_contacto,'idusuario':indice
                            })
        
    return pd.DataFrame(usuarios), pd.DataFrame(propiedades)