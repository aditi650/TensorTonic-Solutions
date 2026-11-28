import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    # req: list to array, result in float, no loop
    x = np.array(x, dtype = float)
    y = np.array(y, dtype = float)
    difference_vector = np.subtract(x,y)
    square_vector = np.square(difference_vector)
    adding_squared_vector = np.sum(square_vector)
    result = np.sqrt(adding_squared_vector)
    return result
    