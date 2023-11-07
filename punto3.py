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