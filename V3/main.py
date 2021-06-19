from collections import namedtuple
import pandas as pd
import mysql.connector
from pandas.io.parsers import count_empty_vals

db = mysql.connector.connect(
    host = "localhost",
    user = "home",
    passwd = "home",
    database = "chess"
)
mycursor = db.cursor()

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
    def __init__(self) -> None:
        pass

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
            Movement.trace_route(self)

        def trace_route(self):
            print("tracing route")

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
    move = "Qb1"
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

main()