from TTTsolver import TicTacToeSolver
from TCPUDPServer import Server
import numpy as np
import json

def handleRequest(message, address):
    decodedMessage = json.loads(message)
    print(decodedMessage)
    role = decodedMessage["role"]
    board = np.array(decodedMessage["board"])
    x,y = map(int, tictactoe.solveState(board, role))
    print(x,y)
    return json.dumps({"x":x, "y":y})

tictactoe = TicTacToeSolver("policy_3_3_x.pkl","policy_3_3_o.pkl")
server = Server("TCP", 8080)
server.listen(handleRequest)