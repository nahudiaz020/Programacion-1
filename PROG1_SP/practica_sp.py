from Funciones1 import *

alumnos = []
opcion = ""
promedios_calculados = False

while opcion != "10":

    mostrar_menu()

    opcion = input("Ingrese una opcion: ").strip()

    match opcion:

        case "1":
            alumnos = leer_json("PROG1_SP/data_sp.json")
            promedios_calculados = False
            print("Datos cargados desde el archivo.")
            limpiar_pantalla()
        
        case "2":
            if len(alumnos) == 0:
                print("Cargando datos inicial del JSON..")
                alumnos = leer_json("PROG1_SP/data_sp.json")
            cargar_un_alumno(alumnos)
            promedios_calculados = False
            limpiar_pantalla()

        case "3":
            if verificar_datos_cargados(alumnos):
                imprimir_titulos("LEGAJO | NOMBRE | GENERO | P1  |  P2  |  PROM")
                mostrar_Alumnos(alumnos)
            limpiar_pantalla()
            
        case "4":
            if verificar_datos_cargados(alumnos):
                calcular_promedio(alumnos)
                promedios_calculados = True
                print("Promedios calculados correctamente")
            limpiar_pantalla()

        case "5":
            if verificar_datos_cargados(alumnos) and verificar_promedios_calculados(promedios_calculados):
                alumnos.sort(key=lambda alumno: alumno["prom"], reverse=True)
                imprimir_titulos("ALUMNOS ORDENADOS POR PROMEDIO DESC")
                mostrar_Alumnos(alumnos)
            limpiar_pantalla()
               
        case "6":
            if verificar_datos_cargados(alumnos) and verificar_promedios_calculados(promedios_calculados):
                mostrar_mayor_promedio(alumnos)
            limpiar_pantalla()

        case "7": 
            if verificar_datos_cargados(alumnos):
                gestionar_busqueda_alumno(alumnos)
            limpiar_pantalla()
        
        case "8":
            if verificar_datos_cargados(alumnos) and verificar_promedios_calculados(promedios_calculados):
                exportar_json(alumnos, "PROG1_SP/data_sp.json")
            limpiar_pantalla

        case "9":    
            if verificar_datos_cargados(alumnos) and verificar_promedios_calculados(promedios_calculados):
                exportar_csv(alumnos, "PROG1_SP/data_sp.csv")
            limpiar_pantalla()

        case "10":
            print("Saliendo del programa...")

        case _:
            print("Opcion invalida")
            limpiar_pantalla()