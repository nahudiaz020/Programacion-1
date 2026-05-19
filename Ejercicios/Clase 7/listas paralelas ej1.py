'''
Hacer una funcion que reciba una lista y el elemento a buscar, y retorne el indice del elemento encontrado. 
Si no encuentra el elemento, retornara -1
'''

def buscar_elemento(lista: str, elemento: int) -> int:
    """
    Busca un elemento dentro de una lista y retorna su índice.

    La función recorre la lista verificando si el elemento
    recibido se encuentra dentro de ella.

    Args:
        lista (str): Lista donde se realizara la busqueda.
        elemento (int): Elemento a buascar dentro de la lista.

    Returns:
        int: Índice del elemento encontrado.
             Retorna -1 si el elemento no existe en la lista.
    """
    retorno = -1
    for i in range (len(lista)):
        if lista[i] == elemento:
            retorno = i
            break
    
    return retorno

lista = [1, 2, 3, 4, 5]

dato_a_buscar = int(input(("buscar: ")))
indice = buscar_elemento(lista, dato_a_buscar)
print(indice)