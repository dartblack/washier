from gpiozero import OutputDevice
from gpiozero import DistanceSensor
from gpiozero import DigitalInputDevice
from time import sleep

direct_width = 600
side_width = 300
kercher_distance = 30
pulse_to_cm = 10

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

side_motor = {
    "DR": OutputDevice(24),
    "PL": OutputDevice(25)
}

safe_sensors = {
    "1.1": DigitalInputDevice(5),
    "1.2": DigitalInputDevice(6),
    "2.1": DigitalInputDevice(12),
    "2.2": DigitalInputDevice(13),
    "3.1": DigitalInputDevice(19),
    "3.2": DigitalInputDevice(20)
}


# sensor = {
#     "top_sensor": DistanceSensor(echo=27, trigger=22, queue_len=30, max_distance=4),
#     "back_sensor": DistanceSensor(echo=23, trigger=24, queue_len=30, max_distance=4),
#     "left_sensor": DistanceSensor(echo=5, trigger=6, queue_len=30, max_distance=4),
#     "right_sensor": DistanceSensor(echo=13, trigger=19, queue_len=30, max_distance=4)
# }
#
#
# def read_distance_sensor(index):
#     return sensor[index].distance * 100


def top_motor_control(dr, duration=10, delay=0.001):
    check = safe_sensors["1.1"]
    if dr == 1:
        top_motor["DR1"].on()
        top_motor["DR2"].off()
    elif dr == 2:
        top_motor["DR1"].off()
        top_motor["DR2"].on()
        check = safe_sensors["1.2"]

    for i in range(duration):
        # if check.is_active:
        #     break
        top_motor["PL1"].on()
        top_motor["PL2"].on()
        sleep(delay)
        top_motor["PL1"].off()
        top_motor["PL2"].off()
        sleep(delay)


def middle_motor_control(dr, duration=10, delay=0.001):
    check = safe_sensors["2.1"]
    if dr == 1:
        middle_motor["DR"].on()
    elif dr == 2:
        middle_motor["DR"].off()
        check = safe_sensors["2.2"]

    for i in range(duration):
        # if check.is_active:
        #     break
        middle_motor["PL"].on()
        sleep(delay)
        middle_motor["PL"].off()
        sleep(delay)


def side_motor_control(dr, duration=10, delay=0.001):
    check = safe_sensors["3.1"]
    if dr == 1:
        side_motor["DR"].on()
    elif dr == 2:
        side_motor["DR"].off()
        check = safe_sensors["3.2"]

    for i in range(duration):
        if check.is_active:
            break
        side_motor["PL"].on()
        sleep(delay)
        side_motor["PL"].off()
        sleep(delay)


def construct_calibration():
    top_motor_control(1, 1000000)
    middle_motor_control(1, 1000000)
    side_motor_control(1, 1000000)


print("start...")
middle_motor_control(1, 100000, 0.001)

# top_distance = read_distance_sensor("top_sensor")
# back_distance = read_distance_sensor("back_sensor")
# car_direct_width = direct_width - top_distance - back_distance
#
# left_distance = read_distance_sensor("left_sensor")
# right_distance = read_distance_sensor("right_sensor")
# car_side_width = side_width - left_distance - right_distance
# print("Top distance: " + str(top_distance) + " | Back distance: " + str(back_distance))
# print("Car direct width: " + str(car_direct_width) + " | Car side width: " + str(car_side_width))
#
# print("--------------------------------------")
#
# print("Move to start positions")
# start_position_move = (top_distance - kercher_distance) * pulse_to_cm
# top_motor_control(1, start_position_move)
#
# top_motor_move = (car_direct_width + kercher_distance * 2) * pulse_to_cm
# top_motor_control(1, top_motor_move)
# top_motor_control(2, top_motor_move)
#
# top_motor_control(2, start_position_move)
