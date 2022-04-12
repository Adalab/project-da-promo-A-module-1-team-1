import os
import xml.etree.ElementTree as ET
import re

 
os.chdir("/mnt/c/Users/a/Desktop/Adalab/ejercicios-resueltos-clase-invertida-DA-promoA/")
print("Estamos aqui", os.getcwd())
origen = '/mnt/c/Users/a/Desktop/Adalab/ejercicios-resueltos-clase-invertida-DA-promoA/'
destino = "./limpieza_projecto"
archivo = os.path.basename(origen)


############################################################################## OPCIÓN 1: compleja
tree = ET.parse('data_xml_trozo.xml')
root = tree.getroot()
print("Esta es la ruta, ", root)

# # data_nuevo = ET.parse('data_xml_limpio.xml')
with open('data_xml_trozo.xml', 'r') as data:
    

    for child in root:
        print(child.tag)
        
        for subchild in child:
            linea_level = re.findall('\<level\_0\>[\d]*', data.read())
            linea_nueva = re.sub('\<level\_0\>[\d]*'," ", data.read())
            print('  ',subchild.tag)
 
with open('data_xml_limpio.xml', 'w') as data:
    xml_nuevo = data.write(linea_nueva)
    print(xml_nuevo)

########################################################################## OPCIÓN 2: simple

with open('data_xml_trozo.xml', 'r') as data:
    data = root.read()

    for line in data:
            if line.tag == "level_0":
                line.tag.remove()
            else:
                pass
        
    with open('data_xml_limpio.xml', 'w') as data_nuevo:  
        
        



        
        
#PROBANDO a eliminar patrón
print(na_probando)
#elminacion=doc.find("xml")
#eliminacion.remove(eliminacion.find("'\<level\_0\>\[\d]<\/level\_0\>")
#La intencion es crear un bucle donde encuentre la palabra level por cada root y la elimine

