mi_lista = [3, 1 , 5, 4, 2]

print("LISTA ORIGINAL")

for i in range(len(mi_lista)):
    print(f"indice: {i} - dato: {mi_lista[i]}")
    
for i in range(len(mi_lista)-1):
    for j in range((i+1), len(mi_lista)):
        if mi_lista[i] > mi_lista[j]:
            aux = mi_lista[i]
            # 3    3
            mi_lista[i] = mi_lista[j]
            # 1            1
            mi_lista[j] = aux
            # 3            3

print("LISTA ORDENADA DE MANERA ASCENDENTE")

for i in range(len(mi_lista)):
    print(f"indice: {i} - dato: {mi_lista[i]}")
    
for i in range(len(mi_lista)-1):
    for j in range((i+1), len(mi_lista)):
        if mi_lista[i] < mi_lista[j]:
            aux = mi_lista[i]
            # 3    3
            mi_lista[i] = mi_lista[j]
            # 1            1
            mi_lista[j] = aux
            # 3            3

print("LISTA ORDENADA DE MANERA DESCENDENTE")

for i in range(len(mi_lista)):
    print(f"indice: {i} - dato: {mi_lista[i]}")
