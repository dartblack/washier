from gpiozero import OutputDevice
from gpiozero import InputDevice
from time import sleep

DR1 = OutputDevice(14)
PL1 = OutputDevice(15)

DR2 = OutputDevice(17)
PL2 = OutputDevice(18)

sensor = {
    "sensor1": InputDevice(27)
}


def read_distance_sensor(index):
    return sensor[index].value


def top_construct(dr, duration=5000, delay=0.0000001):
    if dr == 1:
        DR1.on()
        DR2.off()
    elif dr == 2:
        DR1.off()
        DR2.on()

    for i in range(duration):
        PL1.on()
        PL2.on()
        sleep(delay)
        PL1.off()
        PL2.off()
        sleep(delay)


print("read distance")
sleep(1)
distance = read_distance_sensor("sensor1")
sleep(1)
print("distance: " + distance)
