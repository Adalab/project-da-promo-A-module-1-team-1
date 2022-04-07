import os
import xml.etree.ElementTree as ET
import re


origen = './data_xml.xml'
destino = "./limpieza_projecto"
archivo = os.path.basename(origen)
print(os.getcwd())

tree = ET.parse('data_xml.xml')
root = tree.getroot()
print(root)


with open('data_xml.xml', 'r') as f:
    data = f.read()

# print(data)                                 # comprobación de que abre el archivo xml



# PROBANDO CÓMO ELIMINAR FILA

# root.remove(b)
# ElementTree.dump(root)
# OUTPUT
# <root>
#    <a>1</a>
#    </root>


#PROBANDO A BUSCAR EL PATRÓN DE LA FILA A ELIMINAR EN EL XML

# string_xml = '''<level_0>25969</level_0> 
# <index>25969</index> 
# <time>253</time>'''
# na_probando = re.findall('\<level\_0\>\[\d]<\/level\_0\>',string_xml)

# print(na_probando)
