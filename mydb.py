import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sqlcode1'
)
#prepare a cursor object
cursorobj = dataBase.cursor()

#create a database
cursorobj.execute("CREATE DATABASE swarajdb")

print("All Done!")