import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time, json
import numpy as np

class TicTacToeAPI:
    CONNECTING = 0
    OPEN = 1
    CLOSING =2
    CLOSED = 3

    LOST = 0
    WON = 1
    TIE = 2
    PLAYING = 3
    WAITING = 4
    ABORTED = 5

    playerSymbols = {0:"x", 1:"o"}
    def __init__(self, hostname,  computeMoveCallback, endCallback, playAgainCallback):
        self.readyState = self.CONNECTING
        self.gameState = self.WAITING 
        self.computeMove= computeMoveCallback
        self.endGame = endCallback
        self.playAgain = playAgainCallback
        self.hostname = hostname
        self.connect()
    
    def sendMessage(self, data):
        if self.readyState == self.OPEN:
            self.conenction.send(json.dumps(data))
        else:
            raise TypeError("Connection to websocket is not open, cannot send data")

    def joinRoom(self, roomCode):
        self.roomCode = roomCode
        self.sendMessage({"action":"joinRoom", "roomCode":self.roomCode})

    def createRoom(self):
        self.sendMessage({"action":"createRoom"})
    
    def makeMove(self,position):
        self.sendMessage({"action":"makeMove", "roomCode":self.roomCode, "move":{"x":position[0], "y":position[1]}})
        
    def on_open(self):
        self.readyState = self.OPEN

    def on_message(self, conenction, msg):
        message = json.loads(msg)
        for i in message:
            if i == "playerIndex":
                self.playerIndex = message["playerIndex"]
            elif i == "roomCode":
                self.roomCode = message["roomCode"]
            elif i == "error":
                print("recieved error from server: {}".format(message["error"]))
            elif i == "gameField":
                self.gameField = np.reshape(message["gameFiled"], (3,3))
            elif i == "yourTurn":
                self.makeMove(self.computeMove(self))
            elif i == "winner":
                self.state = self.WON if message["winner"] == True else self.LOST
            elif i == "isTie":
                self.state = self.TIE
            elif i == "aborted":
                self.state = self.ABORTED
            elif i == "playAgain":
                self.playAgain()

    def on_error(self, connection, error):
        print("error :(")

    def on_close(self, connection, statuscode, message):
        self.readyState = self.ABORTED
    
    @property
    def readyState(self):
        return self._readyState

    @readyState.setter
    def readyState(self, value):
        print("state:", value)
        self._readyState = value

    def connect(self):
        self.connection = websocket.WebSocketApp("ws://{}".format(self.hostname),
                                                on_open=self.on_open,
                                                on_message=self.on_message,
                                                on_error=self.on_error,
                                                on_close=self.on_close)

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    def humanGetMove(api):
        print("\n----------\n"," 0 1 2",)
        for i in range(api.gameField):
            print(i, " ".join(map(lambda x: api.playerSymbols[int(x)] if int(x) in api.playerSymbols else "□", api.gameField[i])))
        
        while True:
            try:
                x = input("enter x: ")
                y = input("enter y: ")
                break
            except:
                print("illegal move")
                pass
        return [int(y),int(x)]
    def ask(question):
        while True:
            answer = input(question + "[y,n]: ").lower()
            if answer == "y":
                return True
            elif answer == "n":
                return False

    api = TicTacToeAPI("10.165.20.3:8080", humanGetMove, lambda x : print("connection closed"), lambda x : print("new game"))
    print("connecting...")
    while api.readyState == api.CONNECTING:
        time.sleep(.5)

    print("connected")
    if(ask("create room")):
        api.createRoom()
    else:
        roomCode = input("enter room code: ")
        api.joinRoom(roomCode)

    while api.readyState == api.OPEN:
        time.sleep(.5)
    print("closed")