from libreria.Funciones import *

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

def buscar_estudiante(
        legajos: list,
        legajo_buscado: int
    ) -> int:
    """
    Busca un estudiante por legajo.

    Args:
        legajos (list): Lista de legajos.
        legajo_buscado (int): Legajo a buscar.

    Returns:
        int: Retorna el índice del estudiante encontrado.
             Si no existe, retorna -1.
    """

    retorno = -1

    for i in range(len(legajos)):

        if legajos[i] == legajo_buscado:

            retorno = i
            break

    return retorno     
   
def mostrar_estudiante(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list, indice: int) -> None:
    print(f"\n--- ESTUDIANTE {indice + 1} ---")
       
    print(f"Legajo: {legajos[indice]}")
    print(f"Nombre: {nombres[indice]}")
    print(f"Genero: {generos[indice]}")
    print(f"Notas primer parcial: {notas_pp[indice]}")
    print(f"Notas segundo parcial: {notas_sp[indice]}")    

def mostrar_todos(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list) -> None:
    print("\nResumen de Estudiantes:")
    for i in range(len(legajos)):  
        print(f"\n--- ESTUDIANTE {i+1} ---")
       
        print(f"Legajo: {legajos[i]}")
        print(f"Nombre: {nombres[i]}")
        print(f"Genero: {generos[i]}")
        print(f"Notas primer parcial: {notas_pp[i]}")
        print(f"Notas segundo parcial: {notas_sp[i]}")


def calcular_promedio(notas_pp, notas_sp, promedios): 
    for i in range(len(notas_pp)):
        promedio = (notas_pp[i] + notas_sp[i]) /2
        promedios.append(promedio)
        print(f"Estudiante {i+1} -> Promedio: {promedio:.2f}")
    
def ordenar_estudiantes(legajos:list, nombres: list, generos:list, notas_pp: list, notas_sp: list, promedios: list, criterio:str = "ASC") -> None:
    for i in range(len(promedios)-1):
        for j in range(i + 1, len(promedios) ):  
            if (criterio == "ASC" and promedios[i] > promedios[j]) or (criterio == "DESC" and promedios[i] < promedios[j]):
                    #PROMEDIOS
                    aux = promedios[i]
                    promedios[i] = promedios[j]
                    promedios[j] = aux

                    #LEGAJOS
                    aux = legajos[i]
                    legajos[i] = legajos[j]
                    legajos[j] = aux

                    #NOMBRES
                    aux = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux

                    #GENEROS
                    aux = generos[i]
                    generos[i] = generos[j]
                    generos[j] = aux

                    #PRIMER PARCIAL
                    aux = notas_pp[i]
                    notas_pp[i] = notas_pp[j]
                    notas_pp[j] = aux

                    #SEGUNDO PARCIAL
                    aux = notas_sp[i]
                    notas_sp[i] = notas_sp[j]
                    notas_sp[j] = aux

def encontrar_extremos(promedios): 
    indice_maximo = 0
    indice_minimo = 0
    for i in range(len(promedios)):
        if i == 0:
            indice_maximo = i
            indice_maximo = i
        else:
            if i == 0:
                indice_minimo = i
            elif promedios[i] < promedios[indice_minimo]:
                indice_minimo = i

    return indice_maximo, indice_minimo