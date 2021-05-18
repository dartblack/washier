from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time
from Sensors import DistanceSensor

trigger = DigitalOutputDevice(20)

echos = {
    "1.1": DigitalInputDevice(5),
    "1.2": DigitalInputDevice(9),
    "1.3": DigitalInputDevice(27),
    "1.4": DigitalInputDevice(16),
    "1.5": DigitalInputDevice(12),
    "1.6": DigitalInputDevice(2)
}
distanceSensors = DistanceSensor.Distance(trigger, echos)

print("Start")
while True:
    dists = distanceSensors.get_distances()
    print(dists)
    time.sleep(1)
