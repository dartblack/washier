from gpiozero import OutputDevice
from gpiozero import Button

from Motors.Motor import Motor
from Motors.TopMotor import TopMotor

move_forward_button = Button(19)
move_back_button = Button(26)

move_left_button = Button(20)
move_right_button = Button(21)

top_motor = {
    "DR1": OutputDevice(14),
    "PL1": OutputDevice(15),
    "DR2": OutputDevice(17),
    "PL2": OutputDevice(18)
}

middle_motor = {
    "DR": OutputDevice(22),
    "PL": OutputDevice(23)
}

top_motor_obj = TopMotor(top_motor)
middle_motor_obj = Motor(middle_motor)

while True:
    if move_forward_button.is_active:
        top_motor_obj.direction(1)
        top_motor_obj.move(0.001)

    if move_back_button.is_active:
        top_motor_obj.direction(2)
        top_motor_obj.move(0.001)

    if move_left_button.is_active:
        middle_motor_obj.direction(1)
        middle_motor_obj.move(0.0005)

    if move_right_button.is_active:
        middle_motor_obj.direction(2)
        middle_motor_obj.move(0.0005)
