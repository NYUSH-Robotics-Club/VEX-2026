from vex import *

# Initialize brain and controller
brain = Brain()
controller_1 = Controller()

# Define drive motors
L1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
L2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
L3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
L4 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)

R1 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
R2 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)
R3 = Motor(Ports.PORT7, GearSetting.RATIO_6_1, True)
R4 = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)

# Group left and right motors
left_drive = MotorGroup(L1, L2, L3, L4)
right_drive = MotorGroup(R1, R2, R3, R4)

# User control (driver control mode)
def usercontrol():
    while True:
        # Read joystick input
        forward = controller_1.axis3.position()   # Left stick vertical axis
        turn = controller_1.axis1.position()      # Right stick horizontal axis

        # Arcade drive calculation
        left_speed = forward + turn
        right_speed = forward - turn

        # Clamp values between -100 and 100
        left_speed = max(-100, min(100, left_speed))
        right_speed = max(-100, min(100, right_speed))

        # Spin motors
        left_drive.spin(FORWARD, left_speed, PERCENT)
        right_drive.spin(FORWARD, right_speed, PERCENT)

        # Small delay to prevent CPU overload
        wait(20, MSEC)

# Main program entry
def main():
    brain.screen.print("Driver control started")
    usercontrol()

main()