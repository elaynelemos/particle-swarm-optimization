import random
import numpy as np


def random_position(min=-5.0, max=5.0):
    pos = lambda : min + (max-min)*random.random()
    return np.array([pos(), pos()])
