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
        
        # mycursor.execute("create table startBoard (Location char(5), Piece varchar(15), Colour char(5), Which char(5));")
        # mycursor.execute("insert into startBoard values ('d1','Queen','White',NULL);")
        # mycursor.execute("insert into startBoard values ('e1','King','White',NULL);")
        # mycursor.execute("insert into startBoard values ('f1','Bishop','White',NULL);")
        # mycursor.execute("insert into startBoard values ('c1','Bishop','White',NULL);")
        # mycursor.execute("insert into startBoard values ('g1','Knight','White','g1');")
        # mycursor.execute("insert into startBoard values ('b1','Knight','White','b1');")
        # mycursor.execute("insert into startBoard values ('h1','Rook','White','h1');")
        # mycursor.execute("insert into startBoard values ('a1','Rook','White','a1');")
        # mycursor.execute("insert into startBoard values ('a2','Pawn','White','a2');")
        # mycursor.execute("insert into startBoard values ('b2','Pawn','White','b2');")
        # mycursor.execute("insert into startBoard values ('c2','Pawn','White','c2');")
        # mycursor.execute("insert into startBoard values ('d2','Pawn','White','d2');")
        # mycursor.execute("insert into startBoard values ('e2','Pawn','White','e2');")
        # mycursor.execute("insert into startBoard values ('f2','Pawn','White','f2');")
        # mycursor.execute("insert into startBoard values ('g2','Pawn','White','g2');")
        # mycursor.execute("insert into startBoard values ('h2','Pawn','White','h2');")
        # db.commit()
        # mycursor.execute("insert into startBoard values ('d8','Queen','Black',NULL);")
        # mycursor.execute("insert into startBoard values ('e8','King','Black',NULL);")
        # mycursor.execute("insert into startBoard values ('f8','Bishop','Black',NULL);")
        # mycursor.execute("insert into startBoard values ('c8','Bishop','Black',NULL);")
        # mycursor.execute("insert into startBoard values ('g8','Knight','Black','g8');")
        # mycursor.execute("insert into startBoard values ('b8','Knight','Black','b8');")
        # mycursor.execute("insert into startBoard values ('h8','Rook','Black','h8');")
        # mycursor.execute("insert into startBoard values ('a8','Rook','Black','a8');")
        # mycursor.execute("insert into startBoard values ('a7','Pawn','Black','a7');")
        # mycursor.execute("insert into startBoard values ('b7','Pawn','Black','b7');")
        # mycursor.execute("insert into startBoard values ('c7','Pawn','Black','c7');")
        # mycursor.execute("insert into startBoard values ('d7','Pawn','Black','d7');")
        # mycursor.execute("insert into startBoard values ('e7','Pawn','Black','e7');")
        # mycursor.execute("insert into startBoard values ('f7','Pawn','Black','f7');")
        # mycursor.execute("insert into startBoard values ('g7','Pawn','Black','g7');")
        # mycursor.execute("insert into startBoard values ('h7','Pawn','Black','h7');")
        # db.commit()
        
        mycursor.execute("create table castle (Location char(5), Piece varchar(15), Colour char(5), Moved char(1));")
        mycursor.execute("insert into castle values ('a1','Rook','White','n');")
        mycursor.execute("insert into castle values ('h1','Rook','White','n');")
        mycursor.execute("insert into castle values ('a8','Rook','Black','n');")
        mycursor.execute("insert into castle values ('h8','Rook','Black','n');")
        mycursor.execute("insert into castle values ('e1','King','White','n');")
        mycursor.execute("insert into castle values ('e8','King','Black','n');")

    except ProgrammingError:
        print("database already exists")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)
finally:
    db.close()    
