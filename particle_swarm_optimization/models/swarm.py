from particle_swarm_optimization.helper import random_position
import random


class Swarm():
    def __init__(self, target, target_error, swarm_size):
        self.target = target
        self.target_error = target_error
        self.swarm_size = swarm_size
        self.particles = []
        self.best_value = -float('inf')
        self.best_position = random_position()

    def print_particles(self):
        for particle in self.particles:
            print(particle)

    def __str__(self):
        return f'Current best shot: {self.best_position} = {self.best_value}'

    def set_best_position(self):
        for particle in self.particles:
            best_fitness_cadidate = particle.fitness()
            if(self.best_value < best_fitness_cadidate):
                self.best_value = best_fitness_cadidate
                self.best_position = particle.current_position

        print(self)

    def move_particles(self, W, c1, c2):
        for particle in self.particles:
            new_velocity = (W*particle.velocity) \
                           + (c1*random.random()) * (particle.best_position - particle.current_position) \
                           + (c2*random.random()) * (self.best_position - particle.current_position)

            particle.velocity = new_velocity
            particle.move()
            particle.keep_best_position()
