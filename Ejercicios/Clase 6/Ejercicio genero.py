'''
Hacer una funcion que reciba un caracter y retorne True si el mismo es F, f, M, m, X o x,
 o retorne False si no es ninguno de ellos.
'''
def validar_genero(caracter: str) -> bool:
    retorno = True
    dato = ord(caracter)
    if dato != 70 and dato != 77 and dato != 88 and dato != 102 and dato != 109 and dato != 120:
        retorno = False

    return retorno

#INICIO validacion de genero
letra = input("Ingrese genero [F|M|X]: ")
valor = validar_genero(letra)

while (valor == False):
    letra = input("Ingrese genero [F|M|X]: ")
    valor = validar_genero(letra)
#FIN validacion de genero


print(valor)


#-------------------------------------------------------------------------------------

def validar_genero_2(caracter: str) -> bool:
    retorno = True
    if caracter != 'F' and caracter != 'M' and caracter != 'X' and caracter != 'f' and caracter != 'm' and caracter != 'x':
        retorno = False

    return retorno

#INICIO validacion de genero
letra = input("Ingrese genero [F|M|X]: ")
valor = validar_genero_2(letra)

while (valor == False):
    letra = input("Ingrese genero [F|M|X]: ")
    valor = validar_genero_2(letra)
#FIN validacion de genero


print(valor)
