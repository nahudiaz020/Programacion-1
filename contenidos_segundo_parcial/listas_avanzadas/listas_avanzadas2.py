import copy

print("SHADOWCOPY")
# Lista original con objetos anidados
lista_original = [[1, 2], [3, 4], [5, 6]]

# Copia superficial de la lista
lista_copia = copy.copy(lista_original)

# Modificamos un elemento dentro de un objeto anidado en la copia
lista_copia[0][0] = 99

# Imprimimos ambas listas
print("Lista Original:", lista_original) # [[99, 2], [3, 4], [5, 6]]
print("Lista Copia:", lista_copia) # [[99, 2], [3, 4], [5, 6]]



#--------------------- COPIA PROFUNDA --------------------------------
print()
print("DEEPCOPY")
# Lista original con objetos anidados
lista_original = [[1, 2], [3, 4], [5, 6]]

# Copia superficial de la lista
lista_copia = copy.deepcopy(lista_original)

# Modificamos un elemento dentro de un objeto anidado en la copia
lista_copia[0][0] = 99

# Imprimimos ambas listas
print("Lista Original:", lista_original) # [[1, 2], [3, 4], [5, 6]]
print("Lista Copia:", lista_copia) # [[99, 2], [3, 4], [5, 6]]


#---------------------- FUNCION ENUMERATE ----------------------------------------
print()
print("FUNCION ENUMERATE")

frutas = ["manzana", "plátano", "naranja"]

# Usar enumerate para mostrar el índice y el valor
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")


#---------------------- FUNCION ZIP ----------------------------------------
print()
print("FUNCION ZIP")

nombres = ["Ricardo", "Roman", "Diego"]
edades = [25, 35, 23]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

