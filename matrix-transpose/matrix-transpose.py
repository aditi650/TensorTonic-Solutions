import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    A = np.array(A) #Converting all the python list into numpy array
    N,M = A.shape #Tuple unpacking
    B = np.zeros((M,N))

    #We start a for loop to exchange the positions 
    for i in range(N):
        for j in range (M):
            B[j][i] = A[i][j]

    return B