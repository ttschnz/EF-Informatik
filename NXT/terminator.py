from nxtrobot import *

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

# setup
robot = LegoRobot("Terminator")
steer = Motor(MotorPort.B)
drive = Motor(MotorPort.A)

robot.addPart(steer)
robot.addPart(drive)

drive.setSpeed(100)
steer.setSpeed(20)

turnRight(360)
#turnLeft(45, False)
