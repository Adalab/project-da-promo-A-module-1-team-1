import os
import xml.etree.ElementTree as ET


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
# Eliminar elemento del xml
# https://stackoverflow.com/questions/3593204/how-to-remove-elements-from-xml-using-python
# https://www.adamsmith.haus/python/examples/3595/xml-remove-a-subelement-from-an-xml-element
# https://itqna.net/questions/4202/how-remove-element-xml-python


# root.remove(b)
# ElementTree.dump(root)
# OUTPUT
# <root>
#    <a>1</a>
#    </root>
