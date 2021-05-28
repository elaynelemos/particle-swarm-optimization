from particle_swarm_optimization.helper import random_position
import numpy as np


class Particle():
    def __init__(self):
        self.current_position = random_position()
        self.best_position = self.current_position
        self.best_value = self.fitness()
        self.velocity = np.array([0,0])

    def __str__(self):
        return f'This particle position: {self.best_position}'

    def fitness(self):
        pos = self.current_position
        return 5 - 2*np.sin(3*((pos[0]/4)**2/np.pi + (pos[1]/5)**2/np.pi))

    def move(self):
        self.current_position = self.current_position + self.velocity

    def keep_best_position(self):
        fitness = self.fitness()
        if(self.best_value < fitness):
            self.best_value = fitness
            self.best_position = self.current_position
