
import numpy as np
##question 1
def find_matrix_shape(matrix):
    return np.shape(matrix)

matrix = np.array([[2,3,4],[4,5,6]])
print(find_matrix_shape(matrix))