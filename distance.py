from gpiozero import DigitalOutputDevice
from gpiozero import InputDevice
import time

from Sensors.DistanceSensor import Distance

trigger = DigitalOutputDevice(6)

echos = {
    "1.1": InputDevice(5),
    "1.2": InputDevice(9),
    "1.3": InputDevice(27),
    "1.4": InputDevice(16),
    "1.5": InputDevice(12),
    "1.6": InputDevice(2)
}
distanceSensors = Distance(trigger, echos)

print("Start")
while True:
    dists = distanceSensors.get_distances()
    print(dists)
    time.sleep(1)
