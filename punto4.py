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