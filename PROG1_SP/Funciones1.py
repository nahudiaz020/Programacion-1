import json

def limpiar_pantalla() -> None:
    """
    Frena el programa para que el usuario lea el cartel y 
    luego limpie la pantalla empujando el texto.
    """
    input("\nPresione ENTER para continuar...")

    for i in range(30):
        print("")


def leer_json(data_sp):
    """
    Abre un archivo JSON, lee su contenido y extrae la lista de alumnos.
    
    Args:
        data_sp (str): La ruta o nombre del archivo JSON a leer.
        
    Returns:
        list: Una lista de diccionarios con los datos de los estudiantes.
    """
    with open(data_sp, "r") as archivo:
        diccionario_raiz = json.load(archivo)

    lista_alumnos = diccionario_raiz["estudiantes"]
    return lista_alumnos


def asegurar_precarga_json(lista_alumnos: list, ruta_archivo: str) -> list:
    """ 
    Verifica si la lista está vacía. Si es así, lee el JSON en segundo plano 
    para asegurar la persistencia y la retorna. Si ya tenía datos, no hace nada. 
    """
    if len(lista_alumnos) == 0:
        print("Cargando datos inicialels desde el JSON")
        lista_alumnos = leer_json(ruta_archivo)
        
    return lista_alumnos


def validar_genero(genero: str) -> bool:
    """
    Valida si el género ingresado es correcto según las opciones permitidas.
    
    Args:
        genero (str): El carácter que representa el género.
        
    Returns:
        bool: Retorna True si es 'F', 'M' o 'X', de lo contrario False.
    """
    if genero == "F" or genero == "M" or genero == "X":
        retorno = True
    else:
        retorno = False
    return retorno


def validar_nota(nota: int) -> bool:
    """
    Valida si una nota numérica se encuentra dentro del rango escolar permitido.
    
    Args:
        nota (int): La nota a evaluar.
        
    Returns:
        bool: Retorna True si la nota está entre 1 y 10 inclusive, de lo contrario False.
    """
    return 1 <= nota <= 10


def validar_nombre(nombre: str) -> bool:
    """
    Valida que una cadena de texto contenga únicamente caracteres alfabéticos y espacios.
    
    Args:
        nombre (str): El nombre o apellido a verificar.
        
    Returns:
        bool: Retorna True si solo contiene letras y espacios, de lo contrario False.
    """
    return nombre.replace(" ", "").isalpha()


def cargar_un_alumno(lista_actual: int) -> None:
    """
    Realiza la carga de un unico alumno y lo agrega
    al final de la lista unificada.
    """
    print("\n---- CARGA DE ESTUDIANTE ----")
    legajo = (input("Legajo: "))
    while not legajo.isdigit():
        print("Error: Legajo invalido (numerico entero)")
        legajo = input("Legajo: ")
                
    nombre = input("Apellido y Nombre: ")

    while not validar_nombre(nombre):
        print("Error. Ingrese solo letras.")
        nombre = input("Apellido y Nombre: ")

    genero = input("Genero (F/M/X): ").upper()

    while not validar_genero(genero):
        print("Error. Ingrese F, M o X.")
        genero = input("Genero (F/M/X): ").upper()

    nota_pp = input("Primer parcial: ")

    while not nota_pp.isdigit() or not validar_nota(int(nota_pp)):
        print("Error: nota invalida (1-10 y numerico entero)")
        nota_pp = input("Primer parcial: ")

    nota_pp = int(nota_pp)

    nota_sp = input("Segundo parcial: ")

    while not nota_sp.isdigit() or not validar_nota(int(nota_sp)):
        print("Error: nota invalida (1-10 y numerica)")
        nota_sp = input("Segundo parcial: ")
        
    nota_sp = int(nota_sp)

        
    nuevo_alumno = {
        "legajo": int(legajo),
        "ape_nom": nombre,
        "genero": genero,
        "pp": nota_pp,
        "sp": nota_sp,
        "prom" : 0
    }

    lista_actual.append(nuevo_alumno)
    print(f"Alumno con legajo {legajo} agregado con éxito a la lista.")


def verificar_datos_cargados(lista_alumnos: list) -> bool:
    """
    Devuelve True si la lista tiene alumnos, de lo contrario
    muestra False
    """
    if len(lista_alumnos) > 0:
        retorno = True
    else:
        print("Primero debe cargar los datos (Opción 1 o 2)")
        retorno = False
    
    return retorno


def verificar_promedios_calculados(bandera_promedios: bool) -> bool:
    """
    Devuelve True si los promedios ya fueron procesados, de lo contrario
    muestra False.
    """
    if bandera_promedios == True:
        retorno = True
    else:
        print("Primero debe calcular los promedios (Opción 4).")
        retorno = False
    
    return retorno


def imprimir_titulos(titulos:str ) -> None :
    """
    Dibuja un encabezado estético y centrado para organizar los reportes por consola.
    
    Args:
        titulos (str): El texto informativo que se lucirá dentro del recuadro.
    """
    linea = "----"
    for i in range(len(titulos)):
        linea = linea + "-"    
        
    print(linea)
    print("# "+titulos+" #")
    print(linea)

def mostar_alumno(alumno) :
    """
    Muestra en una única línea tabulada las claves principales de un estudiante.
    Esta función es el bloque base para listados y búsquedas.
    
    Args:
        alumno (dict): Diccionario que contiene la información del estudiante.
    """
    print(alumno['legajo'],  "|",  
        alumno['ape_nom'],  "|", 
        alumno['genero'],  "|",
        alumno['pp'],  "|",  
        alumno['sp'],  "|",
        alumno['prom'])

def mostrar_Alumnos (lista_alumnos) :
    """
    Recorre un conjunto de estudiantes imprimiendo cada elemento.
    
    Args:
        lista_alumnos (list): Lista que contiene los diccionarios a iterar.
    """ 
    for alumno in lista_alumnos:
        mostar_alumno(alumno)

def buscar_estudiante(lista_alumnos: list, legajo_buscado: int) -> int:
    """
    Realiza una búsqueda secuencial verificando la coincidencia de legajo.
    
    Args:
        lista_alumnos (list): Lista de diccionarios donde se buscará.
        legajo_buscado (int): El número de identificación que ingresó el usuario.
        
    Returns:
        int: Retorna el índice (posición) de la celda encontrada. Si no existe, devuelve -1.
    """

    retorno = -1

    for i in range(len(lista_alumnos)):

        if lista_alumnos[i]["legajo"] == legajo_buscado:

            retorno = i
            break

    return retorno     


def mostrar_estudiante_buscado(lista_alumnos: list, indice: int) -> None:
    """
    Imprime en pantalla la ficha de un estudiante localizado mediante un índice de éxito.
    
    Args:
        lista_alumnos (list): Lista de diccionarios del proyecto.
        indice (int): La posición exacta dentro de la lista que se desea visualizar.
    """
    print(f"\n--- ESTUDIANTE ENCONTRADO (Posición{indice + 1}) ---")
       
    alumno = lista_alumnos[indice]

    imprimir_titulos("RESULTADO DE LA BÚSQUEDA")
    mostar_alumno(alumno) 


def gestionar_busqueda_alumno(lista_alumnos: list) -> None:
    """
    Maneja de forma interna los reintentos de búsqueda por legajo
    sin sobrecargar el main.
    """
    while True:
        print("\n ---- BUSCAR ALUMNO ----")
        legajo_input = input("Ingrese el legajo a buscar (o 'S' para salir al menú): ").strip()

        if legajo_input.upper() == "S":
            print("Búsqueda cancelada.")
            break

        if legajo_input.isdigit():
            legajo_num = int(legajo_input)

            indice_encontrado = buscar_estudiante(lista_alumnos, legajo_num)

            if indice_encontrado != -1:
                mostrar_estudiante_buscado(lista_alumnos, indice_encontrado)
                break
            else:
                print(f"No se encontró ningún alumno con el legajo {legajo_num}.")
                legajo_input = input("Ingrese el legajo a buscar: ")
        else:
            print("Error: El legajo debe ser un número entero.")


def calcular_promedio(lista_alumnos):
    """
    Calcula el promedio aritmético flotante entre P1 y P2 de cada alumno.
    Modifica directamente el diccionario original añadiendo el resultado.
    
    Args:
        lista_alumnos (list): Lista de diccionarios con las notas académicas.
    """ 
    for alumno in lista_alumnos:
        alumno['prom'] = (alumno['pp'] + alumno['sp']) / 2

def mostrar_mayor_promedio(lista_alumnos: list) -> None:
    """
    Busca el promedio máximo guardando el valor directamente. 
    """ 
    max_promedio = lista_alumnos[0]["prom"]
    for alumno in lista_alumnos:
        if alumno["prom"] > max_promedio:
            max_promedio = alumno["prom"]

       
    print(f"\n Mayor promedio encontrado: {max_promedio: 2.f}")
    imprimir_titulos("ESTUDIANTE/S CON MAYOR PROMEDIO")

    for alumno in lista_alumnos:
        if alumno["prom"] == max_promedio:
            mostar_alumno(alumno)

def exportar_json(lista_alumnos, ruta_archivo):
    """
    Reconstruye la estructura de diccionario raíz e inmuta los datos
    con sus promedios en un nuevo fichero en formato JSON estructurado.
    
    Args:
        lista_alumnos (list): Lista de diccionarios vigente en memoria.
        ruta_archivo (str): Nombre del archivo donde se guardarán los cambios.
    """
    diccionario_salida = {
        "estudiantes" : lista_alumnos
    }
    with open(ruta_archivo, "w") as archivo:
        json.dump(diccionario_salida, archivo, indent=4)
    
    print(f"Archivo JSON exportado con éxito en: {ruta_archivo}")

def exportar_csv(lista_alumnos, ruta_archivo):
    """
    Descompone los diccionarios a una matriz bidimensional (lista de listas).
    Genera el archivo CSV concatenando celdas por comas y gestionando saltos de renglón.
    
    Args:
        lista_alumnos (list): Lista de diccionarios a respaldar.
        ruta_archivo (str): Nombre físico que tomará el archivo CSV de salida.
    """
    nombres_columnas = ["legajo", "ape_nom", "genero", "pp", "sp", "prom"]
    matriz = []
    for alumno in lista_alumnos:
        fila_alumno = [
            alumno["legajo"],
            alumno["ape_nom"],
            alumno["genero"],
            alumno["pp"],
            alumno["sp"],
            alumno["prom"]
        ]
        matriz.append(fila_alumno)
    
    with open(ruta_archivo, "w") as archivo:
        archivo.write(",".join(nombres_columnas) + "\n")
        for fila in matriz:
            linea = ""
            for i in range(len(fila)):
                linea += str(fila[i])

                if i < (len(fila) - 1):
                    linea += ","
            archivo.write(linea + "\n")
    print(f"Archivo CSV exportado con éxito en: {ruta_archivo}")


def mostrar_menu():
    """
    Muestra la interfaz del menú de opciones del sistema de gestión escolar.
    """

    print("\n----- MENU -----")
    print("1. Leer archivo JSON ")
    print("2. Cargar alumno nuevo manualmente")
    print("3. Mostrar todos los alumnos")
    print("4. Calcular promedios")
    print("5. Ordenar por promedio DESC")
    print("6. Mostrar mayor promedio")
    print("7. Buscar alumno por legajo")
    print("8. Exportar a JSON")
    print("9. Exportar a CSV")
    print("10. Salir")