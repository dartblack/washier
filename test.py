import serial
import time

port = serial.Serial("/dev/rfcomm0", baudrate=38400)

while True:
    port.write(str(1))
    rcv = port.readline()
    if rcv:
        print(rcv)
    time.sleep(3)
