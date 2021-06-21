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

    li= [[Pieces.b_rooke,Pieces.b_knight,Pieces.b_bishop,Pieces.b_queen,'Pieces.b_king',Pieces.b_bishop,Pieces.b_knight,Pieces.b_rooke,"8"],
             [Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,Pieces.b_pawn,"7"],
             [" "," "," "," "," "," "," "," ","6"],
             [" "," "," "," "," "," "," "," ","5"],   
             [" "," "," "," "," "," "," "," ","4"],
             [" "," "," "," "," "," "," "," ","3"],
             [Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,Pieces.w_pawn,"2"],
             [Pieces.w_rooke,Pieces.w_knight,Pieces.w_bishop,Pieces.w_queen,Pieces.w_king,Pieces.w_bishop,Pieces.w_knight,Pieces.w_rooke,"1"],
        ]

    li_ref = [
            [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)],
            [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)],
            [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5)],
            [(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4)],
            [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3)],
            [(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2)],
            [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)],
            [(0,0),(0,1),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)],
        ]

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
        B = Board()
        B.show_updated_board()
        
    def show_updated_board(self):
        self.li = Board.li
        loc_dict_local = Movement.loc_dict
        mycursor.execute("select * from board;")
        result = mycursor.fetchall()
        # create a method to query through table board and reconstruct a board as a list
        B = Board()
        B.check_game_over()

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

class Movement():
        hor = ["a","b","c","d","e","f","g","h"]
        ver = [1,2,3,4,5,6,7,8]
        loc_dict = {
            "a1":(0,0),"a2":(0,1),"a3":(0,2),"a4":(0,3),"a5":(0,4),"a6":(0,5),"a7":(0,6),"a8":(0,7),
            "b1":(1,0),"b2":(1,1),"b3":(1,2),"b4":(1,3),"b5":(1,4),"b6":(1,5),"b7":(1,6),"b8":(1,7),
            "c1":(0,0),"c2":(2,1),"c3":(2,2),"c4":(2,3),"c5":(2,4),"c6":(2,5),"c7":(2,6),"c8":(2,7),
            "d1":(0,0),"d2":(3,1),"d3":(3,2),"d4":(3,3),"d5":(3,4),"d6":(3,5),"d7":(3,6),"d8":(3,7),
            "e1":(0,0),"e2":(4,1),"e3":(4,2),"e4":(4,3),"e5":(4,4),"e6":(4,5),"e7":(4,6),"e8":(4,7),
            "f1":(0,0),"f2":(5,1),"f3":(5,2),"f4":(5,3),"f5":(5,4),"f6":(5,5),"f7":(5,6),"f8":(5,7),
            "g1":(0,0),"g2":(6,1),"g3":(6,2),"g4":(6,3),"g5":(6,4),"g6":(6,5),"g7":(6,6),"g8":(6,7),
            "h1":(0,0),"h2":(7,1),"h3":(7,2),"h4":(7,3),"h5":(7,4),"h6":(7,5),"h7":(7,6),"h8":(7,7),
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
            print("at get current loc!")
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
        print(self.location_captured)
        query = "delete from board where Location = '%s';"
        mycursor.execute(query % str(self.location_captured))
        db.commit()
        print(f"new turn = {self.turn}")
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

