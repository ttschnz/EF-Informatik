from tcpcom import TCPServer
import json
import time

def send(content):
    if type(content) == str:
        server.sendMessage(content)
    else:
        server.sendMessage(json.dumps(content))
def handleClient(state, message):
    global connectionState
    connectionState = state
    if state == TCPServer.PORT_IN_USE:
        print("port is allready in use")
    elif state == TCPServer.LISTENING:
        print("listening for client")
    elif state == TCPServer.CONNECTED:
        print("new client connected")    
    elif state == TCPServer.CONNECTED:
        print("new client connected")
    elif state == TCPServer.MESSAGE:
        print("->", message)
        message = json.loads(message)
    elif state == TCPServer.TERMINATED:
        print("server stopped")
    else:
        print("unknown state", state)
   
server = TCPServer(81, stateChanged=handleClient)
connectionState = None

input("press enter to stop server")
server.terminate()