import numpy as np

data = np.arange(1, 25)

#1
data = data.reshape(4, 6)

#2 -> reshape modifica el array en fils, columnas.

#3
sensor_2 = data[1,:]

#4
third_col = data[:, 2]

#5
data = data.flatten()

#6 
data = data.flatten()
data = data.reshape(-1)

#7
#flatten se usa para pasarla directamente a 1d
#reshape se usa para darle las dimensiones que
#quieras aunque tiene que cuadrar el size con los espacios


