def generar_diccionarios(matriz):
    lista_diccionarios = []
    for fila in matriz:
        cancion = {
            "titulo": fila[0],
            "vistas": fila[1],
            "duracion": fila[2],
            "link": fila[3],
            "fecha": fila[4] 
        }
        lista_diccionarios.append(cancion)
    return lista_diccionarios

def mostrar_canciones(cancion) :
    print(f"{cancion['titulo']}  |  {cancion['vistas']}  |  {cancion['duracion']}  |  {cancion['link']}  |  {cancion['fecha']}")

def mostrar_cancion (lista_canciones) : 
    for cancion in lista_canciones:
        mostrar_canciones(cancion)

with open("ladygaga.csv", "r") as archivo:
    nombres_columnas = archivo.readline().strip().split(",")
    matriz = []
    for linea in archivo:
        linea = linea.rstrip("\n")
        fila = linea.split(",")
        
        if len(fila) == 5:
            matriz.append(fila)

print(f'{nombres_columnas[0]} | \t{nombres_columnas[1]} | \t {nombres_columnas[2]} | \t{nombres_columnas[3]} | \t{nombres_columnas[4]}')

for i in range(len(matriz)): 
    print(f'{matriz[i][0]} | \t{matriz[i][1]} | \t{matriz[i][2]} | \t{matriz[i][3]} | \t{matriz[i][4]}')

matriz_normalizada = []

for fila in matriz:
    vistas = fila[1].split(" ")
    vistas = int(vistas[0]) * 1000000

    duracion = fila[2].split(":")
    duracion_segundos = int(duracion[0]) * 60 + int(duracion[1])

    nueva_fila = [fila[0], vistas, duracion_segundos, fila[3], fila[4]]
    matriz_normalizada.append(nueva_fila)

lista_canciones = generar_diccionarios(matriz_normalizada)

print("\nDICCIONARIOS:\n")

mostrar_cancion(lista_canciones)

