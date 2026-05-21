from libreria.Funciones import *

numero_uno = input("Ingrese el primer numero a sumar: ")
numero_dos = input("Ingrese el segundo numero a sumar: ")

numero_uno = float(numero_uno)
numero_dos = float(numero_dos)

resultado = sumar(numero_uno, numero_dos)
print(f"El resultado de la suma es: {resultado}")


num_uno = input("Ingrese el primer numero a restar: ")
num_dos = input("Ingrese el segundo numero a restar: ")

num_uno = float(num_uno)
num_dos = float(num_dos)

diferencia = restar(num_uno,num_dos)
print(f"El resultado de la resta es {diferencia}")


num_uno = int(input("Ingrese el primer numero a multiplicar: "))
num_dos = int(input("Ingrese el segundo numero a multiplicar: "))

producto = multiplicar(num_uno, num_dos)
print(f"El resultado de la multiplicacion es: {producto}")


num_uno = int(input("Ingrese el primer numero a dividir: "))
num_dos = int(input("Ingrese el segundo numero a dividir: "))

resultado = dividir(num_uno, num_dos)
print(f"El resultado de la division es: {resultado}")

# INICIO validacion de genero
letra = input("Ingrese un caracter: ")
valor = validar_genero(letra)

while (valor == False ):
    letra = input("Ingrese un genero [F|M|X]: ")
    valor = validar_genero(letra)
#FIN validacion de genero

print(valor)

cadena = input("Ingrese un nombre: ")

valor = es_alpha(cadena)

if valor == True:
    print(cadena)
else:
    print(f"El dato ingresado: {cadena}, no es un nombre valido")

'''
#INICIO validacion de genero
letra = input("Ingrese genero [F|M|X]: ")
valor = validar_genero_2(letra)

while (valor == False):
    letra = input("Ingrese genero [F|M|X]: ")
    valor = validar_genero_2(letra)
#FIN validacion de genero


print(valor)
'''

numero = int(input("Ingrese un número: "))
print(f"El número es {determinar_par_impar(numero)}") 

caracter = input("Caracter: ")
valor = get_Char(caracter)
print(valor)

num = input("Ingrese un número: ")
valor = validar_num(num)
print(valor)

patente = input("Patente: ")
valor = validar_patente(patente)

print(valor)

numero = input("Numero: ")
valor = validar_numeros(numero)

print(valor)

print(factorial_while(5))

caracteres = input("Ingrese caracteres: ")
valor = validar_correo(caracteres)

print(valor)

consultar_caracteres = input("Ingrese un numero: ")
respuesta = es_float(consultar_caracteres)
print(respuesta)

letra = input("Ingrese una letra: ")
valor = get_Char(letra)
while valor == False:
    letra = input("Ingrese una letra: ")
    valor = get_Char(letra)

letra = convertir_a_minuscula(letra)
print(letra)

letra = input("Ingrese una letra: ")
letra = convertir_a_mayuscula(letra)
print(letra)

cadena = input("Ingrese un nombre: ")
cadena = str_upr(cadena)

print(cadena)

mi_lista = [8, 1, 5, 6, 2, 10, 4, 9, 3, 7]
lista_ordenada = ordenar_lista_asc(mi_lista)           

print("LISTA ORDENADA DE MANERA ASCENDENTE")

for i in range(len(lista_ordenada)):
    print(f"indice: {i} - dato: {lista_ordenada[i]}")