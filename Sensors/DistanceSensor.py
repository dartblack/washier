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

        end = True
        while end:
            end = True
            for k in self.keys:
                if self.echos[k].value == 0:
                    end = False
                    self.startTime[k] = time.time()

        end = True
        while end:
            end = True
            for k in self.keys:
                if self.echos[k].value == 1:
                    end = False
                    self.stopTime[k] = time.time()

        for k in self.keys:
            TimeElapsed = self.stopTime[k] - self.startTime[k]
            self.distances[k] = round(TimeElapsed * 17150, 2)

    def get_distances(self):
        self.load()
        return self.distances
