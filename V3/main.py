import time
import mysql.connector
import logging

global turn
turn = 1

global revert_status
revert_status = False

global turn_stck
turn_stck = [] #human inputted stack of instructions : like pc3 as compared to c3 in move_stck
 
global move_stck
move_stck = []

global which_stck
which_stck = []

global restore_stck
restore_stck = []

# logging.basicConfig(filename='debug.log', level=logging.DEBUG,format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("--- INITIALIZED ---")

with open("sql.txt","r") as fobj:
    content = fobj.readlines()
    x = content[0].strip()
    y = content[1].strip()
    z = content[2].strip()

db = mysql.connector.connect(
    host = z,
    user = x,
    passwd = y,
    database = "chess"
)
mycursor = db.cursor()
logging.info("sql server connection established")

mycursor.execute("drop table board")
mycursor.execute("create table board (Location char(5), Piece varchar(15), Colour char(5), Which char(5));")
#white pieces data entry
logging.debug("white pieces data entry")
mycursor.execute("insert into board values ('d1','Queen','White',NULL);")
mycursor.execute("insert into board values ('e1','King','White',NULL);")
mycursor.execute("insert into board values ('f1','Bishop','White',NULL);")
mycursor.execute("insert into board values ('c1','Bishop','White',NULL);")
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
#black pieces data entry
logging.debug("black pieces data entry")
mycursor.execute("insert into board values ('d8','Queen','Black',NULL);")
mycursor.execute("insert into board values ('e8','King','Black',NULL);")
mycursor.execute("insert into board values ('f8','Bishop','Black',NULL);")
mycursor.execute("insert into board values ('c8','Bishop','Black',NULL);")
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

    li_anti_ghosting = [
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

    @classmethod
    def cleanup(self):
        move = move_stck[-1]
        for move in Board.li_ref_dict:
            coordinates = Board.li_ref_dict[move]
            Board.li[coordinates[0]][coordinates[1]] = " "

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
        which_pieces = ["Rook","Knight","Pawn"]
        if ((turn-1) % 2) != 0:
            turn_colour = "White"
        else:
            turn_colour = "Black"
        if self.piece in which_pieces:
            query = "update board set Location = '%s' where Location = '%s';"
            mycursor.execute(query % (self.now_loc,which))
            db.commit()
        elif self.piece not in which_pieces:
            query = """update board set Location = '%s' where Piece = '%s' and Colour = '%s';"""
            tupl = (self.now_loc,self.piece,turn_colour)
            # print(tupl)
            mycursor.execute(query % tupl)
            db.commit()
        else:
            raise Exception ("Unknown_Piece_Encountered")



### [FATAL] RESUME WORK HERE TO REMOVE VERTICAL MOVE GHOSTING FOR BLACK QUEEN
        for c_move, co_or in Board.li_ref_dict.items():
            if str(c_move) == str(self.prev_loc):
                # print(c_move,co_or)
                # print(Board.li_ref_empty[co_or[0]][co_or[1]]) #This piece shouldn't be there
                # print(f"index one : {co_or[0]} index two : {co_or[1]}")
                # print(type(co_or))
                # print(type(co_or[0]))
                cleanup = Board.li
                int0 = int(co_or[0])
                int1 = int(co_or[1])
                # print(type(int0))
                cleanup[int0].pop(int1)
                cleanup[int0].insert(int1," ")

        Interaction.promote(self)
        Board.cleanup()

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
                    # print(f"Key = {c_move} Value = {co_or}")
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
        for i in Board.li:
            print(i)
        print(Board.label)
        Board.li = Board.li_ref_empty

        B = Board()  
        B.check_game_over()

    # @staticmethod
    def check_game_over(self):
        # print(move_stck)
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
            #print(i)
        if j[0] == 2:
            draw = True
            print(draw_msg)
            quit()
        # print(type(i[0]))
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

    def restore_pawn_status(self):
        print("pawn cannot capture vartically")
        query = """update board set Location = '%s' where Piece = 'Pawn', """
        Board.show_updated_board()

###[FATAL] global is updated after one turn
    def incheck(self):
        global incheck_status
        incheck_status = False
        northsouth_pieces = ["Queen","Rook"]
        diagonal_pieces = ["Queen","Pawn","Bishop"]
        
        if ((turn -1) % 2) != 0:
            turn_colour = "White"
            mod_colour = "WHITE"
            use_colour = "Black"
        else:
            turn_colour = "Black"
            mod_colour = "BLACK"
            use_colour = "White"

        query = "select * from board where Piece = 'King' and Colour = '%s';"
        mycursor.execute(query % (use_colour))
        result = mycursor.fetchall()
        # print(f"use colour = {use_colour}")
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
            # print(current_loc_square_check)
            result = mycursor.fetchall()
            if result!=[]:
                for i in result:
                    tupl = i
                    if tupl[1] == use_colour:
                        loopy_north = False
                    else:
                        if tupl[0] in northsouth_pieces:
                            incheck_status = True
                            loopy_north = False
            else:
                if int(current_loc_square_check[1]) > 8:
                    loopy_north = False
                count += 1
    
    # check south
        count = 1
        loopy_south = True
        while loopy_south:
            current_loc_square_check = current_loc[0] + str((int(current_loc[1]) - count))
            query = ("select Piece, Colour from board where Location = '%s';")
            mycursor.execute(query % current_loc_square_check)
            # print(current_loc_square_check)
            result = mycursor.fetchall()
            if result!=[]:
                for i in result:
                    tupl = i
                    if tupl[1] == use_colour:
                        loopy_south = False
                    else:
                        if tupl[0] in northsouth_pieces:
                            incheck_status = True
                            loopy_south = False
            else:
                if int(current_loc_square_check[1]) > 8:
                    loopy_south = False
                count -= 1
    # check west
    
    # check east
    
    # check northeast
    
    # check northwest
    
    # check southeast
    
    # check southwest
        if incheck_status:
            print(f"[{use_colour}]'s king is in check")
        #to check whether castling is allowed or not
        
        
        # B = Board()
        # B.check_game_over()

    def draw_game(self,turn):
        self.turn = turn
        if ((self.turn-1) % 2) != 0:
            turn_colour = "White"
        else:
            turn_colour = "Black"
        print(f"[{turn_colour}] offers a draw")
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
            quit()
        else:
            turn = turn - 2
            main()    
    
    def forfeit(self,turn):
        self.turn = turn
        if ((self.turn-1) % 2) != 0:
            turn_colour = "White"
        else:
            turn_colour = "Black"
        print(f"[{turn_colour}] forfeits")
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

###[FATAL] Revert_board_status to undo illegal moves.
    def revert_board_status(self):
        self.turn = turn_stck
        self.which = which_stck


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
            if ((turn-1) % 2) != 0:
                turn_colour = "White"
            else:
                turn_colour = "Black"
            which_pieces = ["Rook","Knight","Bishop","Pawn"]
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
                            # print(result)
                            break
                        else:
                            # print("free square")
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
                        # print("1.",loc_square_check)
                        result = mycursor.fetchall()
                        if result != []:
                            if self.piece == "Pawn":
                                B = Board()
                                B.restore_pawn_status()
                            else:
                                print("obstacle encountered")
                                I = Interaction()
                                I.capture(self.current_loc,loc_square_check,self.piece,self.turn)
                                # print(result)
                                break
                        else:
                            # print("free square")
                            count+=1
                            if str(loc_square_check) == str(self.future_loc):
                                print(f"reached at {self.future_loc}")
                                B = Board()
                                B.update_board(self.piece,self.current_loc,self.future_loc)
                                break
                # print("path clear")
            elif (self.future_loc[1]) == (self.current_loc[1]):
                print("the move is horizontal")
                hor_li = ["a","b","c","d","e","f","g","h"]
                while True:
                    if self.current_loc[0] < self.future_loc[0]:
                        print("the move is towards east")
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
                        print("the move is towards west")
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
                                print(f"tupleISED {next_co_or}")
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
                        elif move_direction == "northwest":
                            while True:
                                num0 -= 1
                                num1 -= 1
                                next_co_or = tuple([num0,num1])
                                print(next_co_or)
                                print(f"tupleISED {next_co_or}")
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
                        elif move_direction == "southwest":
                            while True:
                                num0 += 1
                                num1 -= 1
                                next_co_or = tuple([num0,num1])
                                print(f"tupleISED {next_co_or}")
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
                quit()
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
                quit()
#add code for vertical checking for king move            

            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    print("legal king move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    Movement.get_current_loc(self,"King",self.move,self.turn)
                    
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
                quit()
            print(self.move, tupl[0])
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    print("legal rook move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    Movement.get_current_loc(self,"Rook",self.move,self.turn)

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
            print(self.move, tupl[0])
            if self.move[1] in self.hor:
                if int(self.move[2]) in self.ver:
                    #insert check for occupied squares
                    #insert obstacle check
                    print("legal bishop move")
                    self.move = self.move[1] + self.move[2]
                    move_stck.append(self.move)
                    Movement.get_current_loc(self,"Bishop",self.move,self.turn)

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
            # print(self.move[2])
            # print(self.which[1])
            if (self.move[2] > self.which[1] and turn_colour == "White") or (self.move[2] < self.which[1] and turn_colour == "Black"):
                if (int(self.move[2]) - 2 == 2) or (int(self.move[2]) - 2 == 5):
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
#[FATAL] check after multiple pawn moves wheather the program allows for the pawn to move two paces
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
        
        def check_knight_move(self,move,turn,which):
            self.move = move
            self.turn = turn
            self.which = which


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
def manual():
    with open("manual.txt","r") as fobj:
        content = fobj.read()
        print(content)

def main():
    if revert_status == False:
        B = Board()
        B.create_board()
        M = Movement()
        global turn
        if ((turn) % 2) != 0:
            turn_colour = "WHITE"
        else:
            turn_colour = "BLACK"
        print()
        B.incheck()
        print(f"[{turn_colour}] to move")
        move = input("enter move : ")
        turn_stck.append(move)
        # print(f"turn = {turn}")
        turn += 1
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

        elif move == "O-O":
            which_stck.append(" ")
            pass
        elif move == "O-O-O":
            which_stck.append(" ")
            pass
        elif move == "/draw":
            B.draw_game(turn)
        elif move == "/forfeit":
            B.forfeit(turn)
    elif revert_status == True:
        B = Board()
        B.revert_board_status()

logging.info("main()")

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