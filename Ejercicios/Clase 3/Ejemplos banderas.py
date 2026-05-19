# Ejemplos banderas
# 5 3 2 8 7
maximo = None
minimo = None
bandera = False

while True:
    numero = input("Ingrese un numero natural, cero para salir: ")
    numero = int(numero)
    
    if(bandera == False):
        minimo = numero
        maximo= numero
        bandera = True
    
    if(numero < minimo and numero != 0):
        minimo = numero
        
    if(numero > maximo):
        maximo = numero
        
    if(numero == 0):
        break
    
print(minimo)
print(maximo)

# bandera = False
# match :
#     case 1 #cargo los datos
#         #cargo los datos
#         bandera = True
#     case 2 #mostrar los datos
#         if(bandera == True):
#             #muestro los datos
#         else:
#             #Informo que se deben cargar los datos previamente
#     
#     case 3 # Salir