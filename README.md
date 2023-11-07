# reto-11

### Punto 1

Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

# Pedimos al usuario que ingrese las dimensiones de las matrices
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Creamos las matrices
print("Ingrese los valores de la primera matriz:")
matriz1 = crear_matriz(filas, columnas)

print("Ingrese los valores de la segunda matriz:")
matriz2 = crear_matriz(filas, columnas)

# Sumamos las matrices
resultado = sumar_matrices(matriz1, matriz2)

# Imprimimos el resultado
print("La suma de las matrices es:")
for fila in resultado:
    print(fila)
```

### Punto 2

Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
def multiplicar_matrices(matriz1, matriz2):
    # Validar que las matrices se puedan multiplicar
    if len(matriz1[0]) != len(matriz2):
        print("Las matrices no se pueden multiplicar")
        return None
    
    # Crear una matriz vacía para almacenar el resultado
    resultado = [[0 for j in range(len(matriz2[0]))] for i in range(len(matriz1))]
    
    # Realizar la multiplicación de las matrices
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

# Pedir al usuario que ingrese las matrices
matriz1 = []
matriz2 = []

filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))

for i in range(filas1):
    fila = []
    for j in range(columnas1):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la primera matriz: "))
        fila.append(valor)
    matriz1.append(fila)

filas2 = int(input("Ingrese el número de filas de la segunda matriz: "))
columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))

for i in range(filas2):
    fila = []
    for j in range(columnas2):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la segunda matriz: "))
        fila.append(valor)
    matriz2.append(fila)

# Multiplicar las matrices y mostrar el resultado
resultado = multiplicar_matrices(matriz1, matriz2)

if resultado is not None:
    print("El resultado de la multiplicación es:")
    for fila in resultado:
        print(fila)
```

### Punto 3

Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
def obtener_matriz_transpuesta(matriz):
    # Validar que la matriz no esté vacía
    if matriz is None or len(matriz) == 0:
        return None

    # Validar que la matriz tenga filas y columnas
    filas = len(matriz)
    if filas == 0:
        return None
    columnas = len(matriz[0])
    if columnas == 0:
        return None

    # Validar que la matriz sea rectangular
    for fila in matriz:
        if len(fila) != columnas:
            return None

    # Obtener la matriz transpuesta
    matriz_transpuesta = []
    for j in range(columnas):
        fila_transpuesta = []
        for i in range(filas):
            fila_transpuesta.append(matriz[i][j])
        matriz_transpuesta.append(fila_transpuesta)

    return matriz_transpuesta

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_transpuesta = obtener_matriz_transpuesta(matriz)
print("La matriz transpuesta es")
print(matriz_transpuesta)
```

### Punto 4

Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
def sumar_columna(matriz, columna):
    # Validar que la matriz no esté vacía
    if matriz is None or len(matriz) == 0:
        return None

    # Validar que la columna exista en la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    if columna < 0 or columna >= columnas:
        return None

    # Sumar los elementos de la columna
    suma = 0
    for fila in matriz:
        suma += fila[columna]

    return suma

# Pedir al usuario que ingrese la matriz y la columna a sumar
matriz = []
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la matriz: "))
        fila.append(valor)
    matriz.append(fila)

columna = int(input("Ingrese el número de la columna a sumar (0-indexed): "))

# Sumar los elementos de la columna y mostrar el resultado
suma = sumar_columna(matriz, columna)

if suma is not None:
    print(f"La suma de la columna {columna} es: {suma}")
else:
    print("La columna ingresada no existe en la matriz")
```

### Punto 5

Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
def sumar_fila(matriz, fila):
    # Validar que la matriz no esté vacía
    if matriz is None or len(matriz) == 0:
        return None

    # Validar que la fila exista en la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    if fila < 0 or fila >= filas:
        return None

    # Sumar los elementos de la fila
    suma = 0
    for columna in range(columnas):
        suma += matriz[fila][columna]

    return suma

# Pedir al usuario que ingrese la matriz y la fila a sumar
matriz = []
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}) de la matriz: "))
        fila.append(valor)
    matriz.append(fila)

fila = int(input("Ingrese el número de la fila a sumar (0-indexed): "))

# Sumar los elementos de la fila y mostrar el resultado
suma = sumar_fila(matriz, fila)

if suma is not None:
    print(f"La suma de la fila {fila} es: {suma}")
else:
    print("La fila ingresada no existe en la matriz")
```
