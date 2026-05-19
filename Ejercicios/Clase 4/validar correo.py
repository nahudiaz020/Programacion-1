# Hacer una funcion, quwe analice una cadena de caracteres recibida como parametro y
#  retorne True si corresponde a un correo electronico (cadena, arroba, punto, cadena), False en caso contrario.


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

caracteres = input("Ingrese caracteres: ")
valor = validar_correo(caracteres)

print(valor)