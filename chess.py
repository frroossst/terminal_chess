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

### create two separate board for balck and white and then superimpose them. maybe
'''
print()
clr_player=input("black or white ? ")
if clr_player == 'w' or 'white':
    print("you are playing as white")
    print(pos_start[6][1])
    #pos_init[6].pop(1)
    print(pos_start[6][1])
for i in pos_init:
    print(i)
    for j in i:
        print(j,end=' ')
print()

n=0
i=True
while i:
    print(pos_init[n])
    print()
    n+=1'''
