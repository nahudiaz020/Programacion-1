# Hacer una funcion que determine si una cadena de caracteres es alfabetica o no

def validar_letra(dato: str) -> bool: 
    """   
    Determina si el carácter recibido es una letra del alfabeto.

    La función verifica si el carácter corresponde a una letra
    mayúscula (A-Z) o minúscula (a-z).

    Args:
        dato (str): Carácter a analizar.

    Returns:
        bool: True si el carácter es una letra,
              False en caso contrario.
    """
    retorno = False
    for caracter in dato:
        retorno = False
        if (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
            retorno = True
        else:
            retorno = False
            break
        
    return retorno

caracteres = input("caracteres: ")
valor = validar_letra(caracteres)

print(valor)
