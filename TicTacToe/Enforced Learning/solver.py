from tictactoeAPI import TicTacToeAPI
import numpy as np
import pickle, json
import sys

class TicTacToeSolver:
    def __init__(self, attackerFile, defenderFile) -> None:
        self.scores = {}
        try:
            with open(attackerFile, "rb") as f:
                self.scores = {**self.scores, **pickle.load(f)}
                f.close()
            # print("attackerfile loaded")
        except Exception as e:
            pass
            # print("failed to load", attackerFile)
            # print(e)
        
        try:
            with open(defenderFile, "rb") as f:
                self.scores = {**self.scores, **pickle.load(f)}
                f.close()
            # print("defenderFile loaded")
        except Exception as e:
            # print("failed to load", defenderFile)
            # print(e)
            pass

    def solveState(self, board):
        highestScore = float("-inf")
        attackerMoves = np.count_nonzero(board==-1)
        defenderMoves= np.count_nonzero(board==1)
        if attackerMoves < defenderMoves:  # -1 allways starts game and therefore never made less moves
            # print("flipping board")
            return self.solveState(board*-1)
        # print("board is all right", print(board))
        currentPlayer = -1 if defenderMoves>=attackerMoves else 1
        # print("playing for", currentPlayer)
        board[board == -0.] = 0. # flip all -0 to 0 so the identifier will work
        action = [-1,-1]
        for move in self.getValidMoves(board):
            possibleBoard = board.copy()
            possibleBoard[move[0]][move[1]] = currentPlayer
            possibleBoardId = self.getBoardIdentifier(possibleBoard)
            score = 0 if self.scores.get(possibleBoardId) is None else self.scores.get(possibleBoardId)
            # print(possibleBoardId, score)
            if score >= highestScore:
                highestScore = score
                action = move
        return action

    def getBoardIdentifier(self, board):
        boardIdentifier = str(board.reshape(np.prod(board.shape)))
        return boardIdentifier

    def getValidMoves(self, board):
        # print(board)
        return np.argwhere(board == 0)


if __name__ == "__main__":
    solver = TicTacToeSolver("policy_3_3_x.pkl","policy_3_3_o.pkl")
    while True:
        try:
            board = np.empty(9, dtype="float64") 
            if len(sys.argv) > 1:
                board[:] = sys.argv[1].split(",")
            else:
                board[:] = (input("enter board like 1,-1,0,1,0,... : ").split(","))
            y,x = (solver.solveState(np.reshape(board, (3,3))))
            print(json.dumps({"x":int(x), "y":int(y)}))
            break
        except Exception as e:
            print("cannot handle your input, try again...")
            print(e)