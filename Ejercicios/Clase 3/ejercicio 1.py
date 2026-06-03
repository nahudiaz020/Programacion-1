# Desarrollar una función que determine si un número entero es par o impar. Debe recibir un número por parámetro y devolver True en caso de que sea par, de lo contrario devolverá False.

# def determinar_par_impar (numero):
#     if numero % 2 == 0:
#         return "par"
#     else :
#         return "impar"
    
def determinar_par_impar (numero):
    retorno = False
    if numero % 2 == 0:
        retorno = True
    return retorno

numero = int(input("Ingrese un número: "))
print(f"El número es {determinar_par_impar(numero)}") 