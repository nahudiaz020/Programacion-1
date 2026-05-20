def sumar(numero_a: float, numero_b: float) -> float:
    suma = numero_a + numero_b
    return suma


def restar(num_uno: float, num_dos: float) -> float:
    diferencia = num_uno - num_dos
    return diferencia


def multiplicar(num_uno: int, num_dos: int) -> int:
    producto = num_uno * num_dos
    return producto

def dividir(num_uno, num_dos):
    resultado = num_uno / num_dos
    return resultado

def determinar_par_impar (numero):
    retorno = False
    if numero % 2 == 0:
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

'''
Funcion que recorre una cadena de caracteres, por cada caracater llama a la 
funcion get_Char.
Retornara True si todos los elementos de la cadena son letras, o False en caso
contrario.
'''
def es_alpha(cadena: str) -> bool:
    """ 
    Determina si una cadena contiene exactamente un carácter alfabético.

    Verifica que el carácter ingresado sea una letra (mayúscula o minúscula)
    y que no haya más de un carácter.


    Args:
        cadena (str): Cadena de caracteres a analizar.

    Returns:
        bool: True si contiene un solo carácter alfabetico,
              False en caso contrario.
    """
    for letra in cadena:
        retorno = True
        if get_Char(letra) == False:
            retorno = False
            break

    return retorno

def validar_num(num: str) -> bool:
    """ Determina si el carácter recibido es un número.

    La función verifica si el carácter corresponde a un
    dígito numérico del 0 al 9. 

    Args:
        num (str): Carácter a analizar.

    Returns:
        bool: True si el carácter es un número,
              False en caso contrario.
    """
    retorno = False
    if ord(num) >= 48 and ord(num) <= 57:
        retorno = True 
    
    return retorno

def validar_patente(dato: str) -> str:
    """Determina si una patente corresponde a un auto o una moto
según su formato (3 letras y 3 numeros o 3 numeros y 3 letras).
    Args:
        dato (str): Patente compuesta por 6 caracteres

    Returns:
        str: devuelve "AUTO" si la patente tiene formato de 3 letras  y 3 numeros, 
            devuelve "MOTO" si tiene formato de 3 numeros y 3 letras
    """
    contador = 0
    for letra in dato:
        bandera_auto = False
        bandera_moto = False
        if (contador < 3):
            if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122):
                bandera_auto = True
                
        elif (contador < 6):
            if (ord(letra) >= 48 and ord(letra) <= 57):
                bandera_auto = True
    
        if (contador < 3):
            if (ord(letra) >= 48 and ord(letra) <= 57):
                bandera_moto = True
        elif (contador < 6):
            if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122):
                bandera_moto = True
                
        contador += 1
        
        if(bandera_auto == True):
            retorno = "AUTO"
        if(bandera_moto == True):
            retorno = "MOTO"
        
    return retorno

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
    retorno = False
    for caracter in dato:
        retorno = False
        if ord(caracter) >= 48 and ord(caracter) <= 57:
            retorno = True
        else:
            retorno = False
            break
        
    return retorno

# Hacer una funcion, que analice una cadena de caracteres recibida como parametro y y retorne True si corresponde a un numero real (parte entera, punto y parte decimal), False en caso contrario
# 3.14 (Ejemplo)
def es_float(valor: str) -> bool:
    """"
     Determina si una cadena representa un número real.

    Un número válido puede ser:
    - un número entero (ej: 5, 123)
    - un número decimal con un solo punto (ej: 3.14)


    Args:
        valor (str): Cadena de caracteres a analizar.

    Returns:
        bool: True si la cadena representa un número real válido,
              False en caso contrario.
    """
    retorno = False
    contador = 0
    contador_puntos = 0
    for caracteres in valor:
        retorno = False
        caracter = ord(caracteres)
        # Controlo que sea el primer caracter 
        if (contador == 0):
            # Controlo que no sea un numero
            if (caracter < 48 or caracter > 57):
                retorno = False
                break
            # Controlo que sea un numero
            else:
                retorno = True
        # Controlo a partir del segundo caracter en adelante
        if (contador > 0) and ((caracter >= 48 and caracter <= 57) or (caracter == 46)):
            retorno = True
        # Controlo la cantidad de puntos
        if caracter == 46:
            contador_puntos += 1
        # Controlo si hay mas de 1 punto
        if contador_puntos > 1:
            retorno = False
            break

        contador += 1
    return retorno

def factorial_while(numero):
    resultado = 1
    # Mientras n sea mayor que 1 sigue multiplicando
    while numero > 1:
        resultado = resultado * numero
        numero = numero - 1  # Restamos 1 en cada iteracion
    return resultado

def validar_correo(dato: str) -> bool:
    """Determina si una cadena de caracateres tiene formato de correo electronico o no.
      Para que sea valido debe tener formato de texto@texto.texto.
      
      Condiciones:
      No debe empezar por arroba ni terminar con punto.
      No debe tener mas de dos arrobas.
      El arroba no puede estar seguido de punto (@.)

    Args:
        dato (str): Cadena de caracteres a analizar.

    Returns:
        bool: Devuelve True si es un correo valido.
              Devuelve False si no es un correo valido. 
    """
    contador = 0
    posicion_arroba = -1
    posicion_punto = -1
    contador_arroba = 0
    for caracter in dato:
        if caracter == "@":
            posicion_arroba = contador
        elif caracter == ".":
            posicion_punto = contador

        contador += 1

    if posicion_arroba == -1 or posicion_punto == -1:
        return False  # falta @ o .
    if posicion_arroba == 0:
        return False  # no puede empezar con @

    if posicion_punto == contador - 1:
        return False # no puede terminar con .

    if posicion_arroba > posicion_punto:
        return False  # el . debe estar después del @

    if posicion_punto - posicion_arroba == 1:
        return False  # no puede ser "@."

    return True

def convertir_a_mayuscula(caracter):
    retorno = caracter
    if ord(caracter) >= 97 and ord(caracter) <= 122:
        valor = ord(caracter) - 32
        retorno = chr(valor)
    
    return retorno 

def convertir_a_minuscula(caracter):
    retorno = caracter
    if ord(caracter) >= 65 and ord(caracter) <= 90:
        valor = ord(caracter) + 32
        retorno = chr(valor)
    
    return retorno 

def es_palindromo(cadena: str) -> bool:
    """
        Determina si una cadena de caracteres es un palíndromo.
        Un palíndromo es una palabra que se lee igual de izquierda a derecha
        que de derecha a izquierda.
        La función construye una nueva cadena invertida y la compara con la original. 

    Args:
        palabra (str): Cadena de caracteres a analizar.

    Returns:
        bool: True si la palabra es un palíndromo,
              False en caso contrario.
    """
   
    invertida = ""
    retorno = False

    for caracteres in cadena:
        caracter = ord(caracteres)
        if caracter < 97 or caracter > 122:
            retorno = False


    for caracter in cadena:
        invertida = caracter + invertida

    print(f"{cadena} - {invertida}")

    if cadena == invertida:
        retorno = True
    else:
        retorno = False
    
    return retorno

'''
Hacer una funcion que reciba un caracter y retorne True si el mismo es F, f, M, m, X o x,
 o retorne False si no es ninguno de ellos.
'''

def validar_genero(caracter: str) -> bool:
    retorno = True
    caracter = convertir_a_mayuscula(caracter)
    if caracter != 'F' and caracter != 'M' and caracter != 'X':
        retorno = False
    return retorno

def str_upr(cadena):
    cadena_aux = ""
    for letra in cadena:
        cadena_aux = cadena_aux + convertir_a_mayuscula(letra)
        

    return cadena_aux

def str_lwr(cadena):
    cadena_aux = ""
    for letra in cadena:
        cadena_aux = cadena_aux + convertir_a_minuscula(letra)
        

    return cadena_aux

'''
Hacer una funcion que reciba una lista, y un parametro de criterio, la ordene de manera ascendente (de menor a mayor) o descendente (de mayor a menor), 
de acuerdo al criterio del segundo parametro y retorne la misma ordenada
'''
def ordenar_lista_asc(lista: list) -> list:
    """
    Ordena una lista de números de manera ascendente 
    (de menor a mayor).

    La función recorre la lista comparando cada elemento
    con los siguientes y, en caso de ser necesario,
    intercambia sus posiciones.


    Args:
        lista (list): Lista de números a ordenar.

    Returns:
        list: Lista ordenada de manera ascendente.
    """
    print("LISTA ORIGINAL")

    for i in range(len(lista)):
        print(f"indice: {i} - dato: {lista[i]}")
    
    for i in range(len(lista)-1):
        for j in range((i+1), len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista

def ordenar_lista(lista: list, criterio: int) -> list:
    """
     Ordena una lista de números según el criterio indicado.

    La función puede ordenar la lista:
    - de manera ascendente (de menor a mayor)
    - de manera descendente (de mayor a menor)

    El criterio de ordenamiento se define mediante un número:
    - 1 → Ascendente
    - 2 → Descendente

    La función recorre la lista comparando elementos e
    intercambiando sus posiciones cuando es necesario.

    Args:
        lista (list): Lísta de números a ordenar.
        criterio (int): Tipo de ordenamiento.
                        1 para ascendente.
                        2 para descendente. 

    Returns:
        list: Lísta ordenada según el criterio seleccionado.
    """
    print("LISTA ORIGINAL")
    for i in range(len(lista)):
            print(f"indice: {i} - dato: {lista[i]}")
    
    if criterio == 1:
        print("LISTA ORDENADA DE MANERA ASCENDENTE")
        for i in range(len(lista)-1):
            for j in range((i+1), len(lista)):
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    elif criterio == 2:
        print("LISTA ORDENADA DE MANERA DESCENDENTE")
        for i in range(len(lista)-1):
            for j in range((i+1), len(lista)):
                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux                

    
    return lista