import numpy as np


class Population:
    def __init__(self):
        # Types of humans and initial values:
        self.healthy = 11000000
        self.dead = 0
        self.recovered = 0
        self.sick = 0
        self.incubating = np.zeros(5)
