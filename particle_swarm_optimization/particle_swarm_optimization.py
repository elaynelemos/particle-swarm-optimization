from particle_swarm_optimization.models.particle import Particle
from particle_swarm_optimization.models.swarm import Swarm

def optimize(target: float, target_error: float, iterations: int, swarm_size: int):
    inertia = lambda tmax, t, ws=0.9, we=0.4: (ws - we )*(tmax - t)/tmax + we
    swarm = Swarm(target, target_error, swarm_size)
    particles = [Particle() for _ in range(swarm.swarm_size)]
    swarm.particles = particles
    swarm.print_particles()
    print()

    iteration = 0
    while iteration < iterations:
        swarm.set_best_position()

        if abs(swarm.best_value - swarm.target) <= swarm.target_error:
            break

        swarm.move_particles(inertia(iterations, iteration))
        iteration += 1

    print(f'\nThe best position is: {swarm.best_position} = {swarm.best_value}'
          f'\nReached in {iteration} iterations')
