
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd"
)

#print(my_db)

my_curser = my_db.cursor()

my_curser.execute("CREATE DATABASE zukunft")

my_curser.execute("SHOW DATABASES")

for db in my_curser:
    print(db)