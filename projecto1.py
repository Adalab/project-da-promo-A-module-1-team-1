
#Pseudocógido

#En qué carpeta estamos
                                                                            #tenéis que crear las carpetas: limpieza_proyecto en escritorio), prueba_proyecto en Descargas.

import os 
os.getcwd()
                                                                            #Asumimos que el cliente va a hacer esto: descargar los archivos --> Carpeta por defecto Descargas.
os.mkdir('C:/Users/a/Escritorio/limpieza_projecto')                         #crear carpeta donde vamos a mover los archivos (carpeta definitiva: limpieza_proyecto) (tal vez un input para que lo de fina el cliente?)
os.rename('C:/Users/a/Downloads/prueba_projecto1/data_txt.txt','C:/Users/a/Escritorio/limpieza_projecto')     #movemos archivo descargado a la carpeta definitiva  : limpieza proyecto
                                                                            #abrimos carpeta TXT y XML (GUADA, LAU: XML. ALICIA, LARA: TXT)
                                                                            #leemos archivo por líneas (read()--> sin argumento para todo el documento)
                                                                            #cerramos carpeta o utilizamos WITH 








#ESTE ES EL ESQUEMA DE LOS POSIBLES ERRORES A LIMPIAR HECHO EN GITHUB.
#A TENERLO EN CUENTA MÁS ADELANTE.
# Después de observar los archivos hemos llegado a la conclusión que los posibles errores de limpieza a solucionar son:
# Esperando votación SOLO EN XML de todas las integrantes. Las opciones para TXT se van a realizar TODAS. Propuestas de día 01/04.

# En: XML:

#  Limpieza la parte de la fila donde pone level es [0] porque siempre es igual (elegir esta): GUADA.

#  Limpieza de la fila total ya que tiene la misma info que index. En el caso que se necesite la fila level, borramos solo la parte del 0 (o elegir esta). LAURA, ALICI, LARA.

# En: TXT:

#  Asumiendo que NO conocemos las unidades de la variable tiempo (el cliente no nos la ha dicho), podemos dejar sin hacer una conversión de momento.

#  Cadena de Nulls no se repiten en otras las filas, así que no podemos eliminarlas.

#  Limpiar espacios sobrantes de:
# - antes de la coma (pueden ser 1 o 2 espacios demás) ( ej: ;null, Visual Studio Code (VSCode) ,
# PyCharm , Jupyter Notebook;
# - antes y después palabra (ejemplo: PyCharm )

# En SQL:

# Limpieza de espacios a la izquierda en la columna q10_part_1

# Cambio de ERROR por NULL? Veremos en el futuro si es necesario o no dependiendo de si "rellenaremos la tabla con info la info del txt y el xml o no"
