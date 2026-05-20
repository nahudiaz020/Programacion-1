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

caracter = input("Caracter: ")
valor = get_Char(caracter)
print(valor)