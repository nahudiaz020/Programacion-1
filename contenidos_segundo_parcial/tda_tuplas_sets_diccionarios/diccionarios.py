# Diccionarios

diccionario = dict([
    ('Nombre', 'Sara'),
    ('Edad', 27),
    ('Documento', 1003883),
])

print(diccionario)

#--------------- SEGUNDA FORMA -----------------------

diccionario = {
    'nombre': 'Juan',
    'edad': 21,
    'ciudad': 'Buenos Aires'
}
print(type(diccionario))
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['ciudad'])

#----------------- FUNCION KEYS ------------------------

diccionario = {'Nombre': 'Juan', 'Edad': 21}
print(diccionario.keys())

#----------------- FUNCION VALUES ------------------------

diccionario = {'Nombre': 'Juan', 'Edad': 21}
print(diccionario.values())

#----------------- FUNCION ITEMS ------------------------

diccionario = {'Nombre': 'Juan', 'Edad': 21}
print(diccionario.items())