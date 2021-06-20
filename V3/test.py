import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "home",
    passwd = "home",
    database = "chess"
)
mycursor = db.cursor()
query = "delete from board where Location = 'd7';"
mycursor.execute(query)
db.commit()