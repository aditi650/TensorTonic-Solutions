import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    # req: list to array, result in float, no loop
    x = np.array(x, dtype = float)
    y = np.array(y, dtype = float)

    result = np.sqrt(np.sum(np.square(np.subtract(x,y))))
    return result