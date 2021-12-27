from nxtrobot import *
from tcpcom import TCPServer

STEERANGLE = 90
ROUNDDUR = 1900

def steerRight():
    steerReset()
    steer.continueTo(STEERANGLE)

def steerLeft():
    steerReset()
    steer.continueTo(-STEERANGLE)

def steerReset():
    steer.continueTo(0)

def turnRight(degree, forward = True):
    steerRight()
    if(forward):
        drive.forward()
    else:
        drive.backward()
    Tools.delay(int(round(ROUNDDUR/90*degree)))
    drive.stop()
    steerReset()

def turnLeft(degree, forward = True):
    steerLeft()
    if(forward):
        drive.forward()
    else:
        drive.backward()
    Tools.delay(int(round(ROUNDDUR//90*degree)))
    drive.stop()
    steerReset()
    
def handleTCPClient(state, message):
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
    elif state == TCPServer.TERMINATED:
        print("server stopped")
    else:
        print("unknown state", state)

server = TCPServer(81, stateChanged=handleTCPClient)
connectionState = None

# setup
robot = LegoRobot("Terminator")
steer = Motor(MotorPort.B)
drive = Motor(MotorPort.A)

robot.addPart(steer)
robot.addPart(drive)
while not robot.isEscapeHit():
    l = robot.isLeftHit()
    r = robot.isRightHit()
    b = robot.isDownHit()
    f = robot.isUpHit()
    if l and not r:
        steerLeft()
    if r and not l:
        steerRight()
    if not r and not l:
        steerReset()
        
    if f and not b:
        drive.forward()
    if b and not f:
        drive.backward()
    if not b and not f:
        drive.stop()
        
        