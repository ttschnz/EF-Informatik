from nxtrobot import *
import random
def drive(duration):
    leftMotor.forward()
    rightMotor.forward()
    Tools.delay(duration)

def reverse(duration):
    leftMotor.backward()
    rightMotor.backward()
    Tools.delay(duration)
    
def turnLeft(duration):
    leftMotor.backward()
    rightMotor.forward()
    Tools.delay(duration)
    
def turnRight(duration):    
    leftMotor.forward()
    rightMotor.backward()
    Tools.delay(duration)

offsetRight = 50 # the right value is allways 50 units too high

robot = LegoRobot("Terminator")
rightMotor = Motor(MotorPort.A)
leftMotor = Motor(MotorPort.B)
robot.addPart(rightMotor)
robot.addPart(leftMotor)

lightLeft = LightSensor(SensorPort.S3)
robot.addPart(lightLeft)

lightRight = LightSensor(SensorPort.S1)
robot.addPart(lightRight)

while not robot.isEscapeHit():
    leftVal = lightLeft.getValue()
    rightVal = lightRight.getValue() - offsetRight
    print("left: {0}, right: {1}".format(leftVal, rightVal))
    leftOffTable = leftVal < 300
    rightOffTable = rightVal < 300
    print("leftOffTable: {0}, rightOffTable: {1}".format(leftOffTable , rightOffTable ))
    if rightOffTable and leftOffTable:
        reverse(500)
        if(bool(random.getrandbits(1))):
            turnLeft(500)
        else:
            turnRight(500)
    elif rightOffTable:
        reverse(500)
        turnLeft(500)
    elif leftOffTable:
        reverse(500)
        turnRight(500)
    else:
        drive(50)
