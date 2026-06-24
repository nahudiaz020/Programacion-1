def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b


operaciones = (sumar, restar, multiplicar)

resultado_suma = operaciones[0](10, 5)
resultado_resta = operaciones[1](10, 5)
resultado_multiplicacion = operaciones[2](10, 5)

print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")
print(f"Resultado de la multiplicacione: {resultado_multiplicacion}")

#---------------------- DICCIONARIOS ------------------------------

operaciones = {
    "sumar" : sumar,
    "restar" : restar,
    "multiplicar" : multiplicar
}

resultado_multiplicacion = operaciones["multiplicar"](10, 5)
resultado_suma = operaciones["sumar"](10, 5)
resultado_resta = operaciones["restar"](10, 5)

print(f"Resultado de la multiplicación: {resultado_multiplicacion}")
print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")

#---------------------- FUNCION COMO PARAMETRO ------------------------------

def operar(a, b, funcion):
    return funcion(a, b)

def aplicar_operacion(numero, funcion):
    resultado = funcion(numero)
    return resultado

def duplicar(x):
    return x * 2

def triplicar(x):
    return x * 3

resultado_suma = operar(10, 5, sumar)
resultado_resta = operar(10, 5, restar)

print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")

# Usando la función aplicar_operacion
resultado1 = aplicar_operacion(5, duplicar)
resultado2 = aplicar_operacion(5, triplicar)

print(resultado1) # Imprime 10
print(resultado2) # Imprime 15

#---------------------- FUNCION COMO PARAMETRO 2 ------------------------------

def filtrar_lista(funcion, lista):
    """Filtra una lista según una función de predicado."""
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado

def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5]
resultado = filtrar_lista(es_par, numeros)
print(resultado)
# Salida: [2, 4]

#---------------------- FUNCION DEVUELVE OTRA FUNCION ------------------------------

def funcion_externa(x):
    return x + 5

def retornar_funcion( ):
    return funcion_externa

# Obtener la función externa
mi_funcion = retornar_funcion()

# Usar la función externa
resultado = mi_funcion(10)
print(resultado)

#---------------------- FUNCION RETORNA FUNCIONES DE FORMATEO DE CADENAS ------------------------------

def formatear_mayusculas(texto):
    return texto.upper()

def formatear_minusculas(texto):
    return texto.lower()

def formatear_titulo(texto):
    return texto.title()

# Función que retorna la función de formateo deseada
def obtener_formateador(tipo):
    if tipo == 'mayusculas':
        return formatear_mayusculas
    elif tipo == 'minusculas':
        return formatear_minusculas
    elif tipo == 'titulo':
        return formatear_titulo
    else:
        raise ValueError("Tipo de formateo no válido")
    
# Ejemplo de uso
texto = "hola mundo"

# Obtener la función de formateo deseada
formateador = obtener_formateador('mayusculas')
resultado = formateador(texto)
print(f"Texto en mayúsculas: {resultado}") # Salida: HOLA MUNDO

formateador = obtener_formateador('minusculas')
resultado = formateador(texto)
print(f"Texto en minússculas: {resultado}") # Salida: hola mundo

formateador = obtener_formateador('titulo')
resultado = formateador(texto)
print(f"Texto en título: {resultado}") # Salida: Hola Mundo

#---------------------- FUNCION LAMBDA ------------------------------

suma = lambda a, b: a + b
print(suma(2, 4)) # 6

suma = (lambda a, b, c: a + b + c)(2, 3, 4)
print(suma) # 9

# Función normal
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado) # Salida 8

# Función lambda
suma_lambda = lambda a, b: a + b

resultado_lambda = suma_lambda(3, 5)
print(resultado_lambda) # Salida: 8

#---------------------- LAMBDA COMO PARAMETRO ------------------------------

def validar(valor, condicion):
    return condicion(valor)

es_positivo = lambda x: x > 0
print(validar(10, es_positivo)) # Salida: True
print(validar(-5, es_positivo)) # Salida: False