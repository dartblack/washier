import gpiozero
from time import sleep

DR1 = gpiozero.DigitalOutputDevice(14)
PL1 = gpiozero.DigitalOutputDevice(15)

DR2 = gpiozero.DigitalOutputDevice(17)
PL2 = gpiozero.DigitalOutputDevice(18)


def top_construct(dr, limit, delay):
    if dr == 1:
        DR1.on()
        DR2.off()
    elif dr == 2:
        DR1.off()
        DR2.on()

    for i in range(limit):
        PL1.on()
        PL2.on()
        sleep(delay)
        PL1.off()
        PL2.off()
        sleep(delay)


while True:
    top_construct(1, 10000, 0.0001)
