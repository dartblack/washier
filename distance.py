from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time

trigger = DigitalOutputDevice(20)

echos = {
    "1.1": DigitalInputDevice(5),
    "1.2": DigitalInputDevice(9),
    "1.3": DigitalInputDevice(27),
    "1.4": DigitalInputDevice(16),
    "1.5": DigitalInputDevice(12),
    "1.6": DigitalInputDevice(2)
}


def distance():
    trigger.on()
    time.sleep(0.00001)
    trigger.off()

    startTime = {
        "1.1": 0,
        "1.2": 0,
        "1.3": 0,
        "1.4": 0,
        "1.5": 0,
        "1.6": 0
    }
    stopTime = {
        "1.1": 0,
        "1.2": 0,
        "1.3": 0,
        "1.4": 0,
        "1.5": 0,
        "1.6": 0
    }

    distances = {
        "1.1": 0,
        "1.2": 0,
        "1.3": 0,
        "1.4": 0,
        "1.5": 0,
        "1.6": 0
    }

    # save StartTime
    count = len(echos)
    while True:
        for k in echos.keys():
            if echos[k].value == 0 and startTime[k] == 0:
                startTime[k] = time.time()
                count = count - 1
        if count == 0:
            break

    count = len(echos)
    while True:
        for k in echos.keys():
            if echos[k].value == 1 and startTime[k] == 0:
                stopTime[k] = time.time()
                count = count - 1
        if count == 0:
            break

    for k in stopTime.keys():
        TimeElapsed = stopTime[k] - startTime[k]
        distances[k] = (TimeElapsed * 34300) / 2

    return distances


while True:
    dists = distance()
    for key in echos.keys():
        print("Measured Distance = ", dists[key], "cm | Sensor: ", key)
    time.sleep(1)
