# DESAFIO CUADRADO MAGICO
from Biblioteca.Funciones import *

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






filas = input("Ingrese cantidad de filas deseada: ")
columnas = input("Ingrese cantidad de columnas deseada: ")

if validar_num(filas) and validar_num(columnas):    
    mi_matriz = inicializar_matriz(filas, columnas, 0)

else:
    print("Ingrese numeros enteros")

cargar_matriz_secuencialmente(mi_matriz)
print(mi_matriz)
