numeros = [0] * 100
nombres = ['A'] * 100
estados = [0] * 100
cargar = 'S'

def cargar_datos():
    for i in range(100):
        if estados[i] == 0:
            numeros[i] = input("NUMERO: ")
            nombres[i] = input("NOMBRE: ")
            estados[i] = 1
            break

while cargar == 'S':
    cargar_datos()
    cargar = input("Cargar datos? ")
    
    
###########################################
print("NRO | NOMBRE")
for i in range(len(numeros)):
    if estados[i] == 1:
        print(f"{numeros[i]} | {nombres[i]}")
    


CANTIDAD = 3

numeros = [0] * CANTIDAD
nombres = ['A'] * CANTIDAD
estados = [0] * CANTIDAD
cargar = 'S'
contador = 0

def cargar_datos(contador):
    for i in range(CANTIDAD):
        if estados[i] == 0:
            numeros[i] = input("NUMERO: ")
            nombres[i] = input("NOMBRE: ")
            estados[i] = 1
            contador += 1
            break
    return contador

while cargar == 'S':
    if contador < CANTIDAD:
        contador = cargar_datos(contador)
        cargar = input("Cargar datos? ")
    else:
        print("No hay mas espacio...")
        break
    
    
###########################################
print("NRO | NOMBRE")
for i in range(len(numeros)):
    if estados[i] == 1:
        print(f"{numeros[i]} | {nombres[i]}")
    


CANTIDAD = 3

numeros = [0] * CANTIDAD
nombres = ['A'] * CANTIDAD
estados = [0] * CANTIDAD
cargar = 'S'
contador = 0

def cargar_datos(contador):
    for i in range(CANTIDAD):
        if estados[i] == 0:
            numeros[i] = input("NUMERO: ")
            nombres[i] = input("NOMBRE: ")
            estados[i] = 1
            contador += 1
            break
    return contador

while cargar == 'S':
    if contador < CANTIDAD:
        contador = cargar_datos(contador)
    if contador == CANTIDAD:
        print("No hay mas espacio...")
        break
    
    cargar = input("Cargar datos? ")
    
###########################################
print("NRO | NOMBRE")
for i in range(len(numeros)):
    if estados[i] == 1:
        print(f"{numeros[i]} | {nombres[i]}")
    


mi_lista = [1,2,3,4,5]

def trabajar_lista(lista_a_trabajar):
    for i in range(len(lista_a_trabajar)):
        lista_a_trabajar[i] = lista_a_trabajar[i] * 3
        
for elemento in mi_lista:
    print(elemento)
    
trabajar_lista(mi_lista)

for elemento in mi_lista:
    print(elemento)


matrix = [ [2, 4, 5, 8], [6, 3, 1, 9] ]

matrix[0][1] = 8

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print("")



'''
mi_lista = [1,2,3,4,5]

def trabajar_lista(lista_a_trabajar):
    for i in range(len(lista_a_trabajar)):
        lista_a_trabajar[i] = lista_a_trabajar[i] * 3
        
for elemento in mi_lista:
    print(elemento)
    
trabajar_lista(mi_lista)

for elemento in mi_lista:
    print(elemento)
'''