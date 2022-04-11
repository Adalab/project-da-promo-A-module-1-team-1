
#Pseudocógido

#En qué carpeta estamos
                                                                            #tenéis que crear las carpetas: limpieza_proyecto en escritorio), prueba_proyecto en Descargas.

import os 
os.getcwd()
                                                                            #Asumimos que el cliente va a hacer esto: descargar los archivos --> Carpeta por defecto Descargas.

try:                                                                        #mirar si el try cumple todas las posibilidades
  os.mkdir("/mnt/c/Users/a/Desktop/limpieza_projecto")                      #crear carpeta donde vamos a mover los archivos (carpeta definitiva: limpieza_proyecto) (input para que lo de fina el cliente?)
except OSError:                                                             #try/excep/else para que no nos de error si la carpeta ya existe
  print("La creación del directorio falló porque ya existe")
else:
  print("Se ha creado el directorio :) ")



                                                                            
os.rename('C:/Users/a/Downloads/prueba_projecto1/data_txt.txt','C:/Users/a/Escritorio/limpieza_projecto')     #movemos archivo descargado a la carpeta definitiva  : limpieza proyecto
                                                                            #abrimos carpeta TXT y XML (GUADA, LAU: XML. ALICIA, LARA: TXT)
                                                                            #leemos archivo por líneas (read()--> sin argumento para todo el documento)
                                                                            #cerramos carpeta o utilizamos WITH 




########### PARTE TXT




############# PARTE XML










