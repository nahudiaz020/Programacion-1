from PROG1_PP.Funciones_parcial import *
# legajos = []
# nombres = []
# generos = []
# notas_pp = []
# notas_sp = []
legajos = [1001, 1002, 1003, 1004, 1005]
nombres = ["Juan Perez", "Ana Gomez", "Luis Martinez", "Sofia Lopez", "Carlos Diaz"]
generos = ["M", "F", "M", "F", "M"]
notas_pp = [7, 9, 6, 10, 8]
notas_sp = [8, 10, 7, 9, 6]
promedios = [7.5, 9.5, 6.5, 9.5, 7.0]
promedios = []

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

while opcion != "7":

    mostrar_menu()

    opcion = input("Ingrese una opcion: ")

    match opcion:
        case "1":
            ingresar_datos(legajos, nombres, generos, notas_pp, notas_sp)
        
        case "2":
            mostrar_todos(legajos, nombres, generos, notas_pp, notas_sp)
            mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, 4)

        case "3":
            promedio = calcular_promedio(notas_pp, notas_sp, promedios)

        case "4":
            criterio = input("Ingrese ASC o DESC: ")
            ordenar_estudiantes(legajos, nombres, generos, notas_pp, notas_sp, promedios, criterio)
            mostrar_todos(legajos, nombres, generos, notas_pp, notas_sp)

        case "5":
            if len(promedios) > 0:
                resultado = encontrar_extremos(promedios)
                indice_maximo = resultado[0] 
                indice_minimo = resultado[1]
                print("\n--- MAYOR PROMEDIO ----")
                mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, indice_maximo)
                print(f"Promedio: {promedios[indice_maximo]:.2f}")

                print("\n--- MENOR PROMEDIO ----")
                mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, indice_minimo)
                print(f"Promedio: {promedios[indice_minimo]:.2f}")

            else:
                print("Primero debe calcular los promedios.")

        case "6":
            legajo_buscado = int(input("Ingrese legajo a buscar: "))
            indice = buscar_estudiante(legajos, legajo_buscado)  
            if indice != -1:  
                mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, indice)  
            
            else:
                print("No se encontro el estudiante.")   

        case "7":
            print("Saliendo del menu...")
        
        case _:
            print("Opcion invalida")         

   

        
            
            
            
            
            
            
       

    

        