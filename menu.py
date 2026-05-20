from libreria.Funciones import *
legajos = []
nombres = []
generos = []
notas_pp = []
notas_sp = []

def ingresar_datos(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list) -> None:
    

    cantidad = 30
    for i in range(cantidad):
        print(f"\n---- ESTUDIANTE {i+1} ----")
        
        while True:
            legajo = input(f"Ingrese el legajo del estudiante: ")
            if validar_numeros(legajo):
                legajos.append(int(legajo))
                break
            
            else:
                print("Error. Ingrese solo numeros.")
        legajos.append(legajo)
        
        while True:
            nombre  = input("Ingres el nombre y apellido de cada estudiante: ")
            if validar_nombre(nombre):
                nombres.append(nombre)
                break
            else:
                print("Ingrese un nombre valido")
        nombres.append(nombre)

        while True:
            genero = input("Ingrese el genero de cada estudiante (F|M|X): ")
            if validar_genero(genero):
                generos.append(genero)
                break
            else:
                print("ERROR. Ingrese un genero valido.") 
        generos.append(genero)

        while True:
            primer_parcial = input("Ingrese las notas del primer parcial (1 al 10): ")
            if validar_numeros(primer_parcial):
                notas_pp.append(int(primer_parcial))
                break
            
            else:
                print("Error. Ingrese solo numeros.") 
        notas_pp.append(primer_parcial)

        while True:
            segundo_parcial = input("Ingres las notas del segundo parcial (1 al 10): ")  
            if validar_numeros(segundo_parcial):
                notas_sp.append(int(segundo_parcial))
                break
            
            else:
                print("Error. Ingrese solo numeros.")
        notas_sp.append(segundo_parcial)
    
def encontrar_extremos(calificaciones): 
    """
    Función para encontrar la calificación máxima y mínima.
    Arg: Calificaciones: Lista para almacenar las calificaciones.
    Return: Tupla con el indice de la calificación máxima y mínima ingresada por el usuario.
    """
    for i in range(len(calificaciones)):
        if i == 0:
            indice_maximo = i
        elif calificaciones[i] > calificaciones[indice_maximo]:
            indice_maximo =  1

        if i == 0:
            indice_minimo = i
        elif calificaciones[i] < calificaciones[indice_minimo]:
            indice_minimo =   i

    return indice_maximo, indice_minimo

def mostrar_menu():

    print("\n----- MENU -----")
    print("1. Cargar datos")
    print("2. Mostrar todos los datos ")
    print("3. Calcular prom. de cada estudiante")
    print("4. Ordenar datos")
    print("5. Mostrar mayor promedio")
    print("6. Mostrar datos de un estudiante")
    print("7. Salir del menu")


opcion = 0

while opcion != 7:

    mostrar_menu()

    opcion = input("Ingrese una opcion: ")

    match opcion:
        case "1":
            ingresar_datos(legajos, nombres, generos, notas_pp, notas_sp)
        
        case "2":
            print()

        case "3":
            print()

        case "4":
            print()

        case "5":
            print()

        case "6":
            print()

        case "7":
            print("Saliendo del menu...")
        
        case _:
            print("Opcion invalida")