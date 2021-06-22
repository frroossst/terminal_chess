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

li= [[Pieces.b_rooke,Pieces.b_knight,Pieces.b_bishop,Pieces.b_queen,Pieces.b_king,Pieces.b_bishop,Pieces.b_knight,Pieces.b_rooke,"8"],
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


print("OLD LIST")
for i in li:
    print(i)
    
print()
print("NEW LIST")
li_len = len(li)
count = 7
while True:
    print(li[count])
    count -= 1
    if count < 0:
        break


print()
print("ADJUSTED NEW LIST")