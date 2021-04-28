from time import sleep


class Motor:
    def __init__(self, motor):
        self.motor = motor

    def direction(self, dir):
        if dir == 1:
            self.motor["DR"].on()
        elif dir == 2:
            self.motor["DR"].off()

    def move(self, delay):
        self.motor["PL"].on()
        sleep(delay)
        self.motor["PL"].off()
        sleep(delay)

    def control(self, dir, duration=10, delay=0.001):
        self.direction(dir)
        for i in range(duration):
            self.move(delay)
