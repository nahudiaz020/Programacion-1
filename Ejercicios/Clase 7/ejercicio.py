# Hacer una funcion en el cual el primer caracter de una cadena sea mayuscula 

from libreria.Funciones import *

def str_upr_char2(cadena) -> str: #'mundial' cadena1[0] = 'm', cadena1[1] = 'a'...
    """
        Esta función recibe una cadena de caracteres y convierte la 
        primer letra de la palabra en mayúscula. Si es una frase,
        convierte la primer letra de cada palabra en mayúscula.
        
        Convierte la cadena de caracteres en una lista de caracteres
        para recorrer cada posición una a una.
        
        Luego, una vez recorrida y capitalizada las letras correspondientes
        concatena en una nueva variable la palabra o frase. 
        
        Args: 
            cadena: cadena de caracteres
        return: 
            cadena_capital: la cadena capitalizada.
        
        
    """
    
    cadena1 = list(cadena) #['m','u','n','d','i','a','l']
    cadena_capital = ''
    i = 0

    for letra in range(len(cadena1)): #letra = 0 es una variable entera
        
        cadena_ord = ord(cadena1[letra])
        if i == 0: 
            cadena1[letra] = str_upr(cadena1[letra])
            i += 1
        elif i > 0 and (cadena1[letra] == ' ' or cadena_ord == 32): 
            cadena1[letra+1] = str_upr(cadena1[letra+1])
        else: 
            print('no es primera letra luego del espacio.')
    
    for letra in range(len(cadena1)):
        cadena_capital += str(cadena1[letra])
    return cadena_capital

def str_upr_char(cadena) -> str:
    """
        Esta función recibe una cadena de caracteres y convierte la 
        primer letra de la palabra en mayúscula. Si es una frase,
        convierte la primer letra de cada palabra en mayúscula.
        
        Mientras verifica cada letra de la cadena busca por 
        espacios en blanco para luego capitalizar la letra que le
        sigue. Hace ambos procesos en un mismo recorrido.
        
        Args: 
            cadena: cadena de caracteres
        return: 
            cadena_capital: la cadena capitalizada.
        
        
    """
    cadena_capital = ''
    bandera = False
    i = 0

    for letra in cadena: #'mundial' 0 = letra = 'm', 1 = letra = 'a'...
        #letra contiene cada letra de la palabra en cada iteración
        cadena_ord = ord(letra)
        if i == 0: 
            cadena_capital += str_upr(letra)
            i += 1
        elif i > 0 and (letra == ' ' or cadena_ord == 32):
            bandera = True 
        elif bandera == True: 
            cadena_capital += str_upr(letra)
            bandera = False
        else: 
            print('no es primera letra luego del espacio.')
            cadena_capital += letra
    
    #for letra in range(len(cadena1)):
     #   cadena_capital += str(cadena1[letra])
    return cadena_capital