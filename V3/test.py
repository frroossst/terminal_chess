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
    li= [
        [Pieces.b_rooke,Pieces.b_knight,Pieces.b_bishop,Pieces.b_queen,Pieces.b_king,Pieces.b_bishop,Pieces.b_knight,Pieces.b_rooke,"8"],
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
    ceiling = "_"

for i in Board.li:
    print()
    for j in i:
        print(" ",j," ",Board.pipe,end=" ")
    print()
print()
for a in Board.label:
    print(a,Board.pipe,end=" ")

# "insert into startBoard values ('d1','Queen','White',NULL);"
# "insert into startBoard values ('e1','King','White',NULL);"
# "insert into startBoard values ('f1','Bishop','White',NULL);"
# "insert into startBoard values ('c1','Bishop','White',NULL);"
# "insert into startBoard values ('g1','Knight','White','g1');"
# "insert into startBoard values ('b1','Knight','White','b1');"
# "insert into startBoard values ('h1','Rook','White','h1');"
# "insert into startBoard values ('a1','Rook','White','a1');"
# "insert into startBoard values ('a2','Pawn','White','a2');"
# "insert into startBoard values ('b2','Pawn','White','b2');"
# "insert into startBoard values ('c2','Pawn','White','c2');"
# "insert into startBoard values ('d2','Pawn','White','d2');"
# "insert into startBoard values ('e2','Pawn','White','e2');"
# "insert into startBoard values ('f2','Pawn','White','f2');"
# "insert into startBoard values ('g2','Pawn','White','g2');"
# "insert into startBoard values ('h2','Pawn','White','h2');"

# "insert into startBoard values ('d8','Queen','Black',NULL);"
# "insert into startBoard values ('e8','King','Black',NULL);"
# "insert into startBoard values ('f8','Bishop','Black',NULL);"
# "insert into startBoard values ('c8','Bishop','Black',NULL);"
# "insert into startBoard values ('g8','Knight','Black','g8');"
# "insert into startBoard values ('b8','Knight','Black','b8');"
# "insert into startBoard values ('h8','Rook','Black','h8');"
# "insert into startBoard values ('a8','Rook','Black','a8');"
# "insert into startBoard values ('a7','Pawn','Black','a7');"
# "insert into startBoard values ('b7','Pawn','Black','b7');"
# "insert into startBoard values ('c7','Pawn','Black','c7');"
# "insert into startBoard values ('d7','Pawn','Black','d7');"
# "insert into startBoard values ('e7','Pawn','Black','e7');"
# "insert into startBoard values ('f7','Pawn','Black','f7');"
# "insert into startBoard values ('g7','Pawn','Black','g7');"
# "insert into startBoard values ('h7','Pawn','Black','h7');"