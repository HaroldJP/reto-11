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