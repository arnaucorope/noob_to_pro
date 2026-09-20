import numpy as np

#Ejercicio 1 

temperatures = np.array([
    18.5, 21.2, 22.8, 30.1, 19.7,
    25.4, 17.9, 23.5, 28.0, 20.1
])

#1
higher_20 = temperatures[temperatures > 20]

#2
temp = temperatures[
        (temperatures >= 20) & (temperatures <= 25)
        ]

#3
temp = np.where(temperatures > 25)

#4
av = np.mean(temperatures)

#5
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

#6
result = np.sum(temperatures > 20)
