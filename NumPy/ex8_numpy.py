errors = np.array([
    [3, 1, 2, 0, 4],
    [1, 1, 0, 2, 1],
    [5, 3, 2, 4, 3],
    [0, 2, 1, 1, 0]
])

#1
each_error = errors.sum(axis=1)

#2
day = errors.sum(axis=0)

#3
mean = errors.mean(axis=1)

#4
mean = errors.mean(axis=0)

#5
max_errors = np.argmax(each_error)
