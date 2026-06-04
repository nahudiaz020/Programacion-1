'''
Hacer una funcion que reciba una lista, la ordene de manera ascendente (de menor a mayor), 
y retorne la misma ordenada
'''

mi_lista = [8, 1, 5, 6, 2, 10, 4, 9, 3, 7]

def ordenar_lista_asc(lista: list) -> list:
    """
    Ordena una lista de números de manera ascendente 
    (de menor a mayor).

    La función recorre la lista comparando cada elemento
    con los siguientes y, en caso de ser necesario,
    intercambia sus posiciones.


    Args:
        lista (list): Lista de números a ordenar.

    Returns:
        list: Lista ordenada de manera ascendente.
    """
    print("LISTA ORIGINAL")

    for i in range(len(lista)):
        print(f"indice: {i} - dato: {lista[i]}")
    
    for i in range(len(lista)-1):
        for j in range((i+1), len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista

lista_ordenada = ordenar_lista_asc(mi_lista)           

print("LISTA ORDENADA DE MANERA ASCENDENTE")

for i in range(len(lista_ordenada)):
    print(f"indice: {i} - dato: {lista_ordenada[i]}")


