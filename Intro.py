import time
# Assuming you have a Robot class with motor control functions
# You need to replace these with actual motor control code for your robot

class Robot:
    def move_forward(self):
        print("Moving forward")

    def move_backward(self):
        print("Moving backward")

    def turn_left(self):
        print("Turning left")

    def turn_right(self):
        print("Turning right")

# Create an instance of the Robot class
robot = Robot()

# Main control loop
try:
    while True:
        robot.move_forward()
        time.sleep(1)

        robot.turn_left()
        time.sleep(0.5)

        robot.move_backward()
        time.sleep(1)

        robot.turn_right()
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program terminated by user")
  
