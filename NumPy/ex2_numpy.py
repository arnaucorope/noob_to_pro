import numpy as np

players = np.array([
    [21, 180, 75],
    [25, 175, 68],
    [19, 190, 90],
    [31, 168, 72],
    [28, 182, 80]
])

#1
ages = players[:,0]

#2
heights = players[:,1]

#3
heights = players[2,:]

#4
heights = players[:, :2]

#5
last_players = players[2:,]

#6
mask = players[:, 2] > 75
result = players[mask]

#7
result_7 = result[:, 0]
