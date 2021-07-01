# terminal_chess
TLDR; A terminal based chess game.

Languages used : Python, mySQL </br>
OS : Linux Mint </br>
AIM : Create a functional chess game for two players that can be played on the linux terminal.

The current work is being done on version V3, previous versions were V1 and V2 which were my failed attempts at making a chess game. 

If you have any suggestions or ideas feel free to reach out at : adhyanpatel@protonmail.com 

## Requirements
* Python 3.x
* mySQL.connector

```python pip3 install mysql-connector```

## How to run
1. Run setup.py 
2. Open and run on your terminal main.py
3. Ensure main.py and/or setup.py is executable
  
## Known Bugs/ Quirks
* Have to manually modify main.py </br>
```python db = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    passwd = "xyz",
    database = "chess"
```
</br>
As of now you will need to manual change the following attributes : user, passwd, if running on localhost.</br>

##### mySQL password(s) are saved as plain texts. [⚠️ Potential Security Threat!!!]

* No en passant rule
* No castling
* Making an illegal move quits the game 
* Sometimes you can capture your own piece(s)
* There is no stalemate only draw by insufficient material
* There is no checkmate the game ends when either one of the King is captured
* Ke2 follwed by Qd7 gets stuck in an infinite loop

## Future goals : 
  1. Prettify the output to the terminal
  2. Create a GUI
  3. Add ability to play against bot(s)/engine(s)
  4. Potentional online multiplayer ability

## License :
Not for commercial use</br>

Author : Adhyan H. (github.com/frroossst)</br>
Email : adhyanpatel@protonmail.com
