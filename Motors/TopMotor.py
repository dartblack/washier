from time import sleep


class TopMotor:
    def __init__(self, motor):
        self.motor = motor

    def direction(self, dir):
        if dir == 1:
            self.motor["DR1"].on()
            self.motor["DR2"].off()
        elif dir == 2:
            self.motor["DR1"].off()
            self.motor["DR2"].on()

    def move(self, delay):
        self.motor["PL1"].on()
        self.motor["PL2"].on()
        sleep(delay)
        self.motor["PL1"].off()
        self.motor["PL2"].off()
        sleep(delay)

    def control(self, dir, duration=10, delay=0.001):
        self.direction(dir)
        for i in range(duration):
            self.move(delay)
