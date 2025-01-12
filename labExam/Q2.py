import numpy as np

def compute_cross_product(array1, array2):
    return np.cross(array1, array2)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(compute_cross_product(array1, array2)) 