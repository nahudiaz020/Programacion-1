# Desarrollar una función que reciba una patente que tendrá tres letras y tres números o tres números y tres
# letras. Deberá retornar auto o moto, si la patente es tres letras y tres números o tres números y tres letras
# respectivamente.

def validar_patente(dato: str) -> str:
    """Determina si una patente corresponde a un auto o una moto
según su formato (3 letras y 3 numeros o 3 numeros y 3 letras).
    Args:
        dato (str): Patente compuesta por 6 caracteres

    Returns:
        str: devuelve "AUTO" si la patente tiene formato de 3 letras  y 3 numeros, 
            devuelve "MOTO" si tiene formato de 3 numeros y 3 letras
    """
    contador = 0
    for letra in dato:
        bandera_auto = False
        bandera_moto = False
        if (contador < 3):
            if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122):
                bandera_auto = True
                
        elif (contador < 6):
            if (ord(letra) >= 48 and ord(letra) <= 57):
                bandera_auto = True
    
        if (contador < 3):
            if (ord(letra) >= 48 and ord(letra) <= 57):
                bandera_moto = True
        elif (contador < 6):
            if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) >= 97 and ord(letra) <= 122):
                bandera_moto = True
                
        contador += 1
        
        if(bandera_auto == True):
            retorno = "AUTO"
        if(bandera_moto == True):
            retorno = "MOTO"
        
    return retorno

patente = input("Patente: ")
valor = validar_patente(patente)

print(valor)