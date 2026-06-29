alumnos = [
{
    'Legajo': 3310,
    'Nombre': 'Eduardo',
    'Apellido': 'Monzon',
    'Genero':'M',
    'P1':2,
    'P2':1,
    'Promedio':((2+1)/2)
},
{
    'Legajo':2510,
    'Nombre':'Manuel',
    'Apellido':'Salazar',
    'Genero':'M',
    'P1':6,
    'P2':4,
    'Promedio':((6+4)/2)       
},
{
    'Legajo':4410,
    'Nombre':'Martin',
    'Apellido':'Pereyra',
    'Genero':'M',
    'P1':4,
    'P2':2,
    'Promedio':(4+2)/2  
},
{
    'Legajo':4056,
    'Nombre':'Lujan',
    'Apellido':'Escalante',
    'Genero':'F',
    'P1':2,
    'P2':1,
    'Promedio':(2+1)/2  
}
]

def imprimir_titulos(titulos:str ) -> None :
    linea = "----"
    for i in range(len(titulos)):
        linea = linea + "-"    
        
    print(linea)
    print("# "+titulos+" #")
    print(linea)

def mostar_alumno(lista_alumnos) :
    print(f"{lista_alumnos['Legajo']}  |  {lista_alumnos['Nombre']}  |  {lista_alumnos['Apellido']}  |  {lista_alumnos['Genero']}  |  {lista_alumnos['P1']}  |  {lista_alumnos['P2']}  |  {lista_alumnos['Promedio']}")

def mostrar_Alumnos (lista_alumnos : list) : 
    for i in range(len(lista_alumnos)):
        mostar_alumno(lista_alumnos[i])
        
def calcular_promedio(lista_alumnos :list ) :
    for i in range(len(lista_alumnos)) :
        lista_alumnos[i]['Promedio'] = (lista_alumnos[i]['P1'] + lista_alumnos[i]['P2']) / 2
        
#print(alumnos)

'''
print('Legajo Nombre Apellido Genero P1 P2 Prom')
print(diccionario['Legajo'],diccionario['Nombre'],diccionario['Apellido'],diccionario['Genero'],diccionario['P1'],diccionario['P2'],diccionario['Promedio'])
print(diccionario2['Legajo'],diccionario2['Nombre'],diccionario2['Apellido'],diccionario2['Genero'],diccionario2['P1'],diccionario2['P2'],diccionario2['Promedio'])
print(diccionario3['Legajo'],diccionario3['Nombre'],diccionario3['Apellido'],diccionario3['Genero'],diccionario3['P1'],diccionario3['P2'],diccionario3['Promedio'])
print(diccionario4['Legajo'],diccionario4['Nombre'],diccionario4['Apellido'],diccionario4['Genero'],diccionario4['P1'],diccionario4['P2'],diccionario4['Promedio'])
'''
calcular_promedio(alumnos)
imprimir_titulos("LEGAJO  NOMBRE   APELLIDO   GENERO  P1    P2   PROM")
alumnos.sort(key=lambda alumno: alumno["Legajo"])
mostrar_Alumnos(alumnos)
