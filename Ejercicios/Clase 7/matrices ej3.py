'''
Hacer dos funciones, imprimir_matriz e imprimir_elemento(ya existe)
'''

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            imprimir_elemento(elemento)
        print()

def imprimir_elemento(elemento):
    print(elemento, end=" ")


mi_matriz = [[5,5,5], [5,5,5]]
imprimir_matriz(mi_matriz)