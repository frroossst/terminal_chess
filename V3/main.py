from codecs import backslashreplace_errors
from collections import namedtuple
from types import coroutine
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
# mycursor.execute("insert into board values ('d2','Pawn','White');")
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

class Pieces():
    b_king = "♔"
    w_king = "♚"
    b_queen = "♕"
    w_queen = "♛"
    b_bishop = "♗"
    w_bishop = "♝"
    b_knight = "♘" 
    w_knight = "♞" 
    b_rooke = "♖" 
    w_rooke = "♜"
    b_pawn = "♙"
    w_pawn = "♟" 

class Board(Pieces):

    li= [[Pieces.b_rooke,Pieces.b_knight,Pieces.b_bishop,Pieces.b_queen,Pieces.b_king,Pieces.b_bishop,Pieces.b_knight,Pieces.b_rooke,"8"],
             [Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,"7"],
             [" "," "," "," "," "," "," "," ","6"],
             [" "," "," "," "," "," "," "," ","5"],   
             [" "," "," "," "," "," "," "," ","4"],
             [" "," "," "," "," "," "," "," ","3"],
             [Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,"2"],
             [Pieces.w_rooke,Pieces.w_knight,Pieces.w_bishop,Pieces.w_queen,Pieces.w_king,Pieces.w_bishop,Pieces.w_knight,Pieces.w_rooke,"1"],
        ]

    label = ["a","b","c","d","e","f","g","h"]

    li_ref_empty = [
        [" "," "," "," "," "," "," "," ","8"],        
        [" "," "," "," "," "," "," "," ","7"],
        [" "," "," "," "," "," "," "," ","6"],
        [" "," "," "," "," "," "," "," ","5"],
        [" "," "," "," "," "," "," "," ","4"],
        [" "," "," "," "," "," "," "," ","3"],
        [" "," "," "," "," "," "," "," ","2"],
        [" "," "," "," "," "," "," "," ","1"],        
    ]

    li_ref_dict =  {
            "a1":(7,0),"a2":(6,0),"a3":(5,0),"a4":(4,0),"a5":(3,0),"a6":(2,0),"a7":(1,0),"a8":(0,0),
            "b1":(7,1),"b2":(6,1),"b3":(5,1),"b4":(4,1),"b5":(3,1),"b6":(2,1),"b7":(1,1),"b8":(0,1),
            "c1":(7,2),"c2":(6,2),"c3":(5,2),"c4":(4,2),"c5":(3,2),"c6":(2,2),"c7":(1,2),"c8":(0,2),
            "d1":(7,3),"d2":(6,3),"d3":(5,3),"d4":(4,3),"d5":(3,3),"d6":(2,3),"d7":(1,3),"d8":(0,3),
            "e1":(7,4),"e2":(6,4),"e3":(5,4),"e4":(4,4),"e5":(3,4),"e6":(2,4),"e7":(1,4),"e8":(0,4),
            "f1":(7,5),"f2":(6,5),"f3":(5,5),"f4":(4,5),"f5":(3,5),"f6":(2,5),"f7":(1,5),"f8":(0,5),
            "g1":(7,6),"g2":(6,6),"g3":(5,6),"g4":(4,6),"g5":(3,6),"g6":(2,6),"g7":(1,6),"g8":(0,6),
            "h1":(7,7),"h2":(6,7),"h3":(5,7),"h4":(4,7),"h5":(3,7),"h6":(2,7),"h7":(1,7),"h8":(0,7),
        }

    def __init__(self):
        pass

    def create_board(self):     
        for i in Board.li:
            print(i)
        label = ["a","b","c","d","e","f","g","h"]
        print(label)
        logging.debug("starting position board printed")

    def update_board(self,piece,prev_loc,now_loc,):
        self.piece = piece
        self.prev_loc = prev_loc
        self.now_loc = now_loc
        if ((turn-1) % 2) != 0:
            turn_colour = "White"
        else:
            turn_colour = "Black"
        
        query = """update board set Location = '%s' where Piece = '%s' and Colour = '%s';"""
        tupl = (self.now_loc,self.piece,turn_colour)
        # print(tupl)
        mycursor.execute(query % tupl)
        db.commit()

#code to modify sql database to update board positions

        B = Board()
        B.show_updated_board()
        
    def show_updated_board(self):
        self.li = Board.li
        mycursor.execute("select * from board;")
        result = mycursor.fetchall()
        for i in result:
            piece_loc = i[0]  
            piece_name = i[1]  
            piece_colour = i[2] 
            self.dict = Board.li_ref_dict
            self.input_move = piece_loc
            for c_move, co_or in self.dict.items():
                if str(c_move) == str(self.input_move):
                    print(f"Key = {c_move} Value = {co_or}")
                    tupl = co_or
                    if piece_colour == "White":
                        if piece_name == "Queen":
                            Board.li[tupl[0]][tupl[1]] = Pieces.w_queen


        for i in Board.li:
            print(i)
        print(Board.label )
# create a method to query through table board and reconstruct a board as a list


    def check_game_over(self):
        w_king_status = False
        b_king_status = False
        b_win_msg = """
         ____  _            _     __        ___             _ 
        | __ )| | __ _  ___| | __ \ \      / (_)_ __  ___  | |
        |  _ \| |/ _` |/ __| |/ /  \ \ /\ / /| | '_ \/ __| | |
        | |_) | | (_| | (__|   <    \ V  V / | | | | \__ \ |_|
        |____/|_|\__,_|\___|_|\_\    \_/\_/  |_|_| |_|___/ (_)

        """
        w_win_msg = """
        __        ___     _ _        __        ___             _ 
        \ \      / / |__ (_) |_ ___  \ \      / (_)_ __  ___  | |
         \ \ /\ / /| '_ \| | __/ _ \  \ \ /\ / /| | '_ \/ __| | |
          \ V  V / | | | | | ||  __/   \ V  V / | | | | \__ \ |_|
           \_/\_/  |_| |_|_|\__\___|    \_/\_/  |_|_| |_|___/ (_)

        """
        self.li = Board.li
        for i in self.li:
            if Pieces.w_king in i:
                print(f"White King has been found at {i}")
                w_king_status = True
            elif Pieces.b_king in i:
                print(f"Black King has been found at {i}")    
                b_king_status = True
            else:    
                pass
        if w_king_status != True:
            print("White King has been captured")
            print(b_win_msg)
        elif b_king_status != True:
            print("Black King has been captured")        
            print(w_win_msg)

    def get_move_co(self,input_move,piece):
        self.dict = Board.li_ref_dict
        self.piece = piece
        self.input_move = input_move
        for c_move, co_or in self.dict.items():
            if str(c_move) == str(input_move):
                print(f"Key = {c_move} Value = {co_or}")
                tupl = co_or
        print(Board.li[tupl[0]][tupl[1]])

class Movement():
        hor = ["a","b","c","d","e","f","g","h"]
        ver = [1,2,3,4,5,6,7,8]
        loc_dict = {
            "a1":(7,0),"a2":(6,0),"a3":(5,0),"a4":(4,0),"a5":(3,0),"a6":(2,0),"a7":(1,0),"a8":(0,0),
            "b1":(7,1),"b2":(6,1),"b3":(5,1),"b4":(4,1),"b5":(3,1),"b6":(2,1),"b7":(1,1),"b8":(0,1),
            "c1":(7,2),"c2":(6,2),"c3":(5,2),"c4":(4,2),"c5":(3,2),"c6":(2,2),"c7":(1,2),"c8":(0,2),
            "d1":(7,3),"d2":(6,3),"d3":(5,3),"d4":(4,3),"d5":(3,3),"d6":(2,3),"d7":(1,3),"d8":(0,3),
            "e1":(7,4),"e2":(6,4),"e3":(5,4),"e4":(4,4),"e5":(3,4),"e6":(2,4),"e7":(1,4),"e8":(0,4),
            "f1":(7,5),"f2":(6,5),"f3":(5,5),"f4":(4,5),"f5":(3,5),"f6":(2,5),"f7":(1,5),"f8":(0,5),
            "g1":(7,6),"g2":(6,6),"g3":(5,6),"g4":(4,6),"g5":(3,6),"g6":(2,6),"g7":(1,6),"g8":(0,6),
            "h1":(7,7),"h2":(6,7),"h3":(5,7),"h4":(4,7),"h5":(3,7),"h6":(2,7),"h7":(1,7),"h8":(0,7),   
        }

        def __init__(self) -> None:
            pass

        def get_current_loc(self,piece,pos,turn):
            self.piece = piece
            self.pos = pos
            self.turn = turn
            query = "select Loc from pieces where Name = '%s';"
            mycursor.execute(query % self.piece)
            result = mycursor.fetchall()
            for i in result:
                for j in i:
                    print(j)
            # print("at get current loc!")
            self.current_loc = j
            Movement.trace_route(self,self.current_loc,self.piece,self.pos,self.turn)

        def trace_route(self,current_loc,piece,future_loc,turn):
            long = [1,2,3,4,5,6,7,8]
            diag = []
            count = int(self.current_loc[1])
            print("tracing route")
            self.current_loc = current_loc
            self.turn = turn
            self.future_loc = future_loc
            self.piece = piece
            print(f"moving {self.piece} from {self.current_loc} to {self.future_loc}")
            #to check if the move is longitudnal and not diagonal
            if str(self.future_loc[0]) == str(self.current_loc[0]):
                print("the move is longitudnal")
                if self.current_loc[1] > self.future_loc[1]:
                    pass
                #insert code here
                elif self.current_loc[1] < self.future_loc[1]:
                    while True:
                        loc_num_check = int(self.current_loc[1]) + count
                        loc_square_check = str(self.current_loc[0]) + str(loc_num_check)
                        print(loc_square_check)
                        query = ("select Piece from board where Location = '%s';")
                        mycursor.execute(query % loc_square_check)
                        # print("1.",loc_square_check)
                        result = mycursor.fetchall()
                        if result != []:
                            print("obstacle encountered")
                            I = Interaction()
                            I.capture(self.current_loc,loc_square_check,self.piece,self.turn)
                            # print(result)
                            break
                        else:
                            # print("free square")
                            count+=1
                            if str(loc_square_check) == str(self.future_loc):
                                break
                # print("path clear")

        def check_queen_move(self,move,turn):
            self.move = move
            self.turn = turn
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    #insert check for occupied squares
                    #insert obstacle check
                    print("legal queen move")
                    self.move = self.move[1] + self.move[2]
                    Movement.get_current_loc(self,"Queen",self.move,self.turn)

        def check_king_move(self,position,count):
            self.position = position
            if self.position[1] in self.hor:
                if int(self.position[2]) in self.ver:
                    print("legal king move")
                    
        def check_bishop_move(self,position,count):
            self.position = position
            self.count = count
            print(self.position,self.count)

class Interaction(Movement):
    def __init__(self) -> None:
        pass

    def capture(self,prev_location,location_captured,piece_capturer,turn):
        self.prev_location = prev_location
        self.location_captured = location_captured
        self.piece_capturer = piece_capturer
        self.turn = turn
        # print(Movement.loc_dict)
        print(f"{self.piece_capturer} captures a piece at {self.location_captured}")
        # print(self.location_captured)
        query = "delete from board where Location = '%s';"
        mycursor.execute(query % str(self.location_captured))
        db.commit()
        # print(f"new turn = {self.turn}")
        B = Board()
        B.update_board((self.piece_capturer),(self.prev_location),(self.location_captured))


def main():
    b = Board()
    b.create_board()
    m = Movement()
    move = "Qd7"
    global turn
    turn = 1
    print(f"turn = {turn}")
    turn += 1
    global which
    which = "" #current position for the piece to be moved
    if move[0] == "K":
        m.check_king_move(move,turn)

    elif move[0] == "Q":
        m.check_queen_move(move,turn)

    elif move[0] == "B":
        m.check_bishop_move(move,turn)

    elif move[0] == "N":
        which = input("enter current position of the rook to be moved : ")
        m.check_knight_move(move,turn,which)

    elif move[0] == "p":
        m.check_pawn_move(move)

    elif move[0] == "R":
        which = input("enter current position of the rook to be moved : ")
        m.check_rook_move(move,turn,which)      

logging.info("main()")
main()