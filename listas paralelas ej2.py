'''
Hacer una funcion que reciba una lista de numeros, 
calcule el promedio y lo  retorne.
'''

def calcular_promedio(lista: list) -> float:
    """
    Calcula el promedio de una lista de números.

    La función suma todos los elementos de la lista
    y divide el total por la cantidad de elementos.

    Args:
        lista (list): Lista de números.

    Returns:
        float: Promedio de la lista de números.
    """
    suma = 0

    for numero in lista:
        suma += numero

    promedio = suma / len(lista)

    return promedio



mi_lista = [5,8,2,3,4]
promedio = calcular_promedio(mi_lista)
print(f"Promedio: {promedio:}")