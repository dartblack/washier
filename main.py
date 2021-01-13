from gpiozero import OutputDevice
from gpiozero import PWMOutputDevice
from time import sleep

DR1 = OutputDevice(14)
PL1 = PWMOutputDevice(15, True, 0, 100000)

DR2 = OutputDevice(17)
PL2 = PWMOutputDevice(18, True, 0, 100000)


def top_construct(dr, duration=5000, delay=0.00001):
    if dr == 1:
        DR1.on()
        DR2.off()
    elif dr == 2:
        DR1.off()
        DR2.on()

    PL1.pulse(delay, delay, duration)
    PL2.pulse(delay, delay, duration)


while True:
    print("Start move forward")
    top_construct(1)
    print("End move")

    sleep(5)

    print("Start move back")
    top_construct(2)
    print("End move")
