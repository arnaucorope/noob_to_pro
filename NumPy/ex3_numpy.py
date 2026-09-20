import numpy as np

matrix = np.array([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

#1
first_line = matrix[0:2, :]

#2
last_3_col = matrix[:, 2:]

#3
block = matrix[1:4, 1:4]

#4
result_4 = matrix[:, ::2]

#5
result_5 = matrix[::2,:]

#6
resutl_6 = matrix[::2, ::2]
