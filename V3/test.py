import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "home",
    passwd = "home",
    database = "chess"
)
mycursor = db.cursor()

mycursor.execute("select count(*) from board;")
result = mycursor.fetchall()
for i in result:
    rowCount = i
print(rowCount[0])
print(int(rowCount[0])-1)
