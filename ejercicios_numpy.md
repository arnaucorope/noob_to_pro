# Batería de ejercicios NumPy — Fundamentos para IA/ML

## Reglas

- Usar NumPy siempre que tenga sentido.
- Evitar `for` y list comprehensions.
- Antes de ejecutar algo, intentar predecir el resultado o el `shape`.
- Si no recuerdo un método, mirar primero mi chuleta.
- No usar Pandas.
- No buscar la solución del ejercicio.
- Puedo consultar documentación para recordar sintaxis.

---

# Nivel 1 — Manipular datos

## Ejercicio 1 — Sensores de temperatura

Un sensor ha registrado estas temperaturas:

```python
temperatures = np.array([
    18.5, 21.2, 22.8, 30.1, 19.7,
    25.4, 17.9, 23.5, 28.0, 20.1
])
```

Quiero:

1. Obtener únicamente las temperaturas mayores de `20`.
2. Obtener únicamente las temperaturas entre `20` y `25`, ambas incluidas.
3. Obtener las posiciones donde la temperatura supera `25`.
4. Calcular la temperatura media.
5. Obtener la temperatura máxima y mínima.
6. Averiguar cuántas temperaturas superan `20`.

No crear manualmente otro array con los resultados.

<details>
<summary>Pista</summary>

Piensa en máscaras booleanas, `where`, `mean`, `min`, `max` y `size`.

</details>

---

## Ejercicio 2 — Registro de jugadores

Tenemos:

```python
players = np.array([
    [21, 180, 75],
    [25, 175, 68],
    [19, 190, 90],
    [31, 168, 72],
    [28, 182, 80]
])
```

Cada fila representa:

```text
edad | altura_cm | peso_kg
```

Sin reconstruir arrays manualmente:

1. Obtener todas las edades.
2. Obtener todas las alturas.
3. Obtener solamente los datos del tercer jugador.
4. Obtener las dos primeras columnas de todos los jugadores.
5. Obtener los tres últimos jugadores.
6. Obtener los jugadores que pesan más de `75 kg`.
7. Obtener la edad de los jugadores que pesan más de `75 kg`.

Antes de ejecutar:

```python
players[:, 1]
```

escribe qué esperas que devuelva.

---

## Ejercicio 3 — El bloque escondido

Dada esta matriz:

```python
matrix = np.array([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])
```

Extrae utilizando slicing:

1. Las dos primeras filas.
2. Las tres últimas columnas.
3. El bloque:

```text
7   8   9
12 13 14
17 18 19
```

4. Todas las filas, pero solo las columnas pares según su índice.
5. Una fila sí y una fila no.
6. Una fila sí y una no, y además una columna sí y una no.

No escribir los números manualmente.

---

# Nivel 2 — Shape y reshape

## Ejercicio 4 — Telemetría plana

Recibes:

```python
data = np.arange(1, 25)
```

Representa 24 medidas tomadas por 4 sensores.

Cada sensor produjo 6 medidas.

1. Convierte `data` en una matriz de `4 x 6`.
2. Comprueba mentalmente el `shape` antes de ejecutarlo.
3. Obtén únicamente los datos del sensor 2.
4. Obtén la tercera medida de todos los sensores.
5. Vuelve a convertir la matriz completa en un array 1D.
6. Hazlo una vez con `reshape` y otra con `flatten`.
7. Explica con tus palabras qué diferencia conceptual existe entre ambos.

---

## Ejercicio 5 — ¿Qué reshape es válido?

Tienes:

```python
arr = np.arange(24)
```

Sin ejecutar primero, decide cuáles deberían funcionar:

```python
arr.reshape(6, 4)
arr.reshape(2, 12)
arr.reshape(3, 8)
arr.reshape(4, 7)
arr.reshape(2, 3, 4)
arr.reshape(24, 1)
arr.reshape(1, 24)
```

Para cada uno explica:

- válido / inválido
- qué `shape` tendría
- por qué

Después compruébalo ejecutando.

---

# Nivel 3 — Operar sobre arrays

## Ejercicio 6 — Aumentar precios

Tienes:

```python
prices = np.array([10, 25, 8, 40, 15], dtype=float)
```

Sin usar loops:

1. Sube todos los precios un `10%`.
2. Resta `2€` a todos los precios.
3. Duplica todos los precios.
4. Obtén un array booleano que indique qué precios son mayores que `20`.
5. Obtén únicamente esos precios.

La intención del ejercicio es acostumbrarte a:

```text
operación sobre array completo
```

en vez de:

```text
for elemento in array
```

---

## Ejercicio 7 — Pares, impares y divisibles

Crea un array con los números del `1` al `50`.

Sin loops:

1. Obtén todos los números pares.
2. Obtén todos los impares.
3. Obtén los divisibles entre `3`.
4. Obtén los números divisibles entre `3` Y entre `5`.
5. Obtén los números menores de `10` O mayores de `40`.
6. Obtén las posiciones de los números divisibles entre `7`.

---

# Nivel 4 — Axis

## Ejercicio 8 — Errores por programador

Tenemos el número de errores cometidos por 4 programadores durante 5 días:

```python
errors = np.array([
    [3, 1, 2, 0, 4],
    [1, 1, 0, 2, 1],
    [5, 3, 2, 4, 3],
    [0, 2, 1, 1, 0]
])
```

Cada:

```text
fila    = programador
columna = día
```

Sin loops:

1. Calcula el total de errores de cada programador.
2. Calcula el total de errores de cada día.
3. Calcula la media de errores de cada programador.
4. Calcula la media de errores de cada día.
5. Encuentra el programador con más errores totales.

Antes de escribir código responde:

```text
Para obtener un resultado por programador:

¿axis=0 o axis=1?
```

Después compruébalo.

---

## Ejercicio 9 — Notas de estudiantes

```python
grades = np.array([
    [7, 8, 6],
    [5, 6, 5],
    [9, 8, 10],
    [4, 5, 6],
    [8, 7, 9]
])
```

Cada fila es un alumno.

Cada columna es un examen.

Calcula:

1. La media de cada alumno.
2. La media de cada examen.
3. La nota máxima de cada alumno.
4. La nota mínima de cada examen.
5. Qué alumno tiene la mejor media.

No usar loops.

---

# Nivel 5 — Algo parecido a Machine Learning

## Ejercicio 10 — Predicciones de un modelo

Un modelo devuelve estas probabilidades:

```python
probabilities = np.array([
    0.91,
    0.20,
    0.67,
    0.49,
    0.51,
    0.10,
    0.88,
    0.35
])
```

Queremos considerar:

```text
>= 0.5 → clase 1
<  0.5 → clase 0
```

1. Crea un array booleano con las predicciones.
2. Convierte esas predicciones a `0` y `1`.
3. Guarda el resultado en `predictions`.

Después tenemos las respuestas reales:

```python
real = np.array([1, 0, 1, 0, 1, 1, 1, 0])
```

4. Compara `predictions` con `real`.
5. Obtén un array de `True/False` indicando qué predicciones fueron correctas.
6. Calcula qué proporción de predicciones fueron correctas.

Intenta pensar por qué la media de booleanos puede ser útil aquí.

---

# Nivel 6 — Buscar y ordenar

## Ejercicio 11 — Ranking

Tenemos unas puntuaciones ordenadas:

```python
scores = np.array([12, 18, 25, 31, 44, 52, 70])
```

Quieres añadir posteriormente una puntuación de:

```python
new_score = 39
```

Sin modificar todavía el array:

1. Averigua en qué posición debería entrar `39`.
2. Haz lo mismo con `10`.
3. Haz lo mismo con `100`.
4. Explica qué está devolviendo realmente `searchsorted`.

---

## Ejercicio 12 — Buscar condiciones

```python
values = np.array([15, 38, 41, 46, 17, 20, 33])
```

Utilizando `np.where()` encuentra los índices de:

1. Los valores pares.
2. Los valores impares.
3. Los valores mayores de `30`.
4. Los valores entre `20` y `40`.
5. Usa después esos índices para obtener los valores reales.

Quiero que diferencies claramente:

```text
where → posiciones

máscara booleana → valores
```

---

# Nivel 7 — Unir y separar

## Ejercicio 13 — Dos lotes de datos

Tenemos dos batches:

```python
batch_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

batch_b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])
```

Sin ejecutar primero:

### Caso A

Une uno debajo del otro.

Predice el `shape`.

### Caso B

Une uno al lado del otro.

Predice el `shape`.

### Caso C

Prueba a hacerlo utilizando `concatenate` y diferentes `axis`.

Explica qué significa cada resultado.

---

## Ejercicio 14 — Repartir trabajo

Hay 17 tareas:

```python
tasks = np.arange(1, 18)
```

Hay 4 trabajadores.

1. Divide las tareas entre los 4 de la forma más equilibrada posible.
2. Comprueba cuántas tareas recibe cada trabajador.
3. ¿Podrías utilizar `split()`?
4. ¿Por qué `array_split()` es más apropiado en este caso?

No repartirlas tú manualmente.

---

# Nivel 8 — Copy vs View

## Ejercicio 15 — El bug fantasma

Ejecuta:

```python
arr = np.array([10, 20, 30, 40, 50])

x = arr[1:4]
```

Antes de continuar:

1. ¿Qué contiene `x`?
2. ¿Crees que `x` es una copia o una view?

Ahora:

```python
x[0] = 999
```

3. Imprime `x`.
4. Imprime `arr`.
5. Explica qué ha ocurrido.

Después repite el experimento utilizando:

```python
x = arr.copy()
```

6. Modifica `x`.
7. Comprueba si cambia `arr`.
8. Explica la diferencia entre:

```text
x = arr
x = arr.view()
x = arr.copy()
```

No quiero una definición memorizada.

Quiero que lo compruebes ejecutando.

---

# Nivel 9 — Dtype

## Ejercicio 16 — Datos recibidos como texto

Recibes:

```python
data = np.array(["10", "20", "30", "40"])
```

1. Comprueba su `dtype`.
2. Intenta calcular matemáticamente su media.
3. Convierte los datos al tipo adecuado.
4. Calcula ahora la media.
5. Convierte posteriormente el array a `float`.
6. Explica qué problema resolvería `astype()` en un caso real como este.

---

# Nivel 10 — Mini reto final

## Ejercicio 17 — Dataset pequeño

Tenemos:

```python
dataset = np.array([
    [25, 180, 75, 7, 1],
    [31, 172, 68, 6, 0],
    [22, 190, 90, 8, 1],
    [40, 165, 70, 5, 0],
    [28, 178, 73, 7, 1],
    [35, 175, 85, 6, 0],
    [24, 182, 77, 8, 1],
    [29, 169, 65, 5, 0]
])
```

Las columnas representan:

```text
edad | altura | peso | horas_sueño | clase
```

### Parte A — Entender los datos

Sin ejecutar:

1. ¿Cuál crees que es el `shape`?
2. ¿Cuál es su `ndim`?
3. ¿Cuál es su `size`?

Después compruébalo.

### Parte B — Separar datos

Crea:

```text
X → las primeras 4 columnas
y → la última columna
```

No escribas los datos manualmente.

Comprueba los `shape` de `X` e `y`.

### Parte C — Analizar

Sin loops:

1. Media de edad.
2. Media de altura.
3. Media de peso.
4. Media de horas de sueño.
5. Media de cada una de las 4 columnas de `X` utilizando una sola operación.

### Parte D — Filtrar

Obtén:

1. Personas mayores de 30.
2. Personas que duermen 7 horas o más.
3. Personas mayores de 25 Y que duermen 7 horas o más.
4. Personas cuya `clase` sea `1`.

### Parte E — Pregunta importante

Sin escribir código:

Explica con tus palabras qué podría significar:

```python
X.shape == (8, 4)
```

en un problema de Machine Learning.

---

# Boss final — Todo mezclado

## Ejercicio 18 — Telemetría de drones

Tenemos mediciones de varios drones:

```python
telemetry = np.array([
    [101, 120, 42, 80],
    [102, 135, 50, 65],
    [103, 110, 38, 90],
    [104, 150, 55, 40],
    [105, 125, 45, 75],
    [106, 140, 60, 30]
])
```

Las columnas son:

```text
id | altura | velocidad | batería
```

Resuelve sin loops:

1. Obtener únicamente las alturas.
2. Obtener únicamente velocidad y batería.
3. Encontrar los drones con batería inferior al `50%`.
4. Obtener únicamente sus IDs.
5. Encontrar los drones que vuelan a más de `130` metros Y tienen batería superior al `50%`.
6. Calcular la altura media.
7. Calcular la media de cada columna numérica.
8. Encontrar el índice del drone con mayor velocidad.
9. Obtener todos los datos de ese drone utilizando ese índice.
10. Separar los primeros 3 drones de los últimos 3 utilizando slicing.
11. Volver a unirlos.
12. Convertir todos los datos a `float`.
13. Explicar qué operaciones del ejercicio han creado nuevas copias y cuáles podrían ser views.

---

# Checkpoint

Cuando termine los ejercicios debería poder explicar sin mirar:

- qué es `shape`
- qué es `ndim`
- qué es `size`
- qué es `dtype`
- cómo acceder a filas y columnas
- cómo hacer slicing
- cómo cambiar el shape
- cómo filtrar sin loops
- qué devuelve `where`
- cómo funcionan las operaciones vectorizadas
- qué significa `axis`
- cómo obtener medias, máximos, mínimos y sumas
- diferencia entre copy y view
- cómo unir y separar arrays
- por qué NumPy resulta útil cuando tenemos muchos datos
