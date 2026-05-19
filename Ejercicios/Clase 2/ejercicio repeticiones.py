# Fácil para aprender y de usar en mi lógica de programación para resolver problemas.

print('Municipalidad de Avellaneda')
print(' ')
contador = 0
contador_ciclos = 0
acumulador = 0

edad_min = 100
edad_max = 0

usuario = input('Ingresar Usuario: ')
contrasena = input('Ingresar Contraseña: ')
while usuario != 'admin' or contrasena != '1407':
    print('Error. Ingrese correctamente usuario o contraseña:') 
    usuario = input('Ingresar Usuario: ')
    contrasena = input('Ingresar Contraseña: ')

#--- Programa Principal: 
while True: 
    seleccion = int(input('¿Qué deseas realizar: \n 1.Ingresar Información de Estudiante \n 2.Report'))

    match seleccion: 
        case 1: #Programa Ingreso de Estudiantes
            while True: 
                #Entradas: Valores que solicito al usuario.
                nombre = input('Ingresar tu nombre')
                edad = int(input('Ingresá tu edad'))

                #Proceso: Saber que rango de edad es.
                if edad <= 5:
                    rango_de_edad = 'Es un Bebé'
                    escuela = 'Jardin'
                        
                elif edad <= 10:
                    rango_de_edad = 'No es un bebé. Es un niñ@'
                    escuela = 'Primaria'
                    contador +=1

                elif edad <= 13:
                    rango_de_edad = 'Es un@ pre-adolescente'
                    escuela = 'Secundaria'

                elif edad <= 18:
                    rango_de_edad = 'Es un@ adolescente'
                    escuela = 'CBC'

                elif edad <= 25: 
                    rango_de_edad = 'Es un Jóven Adulto'
                    escuela = 'Universidad'
                else: 
                    rango_de_edad = 'Es un mayor de edad'
                    escuela = 'Trabajo'
                
                #Ver máximo y Mínimo'
                if edad > edad_max:
                    edad_max = edad
                
                if edad < edad_min: 
                    edad_min = edad
                #i = 0
                #for i in range(edad, 12, 1):
                #for i in range(edad):
                for i in range(edad, -1, -1):
                    #if i <= 4:
                        #continue
                    print(f'Año {i}-{i+1}')

                match escuela: 

                    case 'Jardin': 
                        print('Debe llevar delantal')
                    case 'Primaria':
                        print('Debe llevar Uniforme')
                    case 'Secundaria':
                        print('Debe llevar merienda')
                    case 'CBC':
                        print('Debe Preparar exámenes')
                    case 'Univesidad':
                        print('Debe llevar Vamos con equipo de mate')
                    case 'Trabajo':
                        print('Debe llevar almuerzo')


                #Tipos de datos.
                #Booleanos: True or False
                #Enteros: 12 
                #Float: 12.3 ó 4.5
                #Cadenas: 'c' o 'Cadenas de Caracteres' 
                print(f'Iteración:  {contador}')
                #Salida
                print(f"{nombre}, {rango_de_edad}, ya que tiene {edad} años")
                seguir = input('¿Desea continuar? s/n')
                while seguir != 's' and seguir !='n': 
                    seguir = input('Error. Ingrese "s" para continuar')
                if seguir == 'n':
                    acumulador += contador
                    contador = 0 
                    contador_ciclos += 1
                    break
        case 2: 
            print(f'Totalidad acumulada de ingresos por ciclo {contador_ciclos}: {acumulador}')
            print(f'Edad máxima: {edad_max} y edad mínima:  {edad_min}')

#----- Fin de Programa General
    print(' ')
    seguir = input('¿Volver al Menú? - s/n')
    while seguir != 's' and seguir !='n': 
        seguir = input('Error. Ingrese "s" para continuar')
    if seguir == 'n':
        print('¡Hasta Luego! - Cerrando Sesión')
        break

    