num = int(input("Ingrese un número: "))
factorial = 1

while num > 1:
    factorial *= num
    num -= 1

print(f"El factorial es {factorial}")   

#------------------------------- resuelto por profe --------------------------------------------------

def factorial_while(numero):
    resultado = 1
    # Mientras n sea mayor que 1 sigue multiplicando
    while numero > 1:
        resultado = resultado * numero
        numero = numero - 1  # Restamos 1 en cada iteracion
    return resultado

print(factorial_while(5))

#numero    = 5 4 3   2   1
#resultado = 1 5 20 60 120