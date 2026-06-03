from Biblioteca.Funciones import *

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
    
cadena = input("Ingrese una palabra: ")


if es_palindromo(cadena):
    print("Es palíndromo")
else:
    print("No es palíndromo")

# -----------------------------------------------------------------------------

def quitar_espacios(cadena: str) -> str: 
    cadena2 = ''
    longitud = len(cadena)
    for i in range(longitud): 
        cadena_ord = cadena[i]
        if cadena[i] == ' ' or cadena_ord == 32:
            print(cadena[i])
        else: 
            cadena2 += cadena[i]
            print(cadena2)
    return cadena2

def verificar_palindromo(cadena: str) -> bool:
    palindromo = False
    cadena2 = quitar_espacios(cadena)

    print(f'nueva palabra: {cadena2}')
    longitud = len(cadena2)
    for i in range(longitud): 
        if cadena2[i] == cadena2[longitud - i - 1]: #cadena2[0] = a longitud = 3. cadena2[3-0-1] <-
            print(f'Coincidencia encontrada para i = {i}: {cadena2[i]} - {cadena2[longitud - i - 1]}')
            palindromo = True
        else: 
            print(f'No hay coincidencia para i = {i}: {cadena2[i]} - {cadena2[longitud - i - 1]}')
            palindromo = False
    return palindromo

def es_palindromo(texto):
    # Limpiar: minúsculas y eliminar espacios
    texto_limpio = "".join(texto.split()).lower()
    # Comparar con su reverso
    return texto_limpio == texto_limpio[::-1]
        # False