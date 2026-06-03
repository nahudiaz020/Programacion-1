'''
Hacer una funcion que reciba una cadena de caracteres y convierta la misma a mayusculas, 
los caracteres de dicha cadena que ya estan en mayusculas deberan quedar en mayusculas.
La funcion debera retornar la misma cadena en mayusculas.
'''
from libreria.Funciones import * 

def str_upr(cadena):
    cadena_aux = ""
    for letra in cadena:
        cadena_aux = cadena_aux + convertir_a_mayuscula(letra)
        

    return cadena_aux


cadena = input("Ingrese un nombre: ")

cadena = str_upr(cadena)

print(cadena)



