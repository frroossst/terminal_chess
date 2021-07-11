import mysql.connector

db = mysql.connector.connect(
    host = z,
    user = x,
    passwd = y,
    database = "chess"
)
mycursor = db.cursor()

