
import numpy as np
from TTTbase import HumanPlayer, RemotePlayer, GameField
serverName = 'localhost' 
serverPort = 8080
board = np.zeros(9, dtype="int").reshape(3,3) 

## let user begin
# defender = RemotePlayer("localhost", 8080)
# attacker = HumanPlayer()

## let server begin
attacker = RemotePlayer("localhost", 8080)
defender = HumanPlayer()
game = GameField([attacker, defender], [3,3], useLog = False, enableRandomness = False, winBy = 3)
while True:
    game.start()
    game.printBoard()
    game.reset()
    if(not input("press enter to play again, enter a value to abort") == ""): break