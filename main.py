from gpiozero import OutputDevice
from time import sleep

DR1 = OutputDevice(14)
PL1 = OutputDevice(15)

DR2 = OutputDevice(17)
PL2 = OutputDevice(18)


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


print("Start move forward")
top_construct(1, 100000)
print("End move")
