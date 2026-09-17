# NumPy — Chuleta básica

## Crear arrays

np.array()          → crear array
np.arange()         → secuencia de números
np.linspace()       → valores espaciados entre dos puntos
np.zeros()          → array de ceros
np.ones()           → array de unos
np.full()           → array relleno con un valor

## Información del array

arr.shape           → forma del array
arr.ndim            → número de dimensiones
arr.size            → número total de elementos
arr.dtype           → tipo de datos

## Cambiar estructura / tipo

arr.reshape()       → cambiar shape
arr.flatten()       → convertir a 1D
arr.astype()        → cambiar dtype

## Indexing / slicing

arr[i]              → elemento o fila
arr[i, j]           → posición en 2D
arr[start:end]      → slice
arr[start:end:step] → slice con saltos
arr[:, 1]           → columna completa
arr[1:3, 0:2]       → seleccionar bloque

## Filtrar

arr[arr > 10]           → valores mayores que 10
arr[arr < 10]           → valores menores que 10
arr[arr % 2 == 0]       → valores pares
np.where(condicion)     → índices donde se cumple la condición

&                       → AND
|                       → OR

## Operaciones

arr + n             → sumar a todos los elementos
arr - n             → restar
arr * n             → multiplicar
arr / n             → dividir

## Agregaciones

np.sum()            → suma
np.mean()           → media
np.min()            → mínimo
np.max()            → máximo
np.std()            → desviación estándar

## Unir arrays

np.concatenate()    → unir arrays
np.hstack()         → unir horizontalmente
np.vstack()         → unir verticalmente

## Separar arrays

np.split()          → dividir en partes iguales
np.array_split()    → dividir aunque no cuadre exactamente

## Buscar / ordenar

np.sort()           → ordenar
np.where()          → encontrar índices por condición
np.searchsorted()   → posición donde insertar manteniendo orden

## Copy / View

arr.copy()          → copia independiente
arr.view()          → nuevo ndarray compartiendo los mismos datos

slicing básico      → normalmente devuelve una view
boolean indexing    → normalmente devuelve una copy
