'''
Hacer una funcion que reciba una cadena de caracteres y convierta las iniciales de la misma a mayusculas, 
y el resto a minusculas.
La funcion debera retornar la misma cadena en formato capitalizado. Por ejemplo: Juan Domingo

1) paso la cadena completa a minusculas
2) paso el primer caracter a mayusculas
3) Identifico un espacio en blanco, entonces el proximo caracter lo paso a mayusculas
    Tantos espacios en blanco como ocurran en la cadena de caracteres
'''

from Biblioteca.Funciones import *

def capitalizar_cadena(cadena: str) -> str:
    """ 
    Convierte la primera letra de cada palabra de una cadena a mayúscula
    y el resto de las letras a minúscula.

    Considera que una nueva palabra comienza después de un espacio.

    Args:
        cadena (str): Cadena de caracteres a procesar.

    Returns:
        str: Cadena con formato capitalizado.
    """
    resultado = ""
    nueva_palabra = True  # indica si el próximo carácter va en mayúscula

    for caracter in cadena:
        codigo = ord(caracter)

        if nueva_palabra and (97 <= codigo <= 122):  # letra minúscula
            resultado += chr(codigo - 32)  # la paso a mayúscula
            nueva_palabra = False

        elif not nueva_palabra and (65 <= codigo <= 90):  # letra mayúscula
            resultado += chr(codigo + 32)  # la paso a minúscula

        else:
            resultado += caracter

        # si hay espacio, la próxima letra es nueva palabra
        if caracter == " ":
            nueva_palabra = True

    return resultado

cadena = input("Ingrese un nombre: ")

cadena = capitalizar_cadena(cadena)

print(cadena)

'''
Hacer una funcion que se llame "trim". La misma debe recibir una cadena de caracteres,
recorrer la misma y eliminar todos los espacios en blanco que pudieran estar tanto a la 
izquierda y como a la derecha de la mencionada cadena recibida.
'''