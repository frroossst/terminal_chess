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