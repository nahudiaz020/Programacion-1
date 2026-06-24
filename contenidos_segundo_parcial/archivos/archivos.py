archivo = open('Prueba.txt','r+')

lista_lineas = archivo.readlines()
for linea in lista_lineas : 
    print(linea, end="")

archivo = open('Prueba.txt','r+')

lista_lineas = archivo.readlines()
for linea in lista_lineas : 
    print(linea, end="")

archivo.close()


diccionario = dict([
    ('Legajo','3310'),
    ('Nombre','Eduardo'),
    ('Apellido','Monzon'),
    ('Genero','M'),
    ('P1','2'),
    ('P2','0'),
])

diccionario2 = {
    'Legajo':2510,
    'Nombre':'Manuel',
    'Apellido':'Salazar',
    'Genero':'M',
    'P1':6,
    'P2':4        
}
diccionario3 ={
    'Legajo':4410,
    'Nombre':'Martin',
    'Apellido':'Pereyra',
    'Genero':'M',
    'P1':4,
    'P2':2
}
diccionario4 ={
    'Legajo':4056,
    'Nombre':'Lujan',
    'Apellido':'Escalante',
    'Genero':'F',
    'P1':2,
    'P2':0
}
print('\nLegajo Nombre Apellido Genero P1 P2')
print(diccionario['Legajo'],diccionario['Nombre'],diccionario['Apellido'],diccionario['Genero'],diccionario['P1'],diccionario['P2'])
print(diccionario2['Legajo'],diccionario2['Nombre'],diccionario2['Apellido'],diccionario2['Genero'],diccionario2['P1'],diccionario2['P2'])
print(diccionario3['Legajo'],diccionario3['Nombre'],diccionario3['Apellido'],diccionario3['Genero'],diccionario3['P1'],diccionario3['P2'])
print(diccionario4['Legajo'],diccionario4['Nombre'],diccionario4['Apellido'],diccionario4['Genero'],diccionario4['P1'],diccionario4['P2'])


with open("archivos/archivo.csv", "r+") as archivo:
    matriz = []
    nombres_columnas = archivo.readline().strip().split(",")
    
    for linea in archivo:
    
        linea = linea.rstrip("\n")
        fila = []
        valores = linea.split(",")
    
        for valor in valores:
            if valor.isdigit():
                fila.append(int (valor))
            else:
                fila.append(valor)
    
        matriz.append(fila)
print(f'{nombres_columnas[0]} | \t{nombres_columnas[1]} | \t {nombres_columnas[2]} | \t\t{nombres_columnas[3]}')

for i in range(len(matriz)): 
    print(f'{matriz[i][0]} | \t{matriz[i][1]} | \t{matriz[i][2]} | \t\t{matriz[i][3]}')

nombres_columnas = ["Nombre", "Edad", "Ciudad"]

matriz = [["Pedro", 24, "Paris"], ["José", 25, "toronto"]]

with open("archivo.csv", "w") as archivo:
    archivo.write(",".join(nombres_columnas) + "\n")
    for fila in matriz:
        linea = ""
        for i in range(len(fila)):
            linea += str(fila[i])

            if i < (len(fila) - 1):
                linea += ","

        archivo.write(linea + "\n")
        