import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    #first take a dot product: Multiply and then add them together, output should be a float value
    #Then calculate the length of a and b, divide both
    a = np.array(a, dtype = float)
    b = np.array(b, dtype = float)
    dot_product = np.dot(a,b)
    magnitude_a = np.sqrt(np.sum(a ** 2))
    magnitude_b = np.sqrt(np.sum(b ** 2))
    result = dot_product / (magnitude_a * magnitude_b + 1e-8)
    return float(result)
    
    
