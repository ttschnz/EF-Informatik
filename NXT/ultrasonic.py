from nxtrobot import *
#from simrobot import *


robot = LegoRobot("Terminator")
#gear = Gear()
#robot.addPart(gear)

ultrasonic = UltrasonicSensor(SensorPort.S1)
robot.addPart(ultrasonic)

while not robot.isEscapeHit():
    print(ultrasonic.getDistance())
    Tools.delay(500)

