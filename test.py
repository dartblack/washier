from gpiozero import OutputDevice
from gpiozero import Button

from Motors.TopMotor import TopMotor

move_forward_button = Button(10)
move_back_button = Button(11)

top_motor = {
    "DR1": OutputDevice(14),
    "PL1": OutputDevice(15),
    "DR2": OutputDevice(17),
    "PL2": OutputDevice(18)
}

top_motor_obj = TopMotor(top_motor)

while True:
    if move_forward_button.is_active:
        top_motor_obj.direction(1)
        top_motor_obj.move(0.001)

    if move_back_button.is_active:
        top_motor_obj.direction(2)
        top_motor_obj.move(0.001)
