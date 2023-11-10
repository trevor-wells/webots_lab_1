"""epuck_go_forward controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, LightSensor

# create the Robot instance.
robot = Robot()

#set constants
TIME_STEP = 64
MAX_SPEED = 6.28

#get the motor devices
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

ls = []
ls_names = ['ls0', 'ls1', 'ls2', 'ls3', 'ls4', 'ls5', 'ls6', 'ls7']
values = []

for name in ls_names:
    ls.append(robot.getDevice(name))
for sensor in ls:
    sensor.enable(32) 

#set target position of the motors to infinity (speed control)
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

#set motor speeds to 10% of MAX_SPEED
leftMotor.setVelocity(6.28)
rightMotor.setVelocity(6.28)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    for sensor in ls:
        values.append(sensor.getValue())
        print(values[0])
    
    leftMotor.setVelocity(values[7]/1000.0)
    rightMotor.setVelocity(values[0]/1000.0)
    
    values.clear()
    
    
