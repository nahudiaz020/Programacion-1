
matriz_linea_colectivos = [[201, 215, 205, 210, 207], 
                           [213, 206, 212, 208, 211], 
                           [204, 202, 214, 209, 203]]

matriz_legajos = [[101, 110, 115, 111, 102],
                  [103, 104, 112, 114, 108],
                  [105, 107, 106, 113, 109]]


def inicializar_matriz(cantidad_filas : int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
      fila = [valor_inicial] * cantidad_columnas

      matriz += [fila]

    return matriz

'''
def cargar_matriz_secuencialmente(matriz:list):
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))
'''

def validar_legajos(mi_matriz: list, legajo_aux: int ):
    for fila in mi_matriz:
      for legajo in fila:
        if legajo == legajo_aux :
          return True
            
    return False

def buscar_legajo(matriz_legajos, legajo_buscado):
    for i in range(len(matriz_legajos)):
      for j in range(len(matriz_legajos[i])):
        if matriz_legajos[i][j] == legajo_buscado:
          return i, j

    return -1, -1

def ingresar_recuadacion_matriz(matriz_colectivos):
    linea = int(input(f'Ingresar linea de colectivo (1-3)'))
    coche = int(input(f'Ingresar Coche de la Linea {linea} (1-5)'))
    monto = float(input(f'Ingresar el monto recaudado del día'))
    linea -= 1
    coche -= 1

    matriz_colectivos[linea][coche] = matriz_colectivos[linea][coche] + monto
    

def mostrar_menu():

    print("\n----- MENU -----")
    print("1. Cargar planilla de recaudación.")
    print("2. Mostrar recaudación de cada coche y línea.")
    print("3. Calcular y mostrar la recaudación por línea.")
    print("4. Calcular y mostrar la recaudación por coche.")
    print("5. Calcular y mostrar recaudación total.")
    print("6. Salir del menu")


opcion = 0
matriz_recaudacion = inicializar_matriz(3, 5, 0)

while opcion != "6":

    mostrar_menu()

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
          legajo_aux = int(input("ingrese legajo (101-115): "))
          validar_legajo = validar_legajos(matriz_legajos,legajo_aux)
                    
          if validar_legajo == True :
            fila, columna = buscar_legajo(matriz_legajos, legajo_aux)
            monto = float(input("Ingrese el monto recaudado: "))
            matriz_recaudacion[fila][columna] += monto
            print("Recaudación cargada correctamente")
            print(matriz_recaudacion)
                    
          else :
            print("El legajo ingresado no existe. Ingrese uno valido")

        case "2":
            print()
        case "3":
            print()

        case "4":
            print()

        case "5":
            print()

        case "6":
            print("Saliendo del menu... ")
        
        case _:
            print("Opcion invalida")