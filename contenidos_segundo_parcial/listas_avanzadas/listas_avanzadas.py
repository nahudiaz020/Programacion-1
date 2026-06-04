mi_lista = [3, 1, 4, 5, 2, 6, 9, 10, 8, 7]
#otra_lista = [6, 9, 10, 8, 10]

#mi_lista.extend(otra_lista)

#pos = mi_lista.index(4, 3, 8)

#print(pos)
#print()
#mi_lista.clear()
#elem = mi_lista.pop()
#mi_lista.remove(10)
mi_lista.sort()
mi_lista.reverse()

#desde inclusive, hasta excluido
del mi_lista[1:4]

#print("LISTA ORIGINAL")
for elemento in mi_lista:
    print(elemento, end=" ")
    
#print()    
#print(f"Elemento eliminado: {elem}")
'''    
mi_lista.insert(1, 6)
print()
print("LISTA CON UN DATO AGREGADO")
for elemento in mi_lista:
    print(elemento, end=" ")
'''
