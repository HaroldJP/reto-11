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