# terminal_chess
TLDR; A terminal based chess game.

Languages used : Python, mySQL
OS : Linux Mint </br>
AIM : Create a functional chess game for two players that can be played on the linux terminal.

The current work is being done on version V3, previous versions were V1 and V2 which were my failed attempts at making a chess game. 

If you have any suggestions or ideas feel free to reach out at : adhyanpatel@protonmail.com (Email)

##Requirements
* Python 3.x
* mySQL.connector

##How to run
1. Run setup.py 
2. Open and run on your terminal main.py
3. Ensure main.py and/or setup.py is executable
  
##Known Bugs
* Have to manually modify main.py </br>
db = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    passwd = "xyz",
    database = "chess"
</br>
As of now you will need to manual change the following attributes : user, passwd

* No en passant rule
* No castling
* Making an illegal move quits the game 
* Sometimes you can capture your own piece(s)

##Future goals : 
  1. Create a GUI
  2. Add ability to play against bot(s)/engine(s)
  3. Potentional online multiplayer ability
