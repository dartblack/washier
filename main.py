from gpiozero import OutputDevice
from gpiozero import DistanceSensor
from time import sleep

top_motor = {
    "DR1": OutputDevice(14),
    "PL1": OutputDevice(15),
    "DR2": OutputDevice(17),
    "PL2": OutputDevice(18)
}

DR1 = OutputDevice(14)
PL1 = OutputDevice(15)

DR2 = OutputDevice(17)
PL2 = OutputDevice(18)

sensor = {
    "sensor1": DistanceSensor(echo=27, trigger=22, queue_len=30, max_distance=4)
}


def read_distance_sensor(index):
    return sensor[index].distance * 100


def top_motor_control(dr, duration=1000, delay=0.0000001):
    if dr == 1:
        top_motor["DR1"].on()
        top_motor["DR2"].off()
    elif dr == 2:
        top_motor["DR1"].off()
        top_motor["DR2"].on()

    for i in range(duration):
        top_motor["PL1"].on()
        top_motor["PL2"].on()
        sleep(delay)
        top_motor["PL1"].off()
        top_motor["PL2"].off()
        sleep(delay)


print("read distance")
sleep(1)
distance = read_distance_sensor("sensor1")
sleep(1)
print(distance)
