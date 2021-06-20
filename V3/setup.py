import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector import errorcode

x = input("enter user name : ")
y = input("enter password : ")
z = input("enter host : ")

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
    except:
        print("database already exists")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)
