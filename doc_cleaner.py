import os
import re
import shutil
import xml.etree.ElementTree as ET
import mysql.connector
import pandas as pd

# FUNCIONES DE LECTURA

# 1. Lectura de texto


def txt(archivo):
    with open(archivo, "r") as f:

        f2 = f.read()

        _1 = re.sub('\n', "\n\n", f2)

        _2 = re.sub("\s+\,", ",", _1)

        _3 = _2.replace("null", "")

    with open(archivo, "w") as a:
        archivo_nuevo = a.write(_3)

    return(archivo_nuevo)


# 2. Lectura xml

# def xml(nuevo):

# ET.archivo.parse()
#   with open(nuevo, "r") as f:
#    with open(nuevo, "w") as a:
#       texto = a.write(_3)
#  return(texto)

# 3. Lectura sql

def docsql(archivo):
    sql = mysql.connector.connect(
        host='localhost', user='root', database='proyecto_1', password='AlumnaAdalab')

    cursor = sql.cursor()
    limpieza_error = "UPDATE data_sql SET Q10_Part_11 = 'null' WHERE Q10_Part_11 = 'ERROR'"

    try:
        cursor.execute(limpieza_error)
        sql.commit()
        print(cursor.rowcount, "registro/s modificado/s.")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)

    cursor.execute("SELECT * FROM data_sql LIMIT 12")
    resultado = cursor.fetchall()
    df = pd.DataFrame(resultado)
    print(df)

    sql.close()

#   with open(archivo, "r") as f:

#  with open(archivo, "w") as a:
#     texto = a.write(_3)

# return(texto)


# FUNCIÓN DE SELECCIÓN DE TIPO (TXT / XML / SQL) Y CREACIÓN DE ARCHIVO DE DESTINO
def apertura_archivo(origen):

    try:
        os.mkdir("./docs_tratados")
    except:
        pass

    archivo = "./docs_tratados/archlimpio_" + origen
    ruta = "./data.txt"
    shutil.copyfile(ruta, archivo)

    if archivo[-3:] == 'txt':
        x = txt(archivo)
    elif archivo[-3:] == 'xml':
        pass
       #x = xml(archivo)
    elif archivo[-3:] == 'sql':
        x = docsql(archivo)
    else:
        x = "Lo sentimos. Nuestro text cleaner solo acepta archivos .sql, .xml y .txt"
        print(x)

    return (x)

# ______________________________________________________________________________________________________

# FUNCION PRINCIPAL
# ______________________________________________________________________________________________________


def doc_cleaner(origen):

    # INICIO
    print("¡Hola! Con este programa vamos a preparar tu archivo. Asegúrate de que el archivo a convertir está en esta misma carpeta:")
    print(os.getcwd(), '\n')

    # BUSCAMOS EL ARCHIVO

    if origen in os.listdir():
        print("Hemos encontrado tu archivo, ¡te lo preparamos enseguida! \n")
        apertura_archivo(origen)
    else:
        print("El archivo no está en la carpeta correcta. Asegúrate de trasladarlo a:")
        print(os.getcwd(), '\n')


# ______________________________________________________________________________________________________
#
#  LLAMADA A FUNCIONES:
# ______________________________________________________________________________________________________

# DOCUMENTOS TIPO .TXT
#origen = "data.txt"
# doc_cleaner(origen)


# DOCUMENTOS TIPO .XML
# origen = "data.xml"
# doc_cleaner(origen)


# DOCUMENTOS TIPO .SQL
origen = "data.sql"
doc_cleaner(origen)
