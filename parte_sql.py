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
