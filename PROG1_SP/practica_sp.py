from Funciones1 import *

alumnos = []
opcion = ""
promedios_calculados = False

while opcion != "10":

    mostrar_menu()

    opcion = input("Ingrese una opcion: ")

    match opcion:

        case "1":
            alumnos = leer_json("PROG1_SP/data_sp.json")
            promedios_calculados = False
            print("Datos cargados desde el archivo.")
        case "2":
            cantidad = int(input("Cantidad de alumnos: "))
            alumnos = cargar_alumnos(cantidad)
            promedios_calculados = False

        case "3":
            if len(alumnos) > 0:
                imprimir_titulos("LEGAJO | NOMBRE | GENERO | P1  |  P2  |  PROM")
                mostrar_Alumnos(alumnos)
            else:
                print("Primero debe cargar los datos")
        case "4":
            if len(alumnos) > 0:
                calcular_promedio(alumnos)
                promedios_calculados = True
                print("Promedios calculados correctamente")
            else:
                print("Primero debe cargar los datos.")

        case "5":
            if len(alumnos) > 0:
                if promedios_calculados == True:
                    alumnos.sort(
                    key=lambda alumno: alumno["prom"],
                    reverse=True
                    )
                    imprimir_titulos("ALUMNOS ORDENADOS POR PROMEDIO DESC")
                    mostrar_Alumnos(alumnos)
                else:
                    print("Primero debe calcular los promedios (Opción 4).")    
            else:
                print("Primero debe cargar los datos.")

        case "6":
            if len(alumnos) > 0 and promedios_calculados == True:
                mostrar_mayor_promedio(alumnos)

            elif len(alumnos) == 0:
                print("Primero debe cargar los datos.")
            
            else:
                print("Primero debe calcular los promedios (Opción 4).")

        case "7": 
            if len(alumnos) > 0:
                while True:
                    print("\n ---- BUSCAR ALUMNO ----")
                    legajo_input = input("Ingrese el legajo a buscar (o 'S' para salir al menú): ").strip()

                    if legajo_input.upper() == "S":
                        print("Búsqueda cancelada.")
                        break

                    if legajo_input.isdigit():
                        legajo_num = int(legajo_input)

                        indice_encontrado = buscar_estudiante(alumnos, legajo_num)

                        if indice_encontrado != -1:
                            mostrar_estudiante_buscado(alumnos, indice_encontrado)
                            break
                        else:
                            print(f"No se encontró ningún alumno con el legajo {legajo_num}.")
                            legajo_input = input("Ingrese el legajo a buscar: ")
                    else:
                        print("Error: El legajo debe ser un número entero.")
            else:
                    print("Primero debe cargar los datos.")
        
        case "8":
            if len(alumnos) > 0 and promedios_calculados == True:
                exportar_json(alumnos, "PROG1_SP/data_sp.json")
            elif len(alumnos) == 0:
                print("Primero debe de cargar los datos.")
            else:
                print("Primero debe de calcular los promedios (Opción 4).")
        
        case "9":    
            if len(alumnos) > 0 and promedios_calculados == True:
                exportar_csv(alumnos, "PROG1_SP/data_sp.csv")
            elif len(alumnos) == 0:
                print("Primero debe de cargar los datos.")
            else:
                print("Primero debe de calcular los promedios (Opción 4).")

        case "10":
            print("Saliendo del programa...")

        case _:
            print("Opcion invalida")