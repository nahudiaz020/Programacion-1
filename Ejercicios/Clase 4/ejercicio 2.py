# Hacer una funcion que determine si una cadena de caracteres es numerica o no

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
    for caracter in dato:
        bandera_caracter = False
        if ord(caracter) >= 48 and ord(caracter) <= 57:
            bandera_caracter = True
        else:
            bandera_caracter = False
    
        if bandera_caracter == True:
            retorno = True
        else:
            retorno = False
            break

    return retorno

numero = input("Numero: ")
valor = validar_numeros(numero)

print(valor)

#-------------------------------- RESOLUCION PROFE --------------------------------

def validar_numeros(dato: str) -> bool: 
    retorno = False
    for caracter in dato:
        retorno = False
        if ord(caracter) >= 48 and ord(caracter) <= 57:
            retorno = True
        else:
            retorno = False
            break
        
    return retorno

numero = input("Numero: ")
valor = validar_numeros(numero)

print(valor)
