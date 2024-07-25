#to access numpy open it through anaconda
import numpy as np

A= np.array([
    [2, 5, 7],
    [1, 2, 4],
    [7, 9, 2]
])

B = np.array([
    [1, 2, 3],
    [5, 5, 5],
    [9, 8, 0]
])

C = A/B+2
print(C[0,2])
