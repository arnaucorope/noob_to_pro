import numpy as np

arr = np.arange(1, 51)

#1
pares = arr[arr % 2 == 0]

#2
impares = arr[arr % 2 != 0]

#3
divisibles = arr[arr % 3 == 0]

#4
divisibles = arr[(arr % 3 == 0) & (arr % 5 == 0)]

#5
numbers = arr[(arr < 10) | (arr > 40)]

#6
seven_div = np.where(arr % 7 == 0)
