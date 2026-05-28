def inicializar_matriz(cantidad_filas : int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz

def cargar_matriz_secuencialmente(matriz:list):
    # Agregar las validaciones/retorno que sean necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))


mi_matriz = inicializar_matriz(2, 4, 0)

cargar_matriz_secuencialmente(mi_matriz)
print(mi_matriz)

