import numpy as np

def dot_product(x: list, y: list) -> float:
    product = np.multiply(x,y)
    result = np.sum(product)
    return result