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