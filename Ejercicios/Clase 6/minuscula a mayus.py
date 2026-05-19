'''
Desarrollar una funcion que reciba un caracter y el mismo si esta en minuscula,
 lo transforme a mayuscula.
 La funcion deberá retornar el caracter en mayuscula.
'''
#A 65 - a97 -> 32
#D 68 - d 100 -> 32
#Q 81 - q 113 -> 32
#97 - 122

def convertir_a_mayuscula(caracter):
    retorno = caracter
    if ord(caracter) >= 97 and ord(caracter) <= 122:
        valor = ord(caracter) - 32
        retorno = chr(valor)
    
    return retorno 

letra = input("Ingrese una letra: ")
letra = convertir_a_mayuscula(letra)
print(letra)