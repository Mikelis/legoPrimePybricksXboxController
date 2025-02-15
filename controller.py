from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port, Button, Color
from pybricks.pupdevices import Motor
from pybricks.robotics import Car
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

xbox = XboxController()
hub = PrimeHub()

print("Waiting for Xbox Controller...")

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
extra_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
MAX_ANGLE = 55
# Jingle Bells melody
jingle_bells = [
    "E4/4", "E4/4", "E4/2",  # E E E (longer)
    "E4/4", "E4/4", "E4/2",  # E E E (longer)
    "E4/4", "G4/4", "C4/4", "D4/4",  # E G C D
    "E4/2"  # E (longer)
]

wait(1000)  # Allow time for connection

while True:
    try:
        left_stick = xbox.joystick_left()
        triggers = xbox.triggers()
        buttons = xbox.buttons.pressed()

        print(buttons)
        if Button.A in buttons:
            hub.speaker.beep()  # Play sound
        elif Button.B in buttons:
            hub.light.on(Color.VIOLET)
        else:
            hub.light.on(Color.GRAY)      

        # print(f"Left Stick: {left_stick}, Triggers: {triggers}")  # Debugging output

        speed = triggers[1] - triggers[0]
        steer = left_stick[0]
        target_angle = (steer * MAX_ANGLE) / 100
        left_motor.dc(speed)
        right_motor.dc(-speed)  
        extra_motor.track_target(-target_angle)


    except Exception as e:
        print(f"Controller error: {e}")

    wait(50)
