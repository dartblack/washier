import time


class Distance:
    def __init__(self, trigger, echos):
        self.trigger = trigger
        self.trigger.off()
        self.echos = echos
        self.startTime = {}
        self.stopTime = {}
        self.distances = {}
        self.count = len(echos)
        self.keys = echos.keys()
        for k in self.keys:
            self.startTime[k] = 0
            self.stopTime[k] = 0
            self.distances[k] = 0

    def load(self):
        for k in self.keys:
            self.startTime[k] = 0
            self.stopTime[k] = 0
            self.distances[k] = 0

        self.trigger.on()
        time.sleep(0.00001)
        self.trigger.off()

        count = self.count
        while True:
            for k in self.keys:
                print(self.echos[k].value)
                if self.echos[k].value == 0 and self.startTime[k] == 0:
                    self.startTime[k] = time.time()
                    count = count - 1
            print(self.startTime)
            if count == 0:
                break

        count2 = self.count
        while True:
            print('start end')
            for k in self.keys:
                print(self.echos[k].value)
                if self.echos[k].value == 1 and self.stopTime[k] == 0:
                    self.stopTime[k] = time.time()
                    count2 = count2 - 1
            print(self.stopTime)
            if count2 == 0:
                break

        for k in self.keys:
            TimeElapsed = self.stopTime[k] - self.startTime[k]
            self.distances[k] = round(TimeElapsed * 17150, 2)

    def get_distances(self):
        self.load()
        return self.distances
