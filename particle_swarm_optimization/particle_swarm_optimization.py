from particle_swarm_optimization.models.particle import Particle
from particle_swarm_optimization.models.swarm import Swarm

def swarm_main():
    W = 0.5
    c1 = 0.8
    c2 = 0.9

    n_iterations = 50
    target_error = 1e-6
    n_particles = 30

    search_space = Swarm(1, target_error, n_particles)
    particles_vector = [Particle() for _ in range(search_space.n_particles)]
    search_space.particles = particles_vector
    search_space.print_particles()

    iteration = 0
    while(iteration < n_iterations):
        search_space.set_pbest()
        search_space.set_gbest()

        if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
            break

        search_space.move_particles()
        iteration += 1

    print("The best solution is: ", search_space.gbest_position, " in n_iterations: ", iteration)
