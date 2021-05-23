import random
import numpy as np


def random_position(min=-3.0, max=3.0):
    pos = lambda : min + (max-min)*random.random()
    return np.array([pos(), pos()])
