import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector import errorcode
from mysql.connector.errors import ProgrammingError

x = input("enter user name : ")
y = input("enter password : ")
z = input("enter host : ")
x = str(x) + str("\n")
y = str(y) + str("\n")
z = str(z) + str("\n")

try:
    db = mysql.connector.connect(
        user = x,
        passwd = y,
        host = z
    )
    mycursor = db.cursor()
    print(db)
    try:
        mycursor.execute("create database chess;")
        with open("sql.txt","w") as fobj:
            fobj.write(x)
            fobj.write("\n")
            fobj.write(y)
            fobj.write("\n")
            fobj.write(z)
    except ProgrammingError:
        print("database already exists")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)
finally:
    db.close()    
