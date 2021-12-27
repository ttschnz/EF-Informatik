from tcpcom import TCPClient
import time, json, gamegrid


"""-------------------------------------------CONNECTION TO SERVER---------------------------------------------"""
def send(content):
    print("<-", content)
    if(type(content)==str):
        client.sendMessage(content)
    else:
        client.sendMessage(json.dumps(content))
    
def handleMessage(state,message):
    global connectionState
    connectionState = state
    if state == TCPClient.CONNECTED:
        # CONNECTED
        print("connection established, ready to exchange messages")
    elif state == TCPClient.CONNECTING:
        print("connecting to server...")
    elif state == TCPClient.CONNECTION_FAILED:
        # CONNECTION FAILED
        print("connection failed, trying to reconnect")
        time.sleep(1)
        client.connect()
    elif state == TCPClient.DISCONNECTED:
        # SERVER DISCONNECTED
        print("disconnected, trying to reconnect")
        time.sleep(1)
        client.connect()
    elif state == TCPClient.MESSAGE:
        # NEW MESSAGE
        print("->", message)
        message = json.loads(message)
        
    else:
        # unknown state
        print("unknown state:", state)

    
    

"""-------------------------------------------GAME---------------------------------------------"""

class Player(gamegrid.Actor):
    def __init__(self, game):
        gamegrid.Actor.__init__(self, "sprites/animal.gif")
        self.game = game

    def handleKeyPress(self,e):
        keyCode = e.getKeyCode()
        send({"action":"down", "data":keyCode})
        return
    
    def handleKeyRelease(self, e):
        keyCode = e.getKeyCode()
        send({"action":"up", "data":keyCode})
        
    def act(self):
        return

class Game:
     def __init__(self):
        self.player = Player(self)
        self.startPos={}
        self.width=10
        self.height=10
        self.startPos["x"] = 1
        self.startPos["y"] = 1
        self.player = Player(self)
        self.grid = gamegrid.makeGameGrid(self.width,self.height,50,None, "", False, keyPressed = self.player.handleKeyPress, notifyExit = self.close, keyReleased=self.player.handleKeyRelease)
        self.grid.setTitle("playground")
        self.grid.addActor(self.player, gamegrid.Location(self.startPos["y"], self.startPos["y"]))
        self.grid.show()
        
     def close(self):
        self.grid.dispose()
        client.disconnect()
        
"""-------------------------------------------RUN IT---------------------------------------------"""

connectionState = None
SERVER_IP = "10.165.179.34"
SERVER_PORT = "81"
client = TCPClient(SERVER_IP, SERVER_PORT, stateChanged = handleMessage)
client.connect()

game = Game()
    