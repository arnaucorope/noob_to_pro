# NumPy — Chuleta útil para IA / ML

## 1. Crear arrays

np.array()
→ crea un ndarray a partir de listas, tuplas u otros datos.

np.arange()
→ crea una secuencia de números con inicio, fin y paso.

np.linspace()
→ crea una cantidad concreta de valores repartidos entre dos límites.

np.zeros()
→ crea un array lleno de ceros.

np.ones()
→ crea un array lleno de unos.

np.full()
→ crea un array lleno del mismo valor que tú indiques.


## 2. Información del array

arr.shape
→ indica el tamaño de cada dimensión del array.

arr.ndim
→ indica cuántas dimensiones tiene el array.

arr.size
→ indica cuántos elementos contiene en total.

arr.dtype
→ indica el tipo de dato almacenado en el array.


## 3. Indexing y slicing

arr[i]
→ accede a un elemento o a una fila, según las dimensiones.

arr[i, j]
→ accede a una posición concreta en un array 2D.

arr[start:end]
→ selecciona desde start incluido hasta end excluido.

arr[start:end:step]
→ igual que slicing normal, pero avanzando con un paso determinado.

arr[:, 1]
→ selecciona toda la columna 1.

arr[1, :]
→ selecciona toda la fila 1.

arr[1:3, 0:2]
→ selecciona un bloque concreto de filas y columnas.


## 4. Cambiar forma

arr.reshape(...)
→ cambia la forma del array sin cambiar el número total de elementos.

arr.flatten()
→ aplana un array multidimensional y lo convierte en 1D.

arr.T
→ transpone el array: filas pasan a columnas y columnas a filas.


## 5. Cambiar tipo

arr.astype(int)
→ convierte los elementos a enteros.

arr.astype(float)
→ convierte los elementos a float.

arr.astype(bool)
→ convierte los elementos a booleanos.

arr.astype(...)
→ permite convertir el dtype del array a otro tipo compatible.


## 6. Operaciones vectorizadas

arr + 2
→ suma 2 a todos los elementos del array.

arr - 2
→ resta 2 a todos los elementos.

arr * 2
→ multiplica todos los elementos por 2.

arr / 2
→ divide todos los elementos entre 2.

a + b
→ suma dos arrays elemento a elemento si sus formas son compatibles.

a - b
→ resta dos arrays elemento a elemento.

a * b
→ multiplica dos arrays elemento a elemento.

a / b
→ divide dos arrays elemento a elemento.


## 7. Comparaciones y máscaras

arr > 10
→ crea un array booleano indicando qué valores son mayores que 10.

arr < 10
→ crea un array booleano indicando qué valores son menores que 10.

arr == 5
→ comprueba elemento a elemento cuáles son iguales a 5.

arr != 5
→ comprueba elemento a elemento cuáles son distintos de 5.

arr[arr > 10]
→ devuelve los valores que cumplen la condición.

arr[arr % 2 == 0]
→ devuelve solo los valores pares.

(arr > 10) & (arr < 20)
→ combina condiciones con AND.

(arr < 5) | (arr > 20)
→ combina condiciones con OR.


## 8. Buscar posiciones

np.where(condicion)
→ devuelve los índices donde la condición es verdadera.

np.where(arr > 10)
→ devuelve las posiciones de los elementos mayores que 10.


## 9. Agregaciones

np.sum(arr)
→ suma todos los elementos del array.

np.mean(arr)
→ calcula la media.

np.min(arr)
→ devuelve el valor mínimo.

np.max(arr)
→ devuelve el valor máximo.

np.std(arr)
→ calcula la desviación estándar.

arr.sum()
→ misma idea que np.sum(), llamada desde el propio ndarray.

arr.mean()
→ calcula la media desde el propio ndarray.

arr.min()
→ devuelve el mínimo.

arr.max()
→ devuelve el máximo.


## 10. Axis

axis=0
→ aplica una operación recorriendo las filas y devuelve resultado por columnas.

axis=1
→ aplica una operación recorriendo las columnas y devuelve resultado por filas.

arr.sum(axis=0)
→ suma cada columna por separado.

arr.mean(axis=1)
→ calcula la media de cada fila.

arr.std(axis=0)
→ calcula la desviación estándar de cada columna.


## 11. Producto escalar y matrices

np.dot(a, b)
→ calcula producto escalar o producto matricial según las dimensiones.

a @ b
→ realiza multiplicación matricial.

np.dot()
→ será importante para vectores, ML, embeddings y redes neuronales.


## 12. Norma de un vector

np.linalg.norm(v)
→ calcula la magnitud o longitud de un vector.


## 13. Unir arrays

np.concatenate((a, b))
→ une arrays a lo largo de un eje existente.

np.hstack((a, b))
→ une arrays horizontalmente, uno al lado del otro.

np.vstack((a, b))
→ une arrays verticalmente, uno debajo del otro.


## 14. Separar arrays

np.split(arr, n)
→ divide el array en n partes iguales; falla si no se puede dividir exactamente.

np.array_split(arr, n)
→ divide el array en n partes aunque no todas tengan el mismo tamaño.


## 15. Ordenar y buscar

np.sort(arr)
→ devuelve los elementos ordenados.

np.searchsorted(arr, x)
→ indica en qué posición debería insertarse x para mantener el array ordenado.


## 16. Copy y View

arr.copy()
→ crea otro array con datos independientes.

arr.view()
→ crea otro ndarray que comparte los mismos datos.

arr[1:4]
→ un slicing básico normalmente devuelve una view.

arr[arr > 10]
→ el boolean indexing normalmente devuelve una copia.


## 17. Otras funciones útiles

np.unique(arr)
→ devuelve los valores únicos sin repetidos.

np.argmax(arr)
→ devuelve el índice donde está el valor máximo.

np.argmin(arr)
→ devuelve el índice donde está el valor mínimo.

np.clip(arr, min, max)
→ limita los valores para que no bajen del mínimo ni superen el máximo.
