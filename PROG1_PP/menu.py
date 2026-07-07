from Funciones_parcial import *
'''
legajos = []
nombres = []
generos = []
notas_pp = []
notas_sp = []
'''
legajos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
nombres = ["Ana", "Juan", "Luz", "Luis", "Mia", "Ian", "Eva", "Leo", "Paz", "Roy", "Amy", "Ben", "Zoe", "Tom", "Ada", "Max", "Eli", "Sam", "Teo", "Jon", "Dan", "Rey", "Noa", "Sol", "Feo", "Gus"]
generos = ["F", "M", "X", "M", "F", "M", "F", "M", "X", "M", "F", "M", "F", "M", "F", "M", "X", "M", "M", "M", "M", "M", "X", "F", "M", "M"]
notas_pp = [8, 4, 7, 2, 9, 6, 5, 8, 10, 3, 7, 6, 8, 5, 9, 4, 7, 6, 5, 8, 9, 3, 7, 6, 4, 10]
notas_sp = [7, 5, 8, 4, 10, 5, 6, 9, 9, 4, 8, 7, 9, 6, 8, 5, 8, 7, 6, 7, 10, 4, 8, 7, 5, 9]
promedios = []

opcion = 0
promedios_calculados = False

while opcion != "7":

    mostrar_menu()

    opcion = input("Ingrese una opcion: ")

    match opcion:
        case "1":
            ingresar_datos(legajos, nombres, generos, notas_pp, notas_sp)
            promedios_calculados = False

        case "2":
            if verificar_carga_completa(legajos):
                mostrar_todos(legajos, nombres, generos, notas_pp, notas_sp, promedios, promedios_calculados)

        case "3":
            if verificar_carga_completa(legajos):
                calcular_promedio(notas_pp, notas_sp, promedios)
                promedios_calculados = True
                print("Promedios calculados correctamente.")

        case "4":
            if verificar_carga_completa(legajos):
                if verificar_promedios_calculados(promedios_calculados):
                    ejecutar_ordenamiento(legajos, nombres, generos, notas_pp, notas_sp, promedios, True)

        case "5":
            if verificar_carga_completa(legajos):
                if verificar_promedios_calculados(promedios_calculados):
                    mostrar_mayores_promedios(legajos, nombres, generos, notas_pp, notas_sp, promedios, True)

        case "6":
            if verificar_carga_completa(legajos):
                gestionar_busqueda_alumno(legajos, nombres, generos, notas_pp, notas_sp, promedios, promedios_calculados)   

        case "7":
            print("Saliendo del menu...")
        
        case _:
            print("Opcion invalida")         

   

        
            
            
            
            
            
            
       

    

        