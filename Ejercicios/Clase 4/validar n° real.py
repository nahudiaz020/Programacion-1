# Hacer una funcion, que analice una cadena de caracteres recibida como parametro y y retorne True si corresponde a un numero real (parte entera, punto y parte decimal), False en caso contrario

# 3.14 (Ejemplo)
def es_float(valor: str) -> bool:
    """ Determina si una cadena es un numero real o no.

    Args:
        valor (str): cadena de caracteres a analizar

    Returns:
        bool: Devuelve True si la cadena recibida es un numero real, 
              de lo contrario devolvera False.
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

consultar_caracteres = input("Ingrese un numero: ")
respuesta = es_float(consultar_caracteres)
print(respuesta)