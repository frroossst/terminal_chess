from collections import namedtuple
import pandas as pd
import mysql.connector

class server():
    def __init__(self):
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

        def check_queen_move(self,position):
            self.position = position
            if self.position[1] in self.hor:
                if int(self.position[2]) in self.ver:
                    print("legal queen move")

        


m = Movement()
pos = "Qb3"
if pos[0] == "Q":
    m.check_queen_move(pos)


        
        
