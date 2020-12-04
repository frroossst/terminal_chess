import sys
from termcolor import colored, cprint

#piece attributes
'piece=[human readable position, matrix position, move no.,status, color]'
bpwn1=['a7',10,0,'alive','black']
bpwn2=['b7',11,0,'alive','black']
bpwn3=['c7',12,0,'alive','black']
bpwn4=['d7',13,0,'alive','black']
bpwn5=['e7',14,0,'alive','black']
bpwn6=['f7',15,0,'alive','black']
bpwn7=['g7',16,0,'alive','black']
bpwn8=['h7',17,0,'alive','black']
wpwn1=['a2',60,0,'alive','white']
wpwn2=['b2',61,0,'alive','white']
wpwn3=['c2',62,0,'alive','white']
wpwn4=['d2',63,0,'alive','white']
wpwn5=['e2',64,0,'alive','white']
wpwn6=['f2',65,0,'alive','white']
wpwn7=['g2',66,0,'alive','white']
wpwn8=['h2',67,0,'alive','white']
 

#board layout
pos_init=[[' 8','rke','kgt','bhp','qun','kng','bhp','kgt','rke'],
          [' 7','pwn','pwn','pwn','pwn','pwn','pwn','pwn','pwn'], 
          [' 6','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 5','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 4','   ','   ',' x ','   ','   ','   ','   ','   '],
          [' 3','   ','   ','   ','   ','   ','   ','   ','   '],
          [' 2','pwn','pwn','pwn','pwn','pwn','pwn','pwn','pwn'],
          [' 1','rke','kgt','bhp','qun','kng','bhp','kgt','rke'],
          ['  ',' a ',' b ',' c ',' d ',' e ',' f ',' g ',' h '],
         ]
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
           print(pos_init[x][y],end=' | ')
       y+=1       
board_white=pos_init
board_view()
print(pos_init[6][2])
pos_board=[bpwn1,bpwn2,bpwn3,bpwn4,bpwn5,bpwn6,bpwn7,bpwn8,wpwn1,wpwn2,wpwn3,wpwn4,wpwn5,wpwn6,wpwn7,wpwn8]

cmd=input("enter a move : ")
if cmd[0]=='p':
    print("pawn move")
    if cmd[1]=='c':
        print("to the c phile")
        if cmd[2]=='4':
            print("the 4th column")
            wpwn3.pop(1)
            pwn_mov=int(cmd[2])-int(wpwn3[0][1])
            curr_pos=wpwn3
            wpwn3.pop(0)
            hr=cmd[1]+cmd[2]
            wpwn3.insert(0,hr) 
            if pwn_mov==2:
                wpwn3.pop(1) 
                wpwn3.insert(1,43)
            board_white.pop([4][3])
            board_white.insert([4][3],'pwn')
print(wpwn3)             










