# Import statements
import time
import mysql.connector
import json
import os

# Global variables
global turn
turn = 1

global revertStatus
revertStatus = False

global w_inCheck
w_inCheck = False

global b_inCheck
b_inCheck = False

global turn_stck
turn_stck = [] #human inputted stack of instructions : like pc3 as compared to c3 in move_stck
 
global move_stck
move_stck = []

global which_stck
which_stck = []

global restore_stck
restore_stck = []

# deleting the JSON file from a previous session
if os.path.exists("revertQuery.json"):
  os.remove("revertQuery.json")

# Opening manual.txt with a context manager
with open("sql.txt","r") as fobj:
    content = fobj.readlines()
    x = content[0].strip()
    y = content[1].strip()
    z = content[2].strip()

# Connecting to the local mySQL server
db = mysql.connector.connect(
    host = z,
    user = x,
    passwd = y,
    database = "chess"
)
mycursor = db.cursor()

#deleting the old table and creating a new one 
mycursor.execute("drop table board")
mycursor.execute("create table board (Location char(5), Piece varchar(15), Colour char(5), Which char(5));")
mycursor.execute("drop table revertBoard")
mycursor.execute("create table revertBoard (Location char(5), Piece varchar(15), Colour char(5), Which char(5));")
#white pieces data entry

mycursor.execute("insert into board values ('d1','Queen','White',NULL);")
mycursor.execute("insert into board values ('e1','King','White',NULL);")
mycursor.execute("insert into board values ('f1','Bishop','White','f1');")
mycursor.execute("insert into board values ('c1','Bishop','White','c1');")
mycursor.execute("insert into board values ('g1','Knight','White','g1');")
mycursor.execute("insert into board values ('b1','Knight','White','b1');")
mycursor.execute("insert into board values ('h1','Rook','White','h1');")
mycursor.execute("insert into board values ('a1','Rook','White','a1');")
mycursor.execute("insert into board values ('a2','Pawn','White','a2');")
mycursor.execute("insert into board values ('b2','Pawn','White','b2');")
mycursor.execute("insert into board values ('c2','Pawn','White','c2');")
mycursor.execute("insert into board values ('d2','Pawn','White','d2');")
mycursor.execute("insert into board values ('e2','Pawn','White','e2');")
mycursor.execute("insert into board values ('f2','Pawn','White','f2');")
mycursor.execute("insert into board values ('g2','Pawn','White','g2');")
mycursor.execute("insert into board values ('h2','Pawn','White','h2');")
db.commit()

mycursor.execute("insert into revertBoard values ('d1','Queen','White',NULL);")
mycursor.execute("insert into revertBoard values ('e1','King','White',NULL);")
mycursor.execute("insert into revertBoard values ('f1','Bishop','White','f1');")
mycursor.execute("insert into revertBoard values ('c1','Bishop','White','c1');")
mycursor.execute("insert into revertBoard values ('g1','Knight','White','g1');")
mycursor.execute("insert into revertBoard values ('b1','Knight','White','b1');")
mycursor.execute("insert into revertBoard values ('h1','Rook','White','h1');")
mycursor.execute("insert into revertBoard values ('a1','Rook','White','a1');")
mycursor.execute("insert into revertBoard values ('a2','Pawn','White','a2');")
mycursor.execute("insert into revertBoard values ('b2','Pawn','White','b2');")
mycursor.execute("insert into revertBoard values ('c2','Pawn','White','c2');")
mycursor.execute("insert into revertBoard values ('d2','Pawn','White','d2');")
mycursor.execute("insert into revertBoard values ('e2','Pawn','White','e2');")
mycursor.execute("insert into revertBoard values ('f2','Pawn','White','f2');")
mycursor.execute("insert into revertBoard values ('g2','Pawn','White','g2');")
mycursor.execute("insert into revertBoard values ('h2','Pawn','White','h2');")
db.commit()
#black pieces data entry

mycursor.execute("insert into board values ('d8','Queen','Black',NULL);")
mycursor.execute("insert into board values ('e8','King','Black',NULL);")
mycursor.execute("insert into board values ('f8','Bishop','Black','f8');")
mycursor.execute("insert into board values ('c8','Bishop','Black','c8');")
mycursor.execute("insert into board values ('g8','Knight','Black','g8');")
mycursor.execute("insert into board values ('b8','Knight','Black','b8');")
mycursor.execute("insert into board values ('h8','Rook','Black','h8');")
mycursor.execute("insert into board values ('a8','Rook','Black','a8');")
mycursor.execute("insert into board values ('a7','Pawn','Black','a7');")
mycursor.execute("insert into board values ('b7','Pawn','Black','b7');")
mycursor.execute("insert into board values ('c7','Pawn','Black','c7');")
mycursor.execute("insert into board values ('d7','Pawn','Black','d7');")
mycursor.execute("insert into board values ('e7','Pawn','Black','e7');")
mycursor.execute("insert into board values ('f7','Pawn','Black','f7');")
mycursor.execute("insert into board values ('g7','Pawn','Black','g7');")
mycursor.execute("insert into board values ('h7','Pawn','Black','h7');")
db.commit()

mycursor.execute("insert into revertBoard values ('d8','Queen','Black',NULL);")
mycursor.execute("insert into revertBoard values ('e8','King','Black',NULL);")
mycursor.execute("insert into revertBoard values ('f8','Bishop','Black','f8');")
mycursor.execute("insert into revertBoard values ('c8','Bishop','Black','c8');")
mycursor.execute("insert into revertBoard values ('g8','Knight','Black','g8');")
mycursor.execute("insert into revertBoard values ('b8','Knight','Black','b8');")
mycursor.execute("insert into revertBoard values ('h8','Rook','Black','h8');")
mycursor.execute("insert into revertBoard values ('a8','Rook','Black','a8');")
mycursor.execute("insert into revertBoard values ('a7','Pawn','Black','a7');")
mycursor.execute("insert into revertBoard values ('b7','Pawn','Black','b7');")
mycursor.execute("insert into revertBoard values ('c7','Pawn','Black','c7');")
mycursor.execute("insert into revertBoard values ('d7','Pawn','Black','d7');")
mycursor.execute("insert into revertBoard values ('e7','Pawn','Black','e7');")
mycursor.execute("insert into revertBoard values ('f7','Pawn','Black','f7');")
mycursor.execute("insert into revertBoard values ('g7','Pawn','Black','g7');")
mycursor.execute("insert into revertBoard values ('h7','Pawn','Black','h7');")
db.commit()

#dropping and creating table castle

mycursor.execute("drop table castle;")
mycursor.execute("create table castle (Location char(5), Piece varchar(15), Colour char(5), Moved char(1));")

#data entry for table castle

mycursor.execute("insert into castle values ('a1','Rook','White','n');")
mycursor.execute("insert into castle values ('h1','Rook','White','n');")
mycursor.execute("insert into castle values ('a8','Rook','Black','n');")
mycursor.execute("insert into castle values ('h8','Rook','Black','n');")
mycursor.execute("insert into castle values ('e1','King','White','n');")
mycursor.execute("insert into castle values ('e8','King','Black','n');")
db.commit()

#Class definition


#Class Pieces contains the icon of the pieces
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


#Class Board contains the function definitions relating to Board attributes
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

    label = ["a","b","c","d","e","f","g","h"," "]
    pipe = "|"

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

    #method for dealing with ghosting of pieces after they are moved
    @classmethod
    def cleanup(self):
        try:
            move = move_stck[-1]
            for move in Board.li_ref_dict:
                coordinates = Board.li_ref_dict[move]
                Board.li[coordinates[0]][coordinates[1]] = " "
        except IndexError:
            pass

    #method for updating revertBoard table after one turn so revert => undo move 
    @classmethod
    def revert_update_board_dump(self,*args,isWhich = False):
        li0 = [] # fmt => query, setLocation, lookupLocation
        li1 = [] # fmt => query, setLocation, Piece, Colour

        sqlObj0 = {"query" : "", "setLocation" : "", "whichLocation" : ""}
        sqlObj1 = {"query" : "", "setLocation" : "", "Piece" : "", "Colour" : ""}
        
        if isWhich:
            for i in args:
                li0.append(i)
            
            sqlObj0["query"] = li0[0]
            sqlObj0["setLocation"] = li0[1]
            sqlObj0["whichLocation"] = li0[2]

            with open("revertQuery.json","w") as fobj:
                json.dump(sqlObj0,fobj)
        else:
            for j in args:
                li1.append(j)

            sqlObj1["query"] = li1[0]
            sqlObj1["setLocation"] = li1[1]
            sqlObj1["Piece"] = li1[2]
            sqlObj1["Colour"] = li1[3]

            with open("revertQuery.json","w") as fobj:
                json.dump(sqlObj1,fobj)

    @classmethod
    def revert_update_board_load(self): 
 
        """I think the revert error is being caused by the load function being
           called too early and/or inappropriately => early SQL table updation 
           => faulty revert."""

        li = []

        with open("revertQuery.json","r") as fobj:
            content = json.load(fobj)
            for k in content:
                li.append(content[k])
        
        if li != []:
            
            if len(li) == 3:
                # it is a which query
                query = li[0]
                setLocation = li[1]
                lookupLocation = li[2]
                mycursor.execute(query % (setLocation, lookupLocation))
                db.commit()

            elif len(li) == 4:
                # it is NOT a which query
                query = li[0]
                setLocation = li[1]
                piece = li[2]
                colour = li[3]
                mycursor.execute(query % (setLocation, piece, colour))
                db.commit()
            
            else:
                raise Exception ("Unexpected List Length Encountered")
        
        else: 
            raise Exception ("Empty List Encountered")

    #method for creating the board
    def create_board(self):     
        # Board.cleanup()
        for i in Board.li:
            print()
            for j in i:
                print(" ",j," ",Board.pipe,end=" ")
            print()
        print()
        for a in Board.label:
            print(" ",a," ",Board.pipe,end=" ")
        label = ["a","b","c","d","e","f","g","h"," "]
        pipe = "|"
        
    #method for updating the board and moving the pieces
    def update_board(self,piece,prev_loc,now_loc,):
        self.piece = piece
        self.prev_loc = prev_loc
        self.now_loc = now_loc
        which_pieces = ["Rook","Knight","Pawn","Bishop"]
        if ((turn-1) % 2) != 0:
            turn_colour = "White"
        else:
            turn_colour = "Black"
        if self.piece in which_pieces:
            query = "update board set Location = '%s' where Location = '%s';"
            mycursor.execute(query % (self.now_loc,which))
            db.commit()
            queryR = "update revertBoard set Location = '%s' where Location = '%s';"
            Board.revert_update_board_dump(queryR,self.now_loc,which,isWhich = True)
            # mycursor.execute(query % (self.now_loc,which))
            # db.commit()
        elif self.piece not in which_pieces:
            query = """update board set Location = '%s' where Piece = '%s' and Colour = '%s';"""
            tupl = (self.now_loc,self.piece,turn_colour)
            mycursor.execute(query % tupl)
            db.commit()
            queryR = """update revertBoard set Location = '%s' where Piece = '%s' and Colour = '%s';"""
            Board.revert_update_board_dump(queryR, self.now_loc, self.piece, turn_colour, isWhich = False)
            # mycursor.execute(query % tupl)
            # db.commit()

        else:
            raise Exception ("Unknown_Piece_Encountered")

        #iterates through the dict to find the location of the last move
        for c_move, co_or in Board.li_ref_dict.items():
            if str(c_move) == str(self.prev_loc):
                cleanup = Board.li
                int0 = int(co_or[0])
                int1 = int(co_or[1])
                cleanup[int0].pop(int1)
                cleanup[int0].insert(int1," ")

        Interaction.promote(self)
        Board.cleanup()

        B = Board()
        B.show_updated_board()
        
    #iterates through the nested array to replace it with icons
    def show_updated_board(self):
        revertStatus = False
        Board.cleanup() # added to remove ghosting while calling the revert function
        self.li = Board.li
        
        if not revertStatus:
            mycursor.execute("select * from board;")
        else: 
            mycursor.execute("select * from revertBoard;")
        
        result = mycursor.fetchall()
        for i in result:
            piece_loc = i[0]  
            piece_name = i[1]  
            piece_colour = i[2] 
            self.dict = Board.li_ref_dict
            self.input_move = piece_loc
            for c_move, co_or in self.dict.items():
                if str(c_move) == str(self.input_move):
                    tupl = co_or
                    if piece_colour == "White":
                        if piece_name == "Queen":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.w_queen
                        elif piece_name == "King":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.w_king
                        elif piece_name == "Bishop":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.w_bishop
                        elif piece_name == "Rook":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.w_rooke
                        elif piece_name == "Knight":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.w_knight
                        elif piece_name == "Pawn":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.w_pawn
                    elif piece_colour == "Black":
                        if piece_name == "Queen":
                            # print("yes!")
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.b_queen
                        elif piece_name == "King":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.b_king
                        elif piece_name == "Bishop":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.b_bishop
                        elif piece_name == "Rook":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.b_rooke
                        elif piece_name == "Knight":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.b_knight
                        elif piece_name == "Pawn":
                            Board.li_ref_empty[tupl[0]][tupl[1]] = Pieces.b_pawn
                    else:
                        raise Exception ("Unexpected_Colour_Encountered")

        Board.li = Board.li_ref_empty      

        B = Board()  
        B.check_game_over()

    # checks if the game is drawn or a king has been captured
    def check_game_over(self):
        draw = False
        w_king_status = False
        b_king_status = False
        draw_msg = """
             _                    
          __| |_ __ __ ___      __
         / _` | '__/ _` \ \ /\ / /
        | (_| | | | (_| |\ V  V / 
         \__,_|_|  \__,_| \_/\_/                        
        """
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
        query = "select count(*) from board;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            j = i
            
        if j[0] == 2:
            draw = True
            print(draw_msg)
            quit()
        
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

        var0 = [("Bishop",),("King",),("King",)]
        var1 = [("King",),("King",),("Knight",)]
        compare_li = []

        query = "select count(*) from board;"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            num = i
        num = str(num)
        num = num[1]
        if int(num) == 3:
            query = "select Piece from board;"
            mycursor.execute(query)
            result = mycursor.fetchall()
            for i in result:
                compare_li.append(i)
            compare_li.sort()
            if compare_li == var0 or compare_li == var1:
                draw = True
        
        if w_king_status != True:
            print("White King has been captured")
            print(b_win_msg)
            print(move_stck)
            quit()
        elif b_king_status != True:
            print("Black King has been captured")        
            print(w_win_msg)
            print(move_stck)
            print(turn_stck)
            quit()
        elif draw == True:
            print(draw_msg)
            quit()
                
        main()

    def get_move_co(self,input_move,piece):
        self.dict = Board.li_ref_dict
        self.piece = piece
        self.input_move = input_move
        for c_move, co_or in self.dict.items():
            if str(c_move) == str(input_move):
                print(f"Key = {c_move} Value = {co_or}")
                tupl = co_or
        print(Board.li[tupl[0]][tupl[1]])

    # I do not know why I added this query here TBH
    def restore_pawn_status(self):
        print("pawn cannot capture vertically")
        query = """update board set Location = '%s' where Piece = 'Pawn';"""
        B = Board()
        B.show_updated_board()

    # method for checking wheather the King is in check
    def incheck(self):
        global incheck_status
        incheck_status = False
        northsouth_pieces = ["Queen","Rook"]
        diagonal_pieces = ["Queen","Pawn","Bishop"]
        
        if ((turn -1) % 2) != 0:
            turn_colour = "White"
            mod_colour = "WHITE"
            use_colour = "Black"
            check_use_colour = "BLACK"
        else:
            turn_colour = "Black"
            mod_colour = "BLACK"
            use_colour = "White"
            check_use_colour = "WHITE"

        query = "select * from board where Piece = 'King' and Colour = '%s';"
        mycursor.execute(query % (use_colour))
        result = mycursor.fetchall()
        
        tupl = ""

        for i in result:
            tupl = i 

        current_loc = str(tupl[0])
        count = 1
        loopy_north = True
    
    # check north                           
        while loopy_north:
            current_loc_square_check = current_loc[0] + str(int(current_loc[1]) + count)
            query = ("select Piece, Colour from board where Location = '%s';")
            mycursor.execute(query % current_loc_square_check)
            result = mycursor.fetchall()
            if result!=[]:
                for i in result:
                    tupl = i
                    if tupl[1] == use_colour:
                        loopy_north = False
                        break
                    else:
                        if tupl[0] in northsouth_pieces:
                            incheck_status = True
                            loopy_north = False
                            break
                    if tupl[0] not in northsouth_pieces and tupl[1] != use_colour:
                        loopy_north = False
                        break


            else:
                if int(current_loc_square_check[1]) > 8:
                    loopy_north = False
                    break
                count += 1
    
    # check south
        count = 1
        loopy_south = True
        while loopy_south:
            current_loc_square_check = current_loc[0] + str((int(current_loc[1]) - count))
            query = ("select Piece, Colour from board where Location = '%s';")
            mycursor.execute(query % current_loc_square_check)
            result = mycursor.fetchall()
            if result!=[]:
                for i in result:
                    tupl = i
                    if tupl[1] == use_colour:
                        loopy_south = False
                        break
                    else:
                        if tupl[0] in northsouth_pieces:
                            incheck_status = True
                            loopy_south = False
                            break
                    if tupl[0] not in northsouth_pieces and tupl[1] != use_colour:
                        loopy_south = False
                        break

            else:
                if int(current_loc_square_check[1]) > 8:
                    loopy_south = False
                    break
                count -= 1
    
    # check east
        hor_li = ["a","b","c","d","e","f","g","h"]
        loopy_east = True
        lindex = hor_li.index(current_loc[0])
        while loopy_east:
            lindex += 1
            current_loc_square_check = str(hor_li[lindex]) + str(current_loc[1]) 
            query = ("select Piece, Colour from board where Location = '%s';")
            mycursor.execute(query % current_loc_square_check)
            result = mycursor.fetchall()
            if result != []:
                for i in result:
                    tupl = i
                    if tupl[1] == use_colour:
                        loopy_east = False
                        break
                    else:
                        if tupl[0] in northsouth_pieces:
                            incheck_status = True
                            loopy_east = False
                            break
                    if tupl[0] not in northsouth_pieces and tupl[1] != use_colour:
                        loopy_east = False
                        break

            else:
                if lindex > len(hor_li):
                    loopy_east = False
                    break

    # check west
        loopy_west = True
        lindex = hor_li.index(current_loc[0])
        while loopy_west:
            lindex -= 1
            current_loc_square_check = str(hor_li[lindex]) + str(current_loc[1]) 
            query = ("select Piece, Colour from board where Location = '%s';")
            mycursor.execute(query % current_loc_square_check)
            result = mycursor.fetchall()
            if result != []:
                for i in result:
                    tupl = i
                    if tupl[1] == use_colour:
                        loopy_west = False
                        break
                    else:
                        if tupl[0] in northsouth_pieces:
                            incheck_status = True
                            loopy_west = False
                            break
                    if tupl[0] not in northsouth_pieces and tupl[1] != use_colour:
                        loopy_west = False
                        break

            else:
                if lindex > len(hor_li):
                    loopy_west = False
                    break

    # check northeast
        for sqr, coor in Movement.loc_dict.items():
            if sqr == current_loc:
                tupl = coor
        num0 = tupl[0]
        num1 = tupl[1]
        loopy_ne = True
        while loopy_ne:
            num0 -= 1
            num1 += 1
            next_co_or = tuple([num0,num1])
            for i,j in Movement.loc_dict.items():
                if next_co_or == j:
                    check_loc_coor = i
                    query = """select Piece, Colour from board where Location = '%s';"""
                    mycursor.execute(query % check_loc_coor)
                    result = mycursor.fetchall()
                    if result != []:
                        for i in result:
                            tupl = i
                            if tupl[1] == use_colour:
                                loopy_ne = False
                                break
                            else:
                                if tupl[0] in diagonal_pieces:
                                    incheck_status = True
                                    loopy_ne = False
                                    break
                            if tupl[0] not in diagonal_pieces and tupl[1] != use_colour:
                                loopy_ne = False
                                break

                    else:
                        if num0 < 0 or num1 >7:
                            loopy_ne  = False
                            break
            break
    
    #check northwest
        for sqr, coor in Movement.loc_dict.items():
            if sqr == current_loc:
                tupl = coor
        num0 = tupl[0]
        num1 = tupl[1]
        loopy_nw = True
        while loopy_nw:
            num0 -= 1
            num1 -= 1
            next_co_or = tuple([num0,num1])
            for i,j in Movement.loc_dict.items():
                if next_co_or == j:
                    check_loc_coor = i
                    query = """select Piece, Colour from board where Location = '%s';"""
                    mycursor.execute(query % check_loc_coor)
                    result = mycursor.fetchall()
                    if result != []:
                        for i in result:
                            tupl = i
                            if tupl[1] == use_colour:
                                loopy_nw = False
                                break
                            else:
                                if tupl[0] in diagonal_pieces:
                                    incheck_status = True
                                    loopy_nw = False
                                    break
                            if tupl[0] not in diagonal_pieces and tupl[1] != use_colour:
                                loopy_nw = False
                                break

                    else:
                        if num0 < 0 or num1 < 0:
                            loopy_nw  = False
                            break
            break
    
    #check southwest
        for sqr, coor in Movement.loc_dict.items():
            if sqr == current_loc:
                tupl = coor
        num0 = tupl[0]
        num1 = tupl[1]
        loopy_sw = True
        while loopy_sw:
            num0 += 1
            num1 -= 1
            next_co_or = tuple([num0,num1])
            for i,j in Movement.loc_dict.items():
                if next_co_or == j:
                    check_loc_coor = i
                    query = """select Piece, Colour from board where Location = '%s';"""
                    mycursor.execute(query % check_loc_coor)
                    result = mycursor.fetchall()
                    if result != []:
                        for i in result:
                            tupl = i
                            if tupl[1] == use_colour:
                                loopy_sw = False
                                break
                            else:
                                if tupl[0] in diagonal_pieces:
                                    incheck_status = True
                                    loopy_sw = False
                                    break
                            if tupl[0] not in diagonal_pieces and tupl[1] != use_colour:
                                loopy_sw = False
                                break

                    else:
                        if num0 > 7 or num1 < 0:
                            loopy_sw  = False
                            break
            break
  
    #check southeast
        for sqr, coor in Movement.loc_dict.items():
            if sqr == current_loc:
                tupl = coor
        num0 = tupl[0]
        num1 = tupl[1]
        loopy_se = True
        while loopy_se:
            num0 += 1
            num1 += 1
            next_co_or = tuple([num0,num1])
            for i,j in Movement.loc_dict.items():
                if next_co_or == j:
                    check_loc_coor = i
                    query = """select Piece, Colour from board where Location = '%s';"""
                    mycursor.execute(query % check_loc_coor)
                    result = mycursor.fetchall()
                    if result != []:
                        for i in result:
                            tupl = i
                            if tupl[1] == use_colour:
                                loopy_se = False
                                break
                            else:
                                if tupl[0] in diagonal_pieces:
                                    incheck_status = True
                                    loopy_se = False
                                    break
                            if tupl[0] not in diagonal_pieces and tupl[1] != use_colour:
                                loopy_se = False
                                break

                    else:
                        if num0 > 7 or num1 > 7:
                            loopy_se  = False
                            break
            break

    #check from knights
        kX = [1,-1,1,-1,2,2,-2,-2]
        kY = [2,2,-2,-2,1,-1,1,-1]
        knightLegalmoves = []
        query = "select Location from board where Piece = 'King' and Colour = '%s';"
        mycursor.execute(query % use_colour)
        result = mycursor.fetchall()
        current_loc = str(result[0])
        current_loc = str(current_loc[2] + current_loc[3])

        for sqr, coor in Movement.loc_dict.items():
            if sqr == current_loc:
                co_or = coor

        permaCoord = co_or
        lindex = 0
        legitX = True
        legitY = True
        while True:
            if lindex > 7:
                break
            else:
                co_or_x = permaCoord[0]
                co_or_y = permaCoord[1]
                co_or_x += kX[lindex]
                co_or_y += kY[lindex]
            
                if co_or_x > 7 or co_or_x < 0:
                    legitX = False
                elif co_or_y > 7 or co_or_y < 0:
                    legitY = False
                else: 
                    legitX = True
                    legitY = True
                    
                if legitX == True and legitY == True:
                    co_orKnight = tuple([co_or_x,co_or_y])
                    for a,b in Movement.loc_dict.items():
                        if b == co_orKnight:
                            knightLegalmoves.append(a)
            lindex += 1

        for i in knightLegalmoves:
            query = "select Piece, Colour from board where Location = '%s';"
            mycursor.execute(query % i)
            result = mycursor.fetchall()
            if result != []:
                if result[0][1] == use_colour:
                    pass
                elif result[0][0] == "Knight" and result[0][1] != use_colour:
                    incheck_status = True
            else:
                pass


        # incheck() status declaration
        if incheck_status:
            print(f"[{check_use_colour}]'s king is in check")
            if use_colour == "White":
                global w_inCheck
                w_inCheck = True
            elif use_colour == "Black":
                global b_inCheck
                b_inCheck = True   
        
    # method for handling draws from the users 
    def draw_game(self,turn):
        self.turn = turn
        if ((self.turn-1) % 2) != 0:
            turn_colour = "White"
            turnColourPrint = "WHITE"
        else:
            turn_colour = "Black"
            turnColourPrint = "BLACK"

        print(f"[{turnColourPrint}] offers a draw")
        draw_in = input("do you accept? y/n ")
        if draw_in.lower() == "y":
            draw_msg = """
             _                    
          __| |_ __ __ ___      __
         / _` | '__/ _` \ \ /\ / /
        | (_| | | | (_| |\ V  V / 
         \__,_|_|  \__,_| \_/\_/                        
        """
            print(draw_msg)
            print(move_stck)
            print(turn_stck)
            quit()
        else:
            # revert() ?
            main()    
    
    #method for handling for forfeiture
    def forfeit(self,turn):
        self.turn = turn
        if ((self.turn-1) % 2) != 0:
            turn_colour = "White"
            turnColourPrint = "WHITE"
        else:
            turn_colour = "Black"
            turnColourPrint = "BLACK"
        print(f"[{turnColourPrint}] forfeits")
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
        if turn_colour == "White":
            print(b_win_msg)
        elif turn_colour == "Black":
            print(w_win_msg)
        
        # print(move_stck)
        print(turn_stck)
        quit()

    # method to revert board status to previous move
    def revert_board_status(self):
        revertStatus = True
        if ((turn-1) % 2) != 0:
            turn_colour = "White"
            revertTurn = 1 
        else:
            turn_colour = "Black"
            revertTurn = 2
            
        query0 = "drop table board;"
        mycursor.execute(query0)
        db.commit()
        mycursor.execute("create table board (Location char(5), Piece varchar(15), Colour char(5), Which char(5));")
        db.commit()
        query1 = ("INSERT INTO board (SELECT * FROM revertBoard);")
        mycursor.execute(query1)
        db.commit()
        B = Board()
        B.show_updated_board()
        # main()

# class for dealing with movement related attributes
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

        # method for getting the current lcoation of non-which pieces
        def get_current_loc(self,piece,pos,turn):
            self.piece = piece
            self.pos = pos
            self.turn = turn
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            which_pieces = ["Rook","Bishop","Pawn"]
            if self.piece not in which_pieces:
                query = "select Location from board where Piece = '%s' and Colour = '%s';"
                mycursor.execute(query % (self.piece,turn_colour))
                result = mycursor.fetchall()
                for i in result:
                    for j in i:
                        print(j)
                # print("at get current loc!")
                self.current_loc = j
                Movement.trace_route(self,self.current_loc,self.piece,self.pos,self.turn)
            else:
                print(f"which {which}")
                Movement.trace_route(self,which,self.piece,self.pos,self.turn)

        # method to check each square and if it is occupied to avoid jumping of pieces over obstacles
        def trace_route(self,current_loc,piece,future_loc,turn):
            long = [1,2,3,4,5,6,7,8]
            diag = []
            count = 1
            print("tracing route")
            self.current_loc = current_loc
            self.turn = turn
            self.future_loc = future_loc
            self.piece = piece
            print(f"moving {self.piece} from {self.current_loc} to {self.future_loc}")
            
            #to check if the move is longitudnal and not diagonal
            if str(self.future_loc[0]) == str(self.current_loc[0]):
                print("the move is vertical")
                if self.current_loc[1] > self.future_loc[1]:
                    while True:
                        loc_num_check = int(self.current_loc[1]) - count
                        loc_square_check = str(self.current_loc[0]) + str(loc_num_check)
                        print(loc_square_check)
                        query = ("select Piece from board where Location = '%s';")
                        mycursor.execute(query % loc_square_check)
                        result = mycursor.fetchall()
                        if result != []:
                            print("obstacle encountered")
                            I = Interaction()
                            I.capture(self.current_loc,loc_square_check,self.piece,self.turn)
                            break
                        else:
                            count+=1
                            if str(loc_square_check) == str(self.future_loc):
                                print(f"reached at {self.future_loc}")
                                B = Board()
                                B.update_board(self.piece,self.current_loc,self.future_loc)
                                break
                            
                elif self.current_loc[1] < self.future_loc[1]:
                    while True:
                        loc_num_check = int(self.current_loc[1]) + count
                        loc_square_check = str(self.current_loc[0]) + str(loc_num_check)
                        print(loc_square_check)
                        query = ("select Piece from board where Location = '%s';")
                        mycursor.execute(query % loc_square_check)
                        result = mycursor.fetchall()
                        if result != []:
                            if self.piece == "Pawn":
                                B = Board()
                                B.restore_pawn_status()
                            else:
                                print("obstacle encountered")
                                I = Interaction()
                                I.capture(self.current_loc,loc_square_check,self.piece,self.turn)
                                break
                        else:
                            count+=1
                            if str(loc_square_check) == str(self.future_loc):
                                print(f"reached at {self.future_loc}")
                                B = Board()
                                B.update_board(self.piece,self.current_loc,self.future_loc)
                                break
            
            #horizontal moves
            elif (self.future_loc[1]) == (self.current_loc[1]):
                print("the move is horizontal")
                hor_li = ["a","b","c","d","e","f","g","h"]
                while True:
                    if self.current_loc[0] < self.future_loc[0]:
                        # eastwards move
                        lindex = hor_li.index(str(self.current_loc[0]))
                        while True:
                            lindex += 1
                            check_loc_coor = str(hor_li[lindex]) + str(self.current_loc[1])
                            query = """select * from board where Location = '%s';"""
                            mycursor.execute(query % check_loc_coor)
                            result = mycursor.fetchall()
                            if result != []:
                                print("obstacle encountered")
                                I = Interaction()
                                I.capture(self.current_loc,check_loc_coor,self.piece,self.turn)
                                break
                            else:
                                if str(check_loc_coor) == str(self.future_loc):
                                    print(f"reached at {self.future_loc}")
                                    B = Board()
                                    B.update_board(self.piece,check_loc_coor,self.future_loc)
                                    break

                    elif self.current_loc[0] > self.future_loc[0]:
                        # westwards move
                        lindex = hor_li.index(str(self.current_loc[0]))
                        while True:
                            lindex -= 1
                            check_loc_coor = str(hor_li[lindex]) + str(self.current_loc[1])
                            query = """select * from board where Location = '%s';"""
                            mycursor.execute(query % check_loc_coor)
                            result = mycursor.fetchall()
                            if result != []:
                                print("obstacle encountered")
                                I = Interaction()
                                I.capture(self.current_loc,check_loc_coor,self.piece,self.turn)
                                break
                            else:
                                if str(check_loc_coor) == str(self.future_loc):
                                    print(f"reached at {self.future_loc}")
                                    B = Board()
                                    B.update_board(self.piece,check_loc_coor,self.future_loc)
                                    break
            
            # diagonal moves
            elif self.piece == "Queen" or self.piece == "Bishop" or self.piece == "King":
                move_direction = ""
                for i in Movement.loc_dict:
                    if i == self.current_loc:
                        co_or_num = Movement.loc_dict[i]
                        print(f"co-ordinate of {self.current_loc} is {co_or_num}")
                        num0 = int(co_or_num[0])
                        num1 = int(co_or_num[1])
                        if self.current_loc[1] < self.future_loc[1]:
                            move_direction = move_direction + "north"
                            if self.current_loc[0] < self.future_loc[0]:
                                move_direction = move_direction + "east"
                            else:
                                move_direction = move_direction + "west"
                        elif self.current_loc[1] > self.future_loc[1]:
                            move_direction = move_direction + "south"
                            if self.current_loc[0] < self.future_loc[0]:
                                move_direction = move_direction + "east"
                            else:
                                move_direction = move_direction + "west"
                        print(f" the direction of the move is {move_direction}")
                        if move_direction == "northeast":
                            while True:
                                num0 -= 1
                                num1 += 1
                                next_co_or = tuple([num0,num1])

                                for i,j in Movement.loc_dict.items():
                                    if next_co_or == j:
                                        
                                        check_loc_coor = i
                                        query = """select * from board where Location = '%s';"""
                                        mycursor.execute(query % check_loc_coor)
                                        result = mycursor.fetchall()
                                        if result != []:
                                            I = Interaction()
                                            I.capture(self.current_loc,check_loc_coor,self.piece,self.turn)
                                            break

                                        else:
                                            if str(check_loc_coor) == str(self.future_loc):
                                                # print(f"reached at {self.future_loc}")
                                                B = Board()
                                                B.update_board(self.piece,check_loc_coor,self.future_loc)
                                                break

                        elif move_direction == "northwest":
                            while True:
                                num0 -= 1
                                num1 -= 1
                                next_co_or = tuple([num0,num1])
                                # print(f"tupleISED {next_co_or}")
                                for i,j in Movement.loc_dict.items():
                                    if next_co_or == j:
                                        print("match found")
                                        print(i,j)
                                        check_loc_coor = i
                                        query = """select * from board where Location = '%s';"""
                                        mycursor.execute(query % check_loc_coor)
                                        result = mycursor.fetchall()
                                        if result != []:
                                            print("obstacle encountered")
                                            I = Interaction()
                                            I.capture(self.current_loc,check_loc_coor,self.piece,self.turn)
                                            break
                                        else:
                                            if str(check_loc_coor) == str(self.future_loc):
                                                print(f"reached at {self.future_loc}")
                                                B = Board()
                                                B.update_board(self.piece,check_loc_coor,self.future_loc)
                                                break    

                        elif move_direction == "southeast":
                            while True:
                                num0 += 1
                                num1 += 1
                                next_co_or = tuple([num0,num1])
                                print(f"tupleISED {next_co_or}")
                                for i,j in Movement.loc_dict.items():
                                    if next_co_or == j:
                                        
                                        check_loc_coor = i
                                        query = """select * from board where Location = '%s';"""
                                        mycursor.execute(query % check_loc_coor)
                                        result = mycursor.fetchall()
                                        if result != []:
                                            print("obstacle encountered")
                                            I = Interaction()
                                            I.capture(self.current_loc,check_loc_coor,self.piece,self.turn)
                                            break
                                        else:
                                            if str(check_loc_coor) == str(self.future_loc):
                                                print(f"reached at {self.future_loc}")
                                                B = Board()
                                                B.update_board(self.piece,check_loc_coor,self.future_loc)
                                                break 

                        elif move_direction == "southwest":
                            while True:
                                num0 += 1
                                num1 -= 1
                                next_co_or = tuple([num0,num1])
                                print(f"tupleISED {next_co_or}")
                                for i,j in Movement.loc_dict.items():
                                    if next_co_or == j:
                                        
                                        check_loc_coor = i
                                        query = """select * from board where Location = '%s';"""
                                        mycursor.execute(query % check_loc_coor)
                                        result = mycursor.fetchall()
                                        if result != []:
                                            print("obstacle encountered")
                                            I = Interaction()
                                            I.capture(self.current_loc,check_loc_coor,self.piece,self.turn)
                                            break
                                        else:
                                            if str(check_loc_coor) == str(self.future_loc):
                                                print(f"reached at {self.future_loc}")
                                                B = Board()
                                                B.update_board(self.piece,check_loc_coor,self.future_loc)
                                                break                                
            else:
                print("[ILLEGAL MOVE] possibly incorrect which")                                        

#Check function(s) for all piece moves

        # checking queen moves
        def check_queen_move(self,move,turn):
            self.move = move
            self.turn = turn
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            query = "select * from board where Piece = 'Queen' and Colour = '%s';"
            mycursor.execute(query % (turn_colour))
            result = mycursor.fetchall()
            for i in result:
                tupl = i
            move_manip = str(self.move[1]) + str(self.move[2])
            if str(tupl[0]) == str(move_manip):
                print("cannot move to the same location")
                quit()
            print(self.move, tupl[0])
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    #insert check for occupied squares
                    #insert obstacle check
                    print("legal queen move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    Movement.get_current_loc(self,"Queen",self.move,self.turn)

        #checking king moves
        def check_king_move(self,move,turn):
            self.move = move
            self.turn = turn
            hor_li = ["a","b","c","d","e","f","g","h"]
            ver_li = [1,2,3,4,5,6,7,8]
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            query = "select * from board where Piece = 'King' and Colour = '%s';"
            mycursor.execute(query % (turn_colour))
            result = mycursor.fetchall()
            for i in result:
                tupl = i
            move_manip = str(self.move[1]) + str(self.move[2])
            if str(tupl[0]) == str(move_manip):
                print("cannot move to the same location")

            if self.move[1] == "a":
                if tupl[0][1] == "b":
                    pass
            elif self.move[1] == "b":
                if tupl[0][1] == "a" or tupl[0][1] == "c":
                    pass
            elif self.move[1] == "c":
                if tupl[0][1] == "b" or tupl[0][1] == "d":
                    pass        
            elif self.move[1] == "d":
                if tupl[0][1] == "c" or tupl[0][1] == "e":
                    pass
            elif self.move[1] == "e":
                if tupl[0][1] == "d" or tupl[0][1] == "f":
                    pass
            elif self.move[1] == "f":
                if tupl[0][1] == "e" or tupl[0][1] == "g":
                    pass
            elif self.move[1] == "g":
                if tupl[0][1] == "f" or tupl[0][1] == "h":
                    pass
            elif self.move[1] == "h":
                if tupl[0][1] == "g":
                    pass
            else:
                print("King can only move one pace(s) horizontally")

            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    print("legal king move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    query = """update castle set Moved = 'y' where Piece = 'King' and Colour = '%s';"""
                    mycursor.execute(query % turn_colour)
                    db.commit()
                    Movement.get_current_loc(self,"King",self.move,self.turn)
                    
        # check rook move
        def check_rook_move(self,move,turn,which):
            self.move = move
            self.turn = turn
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            query = "select * from board where Piece = 'Rook' and Colour = '%s';"
            mycursor.execute(query % (turn_colour))
            result = mycursor.fetchall()
            for i in result:
                tupl = i
            move_manip = str(self.move[1]) + str(self.move[2])
            if str(tupl[0]) == str(move_manip):
                print("cannot move to the same location")
                B = Board()
                B.revert_board_status()
            print(self.move, tupl[0])
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    print("legal rook move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    query = """update castle set Moved = 'y' where Piece = 'Rook' and Colour = '%s';"""
                    mycursor.execute(query % turn_colour)
                    db.commit()
                    Movement.get_current_loc(self,"Rook",self.move,self.turn)

        # check bishop moves
        def check_bishop_move(self,move,turn,which):
            self.move = move
            self.turn = turn
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            query = "select * from board where Piece = 'Bishop' and Colour = '%s';"
            mycursor.execute(query % (turn_colour))
            result = mycursor.fetchall()
            for i in result:
                tupl = i
            move_manip = str(self.move[1]) + str(self.move[2])
            if str(tupl[0]) == str(move_manip):
                print("cannot move to the same location")
                quit()
            
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    print("legal bishop move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    Movement.get_current_loc(self,"Bishop",self.move,self.turn)

        # checking pawn moves
        def check_pawn_move(self,move,turn,which):
            pwn_move_legality = False
            self.move = move
            self.turn = turn
            self.which = which
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            mod_move = self.move[1] + self.move[2]

            if (int(self.move[2]) > int(self.which[1]) and turn_colour == "White") or (int(self.move[2]) < int(self.which[1]) and turn_colour == "Black"):
                if (int(self.move[2]) - 2 == 2 and turn_colour == "White") or (int(self.move[2]) + 2 == 7 and turn_colour == "Black"):
                    pwn_move_legality = True
                    print("pawns are allowed to move two paces on the first step") 
                elif (int(self.move[2]) -1 == int(self.which[1])) or (int(self.move[2]) + 1 == int(self.which[1])):
                    pwn_move_legality = True
                    print("all other pawns can move one step")
                else:
                    pwn_move_legality = False
                    quit()
                if str(which_stck[-1]) == str(mod_move):
                    print("cannot move to the same location")
                    pwn_move_legality = False
                    quit()
            else:
                print("pawns cannot go backwards")
                pwn_move_legality = False
                quit()
            which_stck_mod = which_stck
            which_stck_mod.pop()

            if pwn_move_legality == True:
                if self.move[0] == "p" or self.move[0] == "x":
                    if self.move[1] == self.which[0]:
                        move_stck.append(mod_move)
                        print("legal pawn move")
                        if self.move[0] == "p":
                            Movement.get_current_loc(self,"Pawn",mod_move,self.turn)
                    elif self.move[0] == "x":
                        move_stck.append(mod_move)
                        query = "select * from board where Location = '%s';"
                        mycursor.execute(query % (mod_move))
                        result = mycursor.fetchall()
                        if result != []:
                            I = Interaction()
                            I.capture(self.which,mod_move,"Pawn",self.turn)
                        else:
                            raise Exception("cannot capture a blank square")
                    else:
                        print("the pawn can only move straight")
                        quit()

        # check knight moves
        def check_knight_move(self,move,turn,which):
            self.move = move
            self.turn = turn
            self.which = which
            
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"

            if self.move[1] in self.hor and int(self.move[2]) in self.ver:
                query = "select Piece, Colour from board where Location = '%s';"
                mycursor.execute(query % (self.which))
                result = mycursor.fetchall()
                self.move = move[1] + move[2]
                if result != []: 
                    for i in result:
                        requ = i
                    if requ[0] == "Knight" and requ[1] == turn_colour:
                        
                        kX = [1,-1,1,-1,2,2,-2,-2]
                        kY = [2,2,-2,-2,1,-1,1,-1]
                        knightLegalmoves = []
                        current_loc = self.which
                        for sqr, coor in Movement.loc_dict.items():
                            if sqr == current_loc:
                                co_or = coor
                        permaCoord = co_or
                        lindex = 0
                        legitX = True
                        legitY = True
                        while True:
                            if lindex > 7:
                                break
                            else:
                                co_or_x = permaCoord[0]
                                co_or_y = permaCoord[1]
                                co_or_x += kX[lindex]
                                co_or_y += kY[lindex]
                            
                                if co_or_x > 7 or co_or_x < 0:
                                    legitX = False
                                elif co_or_y > 7 or co_or_y < 0:
                                    legitY = False
                                else: 
                                    legitX = True
                                    legitY = True
                                    
                                if legitX == True and legitY == True:
                                    co_orKnight = tuple([co_or_x,co_or_y])
                                    for a,b in Movement.loc_dict.items():
                                        if b == co_orKnight:
                                            knightLegalmoves.append(a)
                            lindex += 1

                        for i in knightLegalmoves:
                            if i == self.move:
                                move_stck.append(self.move)
                                print(self.move, self.which)
                                print("legal knight move")
                                query = "select * from board where Location = '%s';"
                                mycursor.execute(query % self.move)
                                result = mycursor.fetchall()
                                if result != []:
                                    #meaning capture
                                    I = Interaction()
                                    I.capture(self.which,self.move,"Knight",self.turn)
                                else:
                                    B = Board()
                                    B.update_board("Knight",self.which,self.move)
                                    #meaning no capture only move
                                    pass
                                
                        else:
                            which_stck.pop()
             
                    else:
                        print("[ILLEGAL MOVE] 0")    
                else:
                    print("[ILLEGAL MOVE] 1")
            else:
                print("[ILLEGAL MOVE] 2")
                quit()

        # checking castling move
        def check_castle(self,move):
            
            self.move = move
            castlePieceMoved = True # returns False if either the King or Rook was moved
            castlePieceOccupied = True # return False if the castle squares are occupied 
            castleINCHECK = True # returns False if the king is currently in check 
            castleTransit = True # returns False if the king is in check while in transit

            # ~Check if the squares are occupied~
            # ~Check if the King was moved~
            # ~Check if the Rook was moved~
            # Simulate king movement and check if the king is in check
            # If all conditions are satisfied then castle!
            # If not revert to taking input from the same player

            if ((turn-1) % 2) != 0:
                turn_colour = "White"
                if w_inCheck == True:
                    castleINCHECK = False
            else:
                turn_colour = "Black"
                if b_inCheck == True:
                    castleINCHECK = False

            if self.move == "O-O":
                if turn_colour == "White":
                    # checking whether the King or Rook was moved before
                    query = "select Moved from castle where Location in ('h1','e1');"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    for i in result:
                        if i[0] == 'n':
                            pass
                        else:
                            castlePieceMoved = False
                    # checking wheather the pieces are occupied or not for the short castle
                    OOsquaresWhite = ["f1","g1"]
                    for i in OOsquaresWhite:
                        query = "select * from board where Location ='%s';"
                        mycursor.execute(query % i)
                        result = mycursor.fetchall()
                        if result != []:
                            castlePieceOccupied = False
                            break
                        else:
                            pass
                    
                    # checking if there is a check in transit
                    for i in OOsquaresWhite:
                        query = "update board set Location = '%s' where Piece = 'King' and Colour = 'White';"
                        mycursor.execute(query % i)
                        db.commit()
                        B = Board()
                        B.incheck()
                        if incheck_status:
                            castleTransit = False
                            break
        
                elif turn_colour == "Black":
                    # checking whether the King or Rook was moved before
                    query = "select Moved from castle where Location in ('h8','e8');"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    for i in result:
                        if i[0] == 'n':
                            pass
                        else:
                            castlePieceMoved = False
                    # checking wheather the pieces are occupied or not for the short castle
                    OOsquaresBlack = ["f8","g8"]
                    for i in OOsquaresBlack:
                        query = "select * from board where Location ='%s';"
                        mycursor.execute(query % i)
                        result = mycursor.fetchall()
                        if result != []:
                            castlePieceOccupied = False
                            break
                        else:
                            pass

            elif self.move == "O-O-O":
                if turn_colour == "White":
                    # checking whether the King or Rook was moved before
                    query = "select Moved from castle where Location in ('a1','e1');"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    for i in result:
                        if i[0] == 'n':
                            pass
                        else:
                            castlePieceMoved = False
                    # checking wheather the pieces are occupied or not for the long castle
                    OOOsquaresWhite = ["b1","c1","d1"]
                    for i in OOOsquaresWhite:
                        query = "select * from board where Location ='%s';"
                        mycursor.execute(query % i)
                        result = mycursor.fetchall()
                        if result != []:
                            castlePieceOccupied = False
                            break
                        else:
                            pass

                elif turn_colour == "Black":
                    # checking whether the King or Rook was moved before
                    query = "select Moved from castle where Location in ('a8','e8');"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    for i in result:
                        if i[0] == 'n':
                            pass
                        else:
                            castlePieceMoved = False
                    # checking wheather the pieces are occupied or not for the long castle
                    OOOsquaresBlack = ["b8","c8","d8"]
                    for i in OOOsquaresBlack:
                        query = "select * from board where Location ='%s';"
                        mycursor.execute(query % i)
                        result = mycursor.fetchall()
                        if result != []:
                            castlePieceOccupied = False
                            break
                        else:
                            pass

            # finally checking for castle legality
            if castlePieceOccupied and castlePieceMoved and castleINCHECK and castleTransit:
                print("[CAN CASTLE] True")
                if self.move == "O-O":
                    query0 = "update board set Location = 'g1' where Piece = 'King' and Colour = '%s';"
                    mycursor.execute(query0 % turn_colour)
                    db.commit()
                    query1 = "update board set Location = 'f1' where Piece = 'Rook' and Colour = '%s';"
                    mycursor.execute(query1 % turn_colour)
                    db.commit()
                    Board.cleanup()
                    B = Board()
                    B.show_updated_board()
                elif self.move == "O-O-O":
                    query0 = "update board set Location = 'c1' where Piece = 'King' and Colour = '%s';"
                    mycursor.execute(query0 % turn_colour)
                    db.commit()
                    query1 = "update board set Location = 'd1' where Piece = 'Rook' and Colour = '%s';"
                    mycursor.execute(query1 % turn_colour)
                    db.commit()
                    Board.cleanup()
                    B = Board()
                    B.show_updated_board()
            else:
                print("[CAN CASTLE] False")
                quit()
            
# class to deal with capture and promotion related interactions
class Interaction(Movement):
    def __init__(self) -> None:
        pass

    # method to deal with piece captures
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

    # method to deal with auto-promotion to a queen
    # a pawn only promotes to a queen if there is no same colour piece on the board
    def promote(self):
        white_promote_squares = ["a8","b8","c8","d8","e8","f8","g8","h8"]
        black_promote_sqaures = ["a1","b1","c1","d1","e1","f1","g1","h1"]
        w_q_present = False
        b_q_present = False

        if ((turn-1) % 2) != 0:
                turn_colour = "White"
        else:
            turn_colour = "Black"

        for i in Board.li:
            for j in i:
                if j == Pieces.w_queen:
                    w_q_present = True
                if j == Pieces.b_queen:
                    b_q_present = True

        while True:
            query = "select * from board where Piece = 'Pawn' and Colour = '%s';" 
            mycursor.execute(query % (turn_colour))
            result = mycursor.fetchall()
            for i in result:
                tupl = i
                if w_q_present != True:
                    if tupl[2] == "White":
                        if tupl[0] in white_promote_squares:
                            query = "update board set Piece = 'Queen' where Colour = 'White' and Location ='%s';"
                            mycursor.execute(query % tupl[0])
                            db.commit()
                            break
                elif b_q_present != True:
                    if tupl[2] == "Black":
                        if tupl[0] in black_promote_sqaures:
                            query = "update board set Piece = 'Queen' where Colour = 'Black' and Location ='%s';"
                            mycursor.execute(query % tupl[0])
                            db.commit()
                            break
            break

# method to open the manual file
def manual():
    with open("manual.txt","r") as fobj:
        content = fobj.read()
        print(content)

# das main functions!
def main():
    B = Board()
    B.create_board()
    M = Movement()

    global turn
    revertStatus = False

    if ((turn) % 2) != 0:
        turn_colour = "WHITE"
    else:
        turn_colour = "BLACK"

    if (turn - 1)  % 2 == 0:
        revertColour = "White"
    else:
        revertColour = "Black"    

    print()
    B.incheck()
    print(f"[{turn_colour}] to move")
    move = input("enter move : ")
    turn_stck.append(move)
    turn += 1

    # if turn > 3:
    #     Board.revert_update_board_load

    global which
    which = "" #current position for the piece to be moved
    
    if move[0] == "K":
        which_stck.append(" ")
        M.check_king_move(move,turn)
    elif move[0] == "Q":
        which_stck.append(" ")
        M.check_queen_move(move,turn)
    elif move[0] == "B":
        which = input("enter current position of the bishop to be moved : ")
        which_stck.append(which)
        M.check_bishop_move(move,turn,which)
    elif move[0] == "N":
        which = input("enter current position of the knight to be moved : ")
        which_stck.append(which)
        M.check_knight_move(move,turn,which)
    elif move[0] == "p" or move[0] == "x":
        which = input("enter current position of the pawn to be moved : ")
        which_stck.append(which)
        restore_stck.append(move)
        M.check_pawn_move(move,turn,which)
    elif move[0] == "R":
        which = input("enter current position of the rook to be moved : ")
        which_stck.append(which)
        M.check_rook_move(move,turn,which)      
    elif move == "O-O" or move == "O-O-O":
        which_stck.append(" ")
        M.check_castle(move)
    elif move == "/draw":
        B.draw_game(turn)
    elif move == "/forfeit":
        B.forfeit(turn)
    elif move == "/revert":
        if (turn - 1)  % 2 == 0:
            revertColour = "White"
        else:
            revertColour = "Black"
        print(revertColour)
        B.revert_board_status()
        # B.show_updated_board()

splash_screen_0 = """
 _                      _             _                  
| |_ ___ _ __ _ __ ___ (_)_ __   __ _| |  
| __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |  
| ||  __/ |  | | | | | | | | | | (_| | |  
 \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|                                     
"""
splash_screen_1 = """
      _
  ___| |__   ___  ___ ___ 
 / __| '_ \ / _ \/ __/ __|
| (__| | | |  __/\__ \__ \ 
 \___|_| |_|\___||___/___/
"""

print(splash_screen_0,splash_screen_1)
time.sleep(2)
print("1. /play - to play terminal chess")
print("2. /manual - to open the manual")
print("3. /quit - to quit")
choice = int(input("enter choice : "))
if choice == 1:
    main()
elif choice == 2:
    manual()
elif choice == 3:
    quit()
else:
    main()