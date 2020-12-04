import sys
from termcolor import colored, cprint
pos_init=[[' 8','rke','kgt','bhp','qun','kng','bhp','kgt','rke'],
          [' 7','pwn','pwn','pwn','pwn','pwn','pwn','pwn','pwn'], 
          [' 6','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 5','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 4','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 3','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 2','pwn','pwn','pwn','pwn','pwn','pwn','pwn','pwn'],
          [' 1','rke','kgt','bhp','qun','kng','bhp','kgt','rke'],
          ['  ',' a ',' b ',' c ',' d ',' e ',' f ',' g ',' h '],
         ]
pos_board=pos_init
def board_view():
   i= True  
   x,y=0,0
   while i:
       if y>8:
           x+=1
           y=0
           print()
       if x>8 and y<8:
           break   
       else:    
           print(pos_board[x][y],end=' | ')
       y+=1       
        
board_view()

pos_board_white=pos_init
pos_board_black=pos_init

print()
clr_player=input("black or white ? ")
if clr_player == 'w' or 'white':
    print("you are playing as white. ")
    cmd=input("enter a command : ")
    #pawn move
    if cmd[0]=='p':
        print("pawn move")
        if cmd[1]=='a':
            if int(cmd[2]) > 2:
                print("illegal move")   
        elif cmd[1]=='b':







