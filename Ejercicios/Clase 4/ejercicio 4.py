'''
Hacer una funcion que reciba un caracter y retorne True si el mismo es una letra,
o False si no lo es.
'''
def Es_alpha(caracter: str) -> bool:
    retorno = False
    dato = ord(caracter)
    if (dato >= 65 and dato <= 90) or (dato>= 97 and dato <= 122):
        retorno = True

    return retorno

caracter = input("Ingrese un caracter: ")
valor = Es_alpha(caracter)

print(valor)

#----------------------------------------- RESOLUCION PROFE ------------------------

def get_Char(caracter: str) -> bool:
    retorno = False
    dato = ord(caracter)
    if (dato >= 65 and dato <= 90) or (dato>= 97 and dato <= 122):
        retorno = True

    return retorno

#INICIO validacion de genero
letra = input("Ingrese genero [F|M|X]: ")
valor = get_Char(letra)

while (valor == False) or (letra != 'F' and letra != 'M' and letra != 'X'):
    letra = input("Ingrese genero [F|M|X]: ")
    valor = get_Char(letra)
#FIN validacion de genero

print(valor)