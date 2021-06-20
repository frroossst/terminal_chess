from codecs import backslashreplace_errors
from collections import namedtuple
import pandas as pd
import mysql.connector
from pandas.io.parsers import count_empty_vals
import logging
import time


logging.basicConfig(filename='debug.log', level=logging.DEBUG,format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("--- INITIALIZED ---")

db = mysql.connector.connect(
    host = "localhost",
    user = "home",
    passwd = "home",
    database = "chess"
)
mycursor = db.cursor()
logging.info("sql server connection established")

class Pieces():
    w_king = "♔"
    b_king = "♚"
    w_queen = "♕"
    b_queen = "♛"
    w_bishop = "♗"
    b_bishop = "♝"
    w_knight = "♘" 
    b_knight = "♞" 
    w_rooke = "♖" 
    b_rooke = "♜"
    w_pawn = "♙"
    b_pawn = "♟" 

class Board(Pieces):
    def __init__(self):
        mycursor.execute("drop table board")
        mycursor.execute("create table board (Location char(5), Piece varchar(15), Colour char(5));")
        #white pieces data entry
        logging.debug("white pieces data entry")
        mycursor.execute("insert into board values ('d1','Queen','White');")
        mycursor.execute("insert into board values ('e1','King','White');")
        mycursor.execute("insert into board values ('f1','Bishop','White');")
        mycursor.execute("insert into board values ('c1','Bishop','White');")
        mycursor.execute("insert into board values ('g1','Knight','White');")
        mycursor.execute("insert into board values ('b1','Knight','White');")
        mycursor.execute("insert into board values ('h1','Rook','White');")
        mycursor.execute("insert into board values ('a1','Rook','White');")
        mycursor.execute("insert into board values ('a2','Pawn','White');")
        mycursor.execute("insert into board values ('b2','Pawn','White');")
        mycursor.execute("insert into board values ('c2','Pawn','White');")
        mycursor.execute("insert into board values ('d2','Pawn','White');")
        mycursor.execute("insert into board values ('e2','Pawn','White');")
        mycursor.execute("insert into board values ('f2','Pawn','White');")
        mycursor.execute("insert into board values ('g2','Pawn','White');")
        mycursor.execute("insert into board values ('h2','Pawn','White');")
        db.commit()
        #black pieces data entry
        logging.debug("black pieces data entry")
        mycursor.execute("insert into board values ('d8','Queen','Black');")
        mycursor.execute("insert into board values ('e8','King','Black');")
        mycursor.execute("insert into board values ('f8','Bishop','Black');")
        mycursor.execute("insert into board values ('c8','Bishop','Black');")
        mycursor.execute("insert into board values ('g8','Knight','Black');")
        mycursor.execute("insert into board values ('b8','Knight','Black');")
        mycursor.execute("insert into board values ('h8','Rook','Black');")
        mycursor.execute("insert into board values ('a8','Rook','Black');")
        mycursor.execute("insert into board values ('a7','Pawn','Black');")
        mycursor.execute("insert into board values ('b7','Pawn','Black');")
        mycursor.execute("insert into board values ('c7','Pawn','Black');")
        mycursor.execute("insert into board values ('d7','Pawn','Black');")
        mycursor.execute("insert into board values ('e7','Pawn','Black');")
        mycursor.execute("insert into board values ('f7','Pawn','Black');")
        mycursor.execute("insert into board values ('g7','Pawn','Black');")
        mycursor.execute("insert into board values ('h7','Pawn','Black');")
        db.commit()

    def create_board(self):
        li= [[Pieces.b_rooke,Pieces.b_knight,Pieces.b_bishop,Pieces.b_queen,Pieces.b_king,Pieces.b_bishop,Pieces.b_knight,Pieces.b_rooke,"8"],
             [Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,"7"],
             [" "," "," "," "," "," "," "," ","6"],
             [" "," "," "," "," "," "," "," ","5"],   
             [" "," "," "," "," "," "," "," ","4"],
             [" "," "," "," "," "," "," "," ","3"],
             [Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,"2"],
             [Pieces.w_rooke,Pieces.w_knight,Pieces.w_bishop,Pieces.w_queen,Pieces.w_king,Pieces.w_bishop,Pieces.w_knight,Pieces.w_rooke,"1"],
        ]
        for i in li:
            print(i)
        label = ["a","b","c","d","e","f","g","h"]
        print(label)
        logging.debug("starting position board printed")
        

class Movement():
        hor = ["a","b","c","d","e","f","g","h"]
        ver = [1,2,3,4,5,6,7,8]

        def __init__(self) -> None:
            pass

        def get_current_loc(self,piece,pos):
            self.piece = piece
            self.pos = pos
            query = "select Loc from pieces where Name = '%s';"
            mycursor.execute(query % self.piece)
            result = mycursor.fetchall()
            for i in result:
                for j in i:
                    print(j)
            print("at get current loc!")
            self.current_loc = j
            Movement.trace_route(self,self.current_loc,self.piece,self.pos)

        def trace_route(self,current_loc,piece,future_loc):
            long = [1,2,3,4,5,6,7,8]
            diag = []
            print("tracing route")
            self.current_loc = current_loc
            self.future_loc = future_loc
            self.piece = piece
            print(f"moving {self.piece} from {self.current_loc} to {self.future_loc}")
            #to check if the move is longitudnal and not diagonal
            if str(self.future_loc[0]) == str(self.current_loc[0]):
                print("the move is longitudnal")
                if self.current_loc[1] > self.future_loc[1]:
                    pass
                elif self.current_loc[1] < self.future_loc[1]:
                    while True:
                        loc_num_check = int(self.current_loc[1]) + 1
                        loc_square_check = str(self.current_loc[0]) + str(loc_num_check)
                        print(loc_square_check)
                        time.sleep(1)
                        if str(loc_square_check) == str(self.future_loc):
                            break
                    print("path clear")

        def check_queen_move(self,move,count):
            self.move = move
            self.count = count
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    #insert check for occupied squares
                    #insert obstacle check
                    print("legal queen move")
                    self.move = self.move[1] + self.move[2]
                    Movement.get_current_loc(self,"Queen",self.move)

        def check_king_move(self,position,count):
            self.position = position
            if self.position[1] in self.hor:
                if int(self.position[2]) in self.ver:
                    print("legal king move")
                    
        def check_bishop_move(self,position,count):
            self.position = position
            self.count = count
            print(self.position,self.count)

def main():
    b = Board()
    b.create_board()
    m = Movement()
    move = "Qd4"
    global count
    count = 0
    count += 1
    global which
    which = "" #current position for the piece to be moved
    if move[0] == "K":
        m.check_king_move(move,count)

    elif move[0] == "Q":
        m.check_queen_move(move,count)

    elif move[0] == "B":
        m.check_bishop_move(move,count)

    elif move[0] == "N":
        which = input("enter current position of the rook to be moved : ")
        m.check_knight_move(move,count,which)

    elif move[0] == "p":
        m.check_pawn_move(move)

    elif move[0] == "R":
        which = input("enter current position of the rook to be moved : ")
        m.check_rook_move(move,count,which)      


logging.info("main()")
main()