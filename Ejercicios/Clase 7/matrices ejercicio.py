'''
Hacer una funcion que reciba e inicialice un vector (array unidemencional)
recibe: cantidad de elementos, valor incial.
retorna: lista
'''

def iniciar_vector(elementos, valor_inicial):
    lista_creada = [valor_inicial] * elementos
    return lista_creada

mi_lista = iniciar_vector(5, 9)

print(mi_lista)


#-----------------------------Resolucion Profe---------------------------------------------------------------
'''
Hacer una funcion que reciba e inicialice un vector (array unidemencional)
recibe: cantidad de elementos, valor incial.
retorna: lista
'''

def inicializar_vector(cantidad_elementos, valor_inicial=0):
    lista_creada = [valor_inicial] * cantidad_elementos
    return lista_creada

def imprimir_vector(vector):
    for elemento in vector:
        imprimir_elemento(elemento)

def imprimir_elemento(elemento):
    print(elemento)
    


mi_vector = inicializar_vector(5, 0)

#imprimir_elemento(mi_vector[1])

imprimir_vector(mi_vector)