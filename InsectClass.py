import random

class Insect:

    # def __init__(self):
    #     self.wings = 2
    #     self.legs = 4
    #     self.flight = 0

    def __init__(self, wings, legs):
        self.wings = wings
        self.legs = legs
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight