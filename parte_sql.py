#ABRIR el archivo sql en Python


import mysql.connector

cnx = mysql.connector.connect(user='root', password='AlumnaAdalab',
                              host='127.0.0.1', database='BD_pruebas')


mycursor = cnx.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
try:
    mycursor.execute(sql)
    cnx.commit()
    print(mycursor.rowcount, "registro/s modificado/s.")

except mysql.connector.Error as err:
    print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)

mycursor.execute("SELECT * FROM customers")  
results = mycursor.fetchall()
print(results)





import mysql.connector
import pandas as pd

sql = mysql.connector.connect(host ='localhost',user='root', database='leccion-2-sql', password='AlumnaAdalab')

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
