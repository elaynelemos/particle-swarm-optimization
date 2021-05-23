from particle_swarm_optimization.helper import random_position
import numpy as np


class Particle():
    def __init__(self):
        self.position = random_position()
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0])

    def __str__(self):
        return f'I am at {self.position} my pbest is {self.pbest_position}'

    def move(self):
        self.position = self.position + self.velocity
