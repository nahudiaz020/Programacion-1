'''
Desarrollar una funcion que reciba un caracter y el mismo si esta en mayuscula,
 lo transforme a minuscula.
 La funcion deberá retornar el caracter en minuscula.
'''
#A 65 - a97 -> 32
#D 68 - d 100 -> 32
#Q 81 - q 113 -> 32
#97 - 122

def get_Char(caracter: str) -> bool:
    retorno = False
    dato = ord(caracter)
    if (dato >= 65 and dato <= 90) or (dato>= 97 and dato <= 122):
        retorno = True

    return retorno

def convertir_a_minuscula(caracter):
    retorno = caracter
    if ord(caracter) >= 65 and ord(caracter) <= 90:
        valor = ord(caracter) + 32
        retorno = chr(valor)
    
    return retorno 

letra = input("Ingrese una letra: ")
valor = get_Char(letra)
while valor == False:
    letra = input("Ingrese una letra: ")
    valor = get_Char(letra)

letra = convertir_a_minuscula(letra)
print(letra)