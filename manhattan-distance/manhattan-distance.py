import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    distance = np.subtract(x,y)
    abs_value = abs(distance)
    result = np.sum(abs_value)
    return result