#print(chr(97))
#print(ord('A'))

# Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre a…z o 
# A…Z, en caso afirmativo devolverá True, de lo contrario False.

def validar_letra(caracter: str) -> bool:
    """ 
    Determina si el carácter recibido es una letra del alfabeto.

    La función verifica si el carácter corresponde a una letra
    mayúscula (A-Z) o minúscula (a-z).

    Args:
        caracter (str): Carácter a analizar.

    Returns:
        bool: True si el carácter es una letra,
              False en caso contrario.
    """
    retorno = False
    if (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
        retorno = True 
    
    return retorno

caracter = input("Caracter: ")
valor = validar_letra(caracter)
print(valor)