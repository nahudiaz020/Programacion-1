'''
Hacer una funcion que reciba una lista, y un parametro de criterio, la ordene de manera ascendente (de menor a mayor) o descendente (de mayor a menor), 
de acuerdo al criterio del segundo parametro y retorne la misma ordenada
'''

def ordenar_lista(lista: list, criterio: int) -> list:
    """
     Ordena una lista de números según el criterio indicado.

    La función puede ordenar la lista:
    - de manera ascendente (de menor a mayor)
    - de manera descendente (de mayor a menor)

    El criterio de ordenamiento se define mediante un número:
    - 1 → Ascendente
    - 2 → Descendente

    La función recorre la lista comparando elementos e
    intercambiando sus posiciones cuando es necesario.

    Args:
        lista (list): Lísta de números a ordenar.
        criterio (int): Tipo de ordenamiento.
                        1 para ascendente.
                        2 para descendente. 

    Returns:
        list: Lísta ordenada según el criterio seleccionado.
    """
    print("LISTA ORIGINAL")
    for i in range(len(lista)):
            print(f"indice: {i} - dato: {lista[i]}")
    
    if criterio == 1:
        print("LISTA ORDENADA DE MANERA ASCENDENTE")
        for i in range(len(lista)-1):
            for j in range((i+1), len(lista)):
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    elif criterio == 2:
        print("LISTA ORDENADA DE MANERA DESCENDENTE")
        for i in range(len(lista)-1):
            for j in range((i+1), len(lista)):
                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux                

    
    return lista

mi_lista = [8, 1, 5, 6, 2, 10, 4, 9, 3, 7]
seleccion = int(input('¿Qué deseas realizar?: \n 1.Ordenar de manera Ascendente \n 2.Ordenar de manera Descendente '))

lista_ordenada = ordenar_lista(mi_lista, seleccion)           

for i in range(len(lista_ordenada)):
    print(f"indice: {i} - dato: {lista_ordenada[i]}")
        
# ----------------------------- Solucion Profe sin redundancia ----------------------

def ordenar_lista(lista:list, criterio:str = "ASC") -> list:
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista) ):  
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]):
                    #swap
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista
    
lista = [3, 1, 5, 4, 2]
lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)        