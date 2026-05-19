# Desarrollar una función que reciba un carácter y 
# determine si ese carácter está comprendido entre 0 ... 9, en caso afirmativo devolverá True, de lo contrario False.

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

num = input("Ingrese un número: ")
valor = validar_num(num)
print(valor)