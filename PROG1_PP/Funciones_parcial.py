def mostrar_menu():
    """
    Muestra la interfaz del menú de opciones del sistema de gestión escolar.
    """

    print("\n----- MENU -----")
    print("1. Cargar datos")
    print("2. Mostrar todos los datos ")
    print("3. Calcular prom. de cada estudiante")
    print("4. Ordenar datos")
    print("5. Mostrar mayor promedio")
    print("6. Mostrar datos de un estudiante")
    print("7. Salir del menu")


def validar_numeros(dato: str) -> bool: 
    """
    Determina si una cadena de caracteres contiene únicamente números.

    La función recorre cada carácter de la cadena y verifica
    si corresponde a un dígito numérico del 0 al 9.

    Args:
        dato (str): Cadena de caracteres a analizar.

    Returns:
        bool: True si todos los caracteres son números,
              False en caso contrario.
   """
    if len(dato) == 0:
        retorno = False
    
    for caracter in dato:
        if ord(caracter) < 48 or ord(caracter) > 57:
            retorno = False
            break
        else:
            retorno = True
            
        
    return retorno


def get_Char(caracter: str) -> bool:
    """ Determina si el carácter recibido es una letra del alfabeto.

    La función verifica si el carácter corresponde a una letra
    mayúscula (A-Z) o minúscula (a-z).

    Args:
        caracter (str): Carácter a analizar.

    Returns:
        bool: True si el carácter es una letra,
              False en caso contrario.
    """
    retorno = False
    dato = ord(caracter)
    if (dato >= 65 and dato <= 90) or (dato>= 97 and dato <= 122):
        retorno = True

    return retorno


def validar_nombre(nombre: str) -> bool:
    """
    Determina si una cadena corresponde a un nombre válido.

    La función verifica que la cadena contenga únicamente:
    - letras mayúsculas o minúsculas
    - espacios en blanco

    Args:
        nombre (str): Nombre y apellido a validar.

    Returns:
        bool: True si el nombre es válido.
              False en caso contrario.
    """
    retorno = True
    if len(nombre) == 0:
        retorno = False
    
    else:
        for caracter in nombre:
            # VALIDAR LETRAS
            if get_Char(caracter):
                retorno = True
            # VALIDAR ESPACIOS
            elif caracter == " ":
                retorno = True
            else:
                retorno = False
                break
    return retorno


def convertir_a_mayuscula(caracter):
    """
    Convierte un carácter alfabético en minúscula a su equivalente en mayúscula.
    Aplica la diferencia numérica de la tabla ASCII (-32) para realizar
    la conversión de forma puramente algorítmica.

    Args:
        caracter (str): El carácter a convertir.

    Returns:
        str: El carácter convertido a mayúscula, o el mismo carácter 
             si no era una letra minúscula.
    """
    retorno = True
    if ord(caracter) >= 97 and ord(caracter) <= 122:
        valor = ord(caracter) - 32
        retorno = chr(valor)
    return retorno 


def validar_genero(caracter: str) -> bool:
    """
    Valida si un carácter corresponde a un género permitido (F, M o X).
    La función normaliza el carácter convirtiéndolo previamente a mayúscula
    para aceptar variantes en minúsculas.

    Args:
        caracter (str): Carácter que representa el género.

    Returns:
        bool: True si corresponde a 'F', 'M' o 'X',
              False en caso contrario.
    """
    retorno = True
    if len(caracter) != 1:
        retorno = False
    
    else:
        caracter = convertir_a_mayuscula(caracter)
        if caracter != 'F' and caracter != 'M' and caracter != 'X':
            retorno = False 
    return retorno


def ingresar_datos(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list) -> None:
    """
    Permite la carga secuencial de datos de estudiantes por consola.
    Completa el listado de listas paralelas desde la cantidad actual precargada
    hasta alcanzar el límite estricto de 30 estudiantes, validando que los legajos
    no se repitan.

    Args:
        legajos (list): Lista de legajos (enteros).
        nombres (list): Lista de nombres (strings).
        generos (list): Lista de géneros (F|M|X).
        notas_pp (list): Lista de notas del primer parcial.
        notas_sp (list): Lista de notas del segundo parcial.
    """
    LIMITE_ESTUDIANTES = 30
    cantidad_precargada = 0
    for i in range(LIMITE_ESTUDIANTES):
        if legajos[i] != 0:
            cantidad_precargada = cantidad_precargada + 1
    if cantidad_precargada >= LIMITE_ESTUDIANTES:
        print(f"\nYa se encuentran cargados los {LIMITE_ESTUDIANTES} estudiantes.")
        return

    for i in range(cantidad_precargada, LIMITE_ESTUDIANTES):
        print(f"\n---- ESTUDIANTE {i+1} ----")
        
        while True:
            legajo_in = input("Ingrese el legajo del estudiante: ")
            if validar_numeros(legajo_in):
                legajo_entero = int(legajo_in)
                if buscar_estudiante(legajos, legajo_entero) != -1:
                    print("Error. Ese legajo ya pertenece a otro estudiante.")
                else:
                    legajo_final = legajo_entero
                    break
            
            else:
                print("Error. Ingrese solo numeros.")
        
        while True:
            nombre_in  = input("Ingrese el nombre del estudiante: ")
            if validar_nombre(nombre_in):
                nombre_final = nombre_in
                break
            print("Ingrese un nombre valido")

        while True:
            genero_in = input("Ingrese el genero del estudiante (F|M|X): ")
            if validar_genero(genero_in):
                genero_final = convertir_a_mayuscula(genero_in)
                break
            print("ERROR. Ingrese un genero valido.") 

        while True:
            primer_parcial_in = input("Ingrese las notas del primer parcial (1 al 10): ")
            if validar_numeros(primer_parcial_in):
                nota = int(primer_parcial_in)
                if nota >= 1 and nota <= 10:
                    notas_pp_final = nota
                    break
                print("Error. La nota debe estar entre 1 y 10.")
            else:
                print("Error. Ingrese solo numeros.") 

        while True:
            segundo_parcial_in = input("Ingres las notas del segundo parcial (1 al 10): ")  
            if validar_numeros(segundo_parcial_in):
                nota = int(segundo_parcial_in)
                if nota >= 1 and nota <= 10:
                    notas_sp_final = nota
                    break
                print("Error. La nota debe estar entre 1 y 10.")
            else:
                print("Error. Ingrese solo numeros.")
        
        legajos[i] = legajo_final
        nombres[i] = nombre_final
        generos[i] = genero_final
        notas_pp[i] = notas_pp_final
        notas_sp[i] = notas_sp_final


def buscar_estudiante(legajos: list, legajo_buscado: int) -> int:
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
   

def mostrar_estudiante(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list, promedios: list, promedios_calculados: bool, indice: int) -> None:
    """
    Muestra de forma formateada por consola los datos de un único estudiante basado en su índice.

    Args:
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        notas_pp (list): Lista de notas primer parcial.
        notas_sp (list): Lista de notas segundo parcial.
        indice (int): Posición física del estudiante en las listas.
    """
    if promedios_calculados == True:
        promedio = promedios[indice]
    else:
        promedio = 0.0 
       
    print(f"{legajos[indice]}\t| {nombres[indice]}\t| {generos[indice]}\t| {notas_pp[indice]}\t| {notas_sp[indice]}\t| {promedio}")


def mostrar_todos(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list, promedios: list, promedios_calculados: bool) -> None:
    """
    Recorre e imprime el listado completo de los estudiantes cargados en el sistema.

    Args:
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        notas_pp (list): Lista de notas primer parcial.
        notas_sp (list): Lista de notas segundo parcial.
    """
    print("\nResumen de Estudiantes:")
    print("LEGAJO\t| NOMBRE | GÉNERO | P1 | P2 | PROM")
    for i in range(len(legajos)):  
        if legajos[i] != 0:
            mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, promedios, promedios_calculados, i)
    

def calcular_promedio(notas_pp: list, notas_sp: list, promedios: list) -> None:
    """
    Calcula el promedio de exámenes de cada estudiante de manera secuencial.
    Si las posiciones ya existen en la lista de promedios, sobreescribe los valores.
    Si la lista está vacía, añade los nuevos resultados.

    Args:
        notas_pp (list): Lista de notas primer parcial.
        notas_sp (list): Lista de notas segundo parcial.
        promedios (list): Lista destino para almacenar los promedios calculados.
    """
    for i in range(len(notas_pp)):
        promedio = (notas_pp[i] + notas_sp[i]) /2
        promedios[i] = promedio
        print(f"Estudiante {i+1} -> Promedio: {promedio:.2f}")


def ordenar_estudiantes(legajos:list, nombres: list, generos:list, notas_pp: list, notas_sp: list, promedios: list, criterio:str = "DESC") -> None:
    """
    Ordena de forma paralela todas las listas de datos bajo el ordenamiento Bubble Sort.
    El ordenamiento toma como pivote o criterio la lista de promedios generada.

    Args:
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        notas_pp (list): Lista de notas primer parcial.
        notas_sp (list): Lista de notas segundo parcial.
        promedios (list): Lista de promedios calculados.
        criterio (str): "ASC" para ordenar de menor a mayor, o "DESC" de mayor a menor.
    """
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


def mostrar_mayores_promedios(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list, promedios: list, promedios_calculados: bool) -> None: 
    """
    Busca el valor máximo dentro de los promedios y muestra a él o los estudiantes asociados.
    Realiza una búsqueda lineal manual para identificar el mayor promedio absolutoy contempla casos de empate imprimiendo todos los registros coincidentes.
    Args:
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        notas_pp (list): Lista de notas primer parcial.
        notas_sp (list): Lista de notas segundo parcial.
        promedios (list): Lista de promedios calculados."""
    mayor_promedio = promedios[0]
    for i in range(len(promedios)):
        if promedios[i] > mayor_promedio:
            mayor_promedio = promedios[i]
        
    print(f"\n--- Estudiantes con el mayor promedio ({mayor_promedio:.2f}) ---")
    for i in range(len(promedios)):
        if promedios[i] == mayor_promedio:
            mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, promedios, promedios_calculados, i)
            

def verificar_carga_completa(lista_legajos: list) -> bool:
    """
    Verifica si la cantidad de estudiantes cargados cumple con el límite estricto de 30.

    Args:
        lista_legajos (list): Lista de legajos cargados en el sistema.

    Returns:
        bool: True si la densidad de datos es igual a 30, False en caso contrario
    """
    contador_reales = 0
    retorno = True
    for i in range(len(lista_legajos)):
        if lista_legajos[i] != 0:
            contador_reales = contador_reales + 1
        
    if contador_reales < 30:
        print("Debe ingresar a la opcion 1 y completar los datos restantes.")
        retorno = False
    return retorno


def verificar_promedios_calculados(bandera_promedios: bool) -> bool:
    """
    Verifica si se ejecutó previamente el cálculo de promedios en el sistema.
    Args:
        bandera_promedios (bool): Indicador que representa si la opción 3 fue ejecutada.

    Returns:
        bool: True si los datos de promedios están inicializados, False en caso de infracción.
    """
    retorno = True
    if not bandera_promedios:
        print("\nERROR: Primero debe calcular los promedios en la opcion 3.")
        retorno = False
    return retorno


def ejecutar_ordenamiento(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list, promedios: list) -> None:
    """
    Pide el criterio al usuario y ordena los datos si la entrada es correcta.

    Args:
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        notas_pp (list): Lista de notas primer parcial.
        notas_sp (list): Lista de notas segundo parcial.
        promedios (list): Lista de promedios calculados.
    """
    criterio_ingresado = input("Ingrese criterio de ordenamiento (ASC o DESC): ")
    criterio = ""
    for i in range(len(criterio_ingresado)):
        letra_mayuscula = convertir_a_mayuscula(criterio_ingresado[i])
        criterio = criterio + letra_mayuscula

    if criterio == "ASC" or criterio == "DESC":
        ordenar_estudiantes(legajos, nombres, generos, notas_pp, notas_sp, promedios, criterio)
        print(f"\nAlumnos ordenados por promedio {criterio}:")
        mostrar_todos(legajos, nombres, generos, notas_pp, notas_sp, promedios, True)
    else:
        print("Criterio invalido. Ingrese estrictamente 'ASC' o 'DESC'.")


def gestionar_busqueda_alumno(legajos: list, nombres: list, generos: list, notas_pp: list, notas_sp: list, promedios: list, promedios_calculados: bool) -> None:
    """
    Se encarga de la interfaz de entrada, validación y respuesta de búsqueda por legajo de forma segura.
    
    Args:
        legajos (list): Lista estática de legajos.
        nombres (list): Lista estática de nombres.
        generos (list): Lista estática de géneros.
        notas_pp (list): Lista estática de notas del primer parcial.
        notas_sp (list): Lista estática de notas del segundo parcial.
        promedios (list): Lista estática de promedios calculados.
        promedios_calculados (bool): Bandera que indica el estado del cálculo de promedios.
    """
    legajo_ingresado = input("Ingrese el legajo a buscar: ")
    if validar_numeros(legajo_ingresado):
        legajo_buscado = int(legajo_ingresado)
        indice = buscar_estudiante(legajos, legajo_buscado)  
        if indice != -1:  
            mostrar_estudiante(legajos, nombres, generos, notas_pp, notas_sp, promedios, promedios_calculados, indice)  

        else:
            print("No se encontro ningun estudiante con ese legajo.")   
    else:
        print("Error. El legajo debe contener exclusivamente digitos numericos.")