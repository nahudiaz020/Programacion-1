def mostrar_menu():

    print("\n----- MENU -----")
    print("1. Saludar")
    print("2. Mostrar numero")
    print("3. Salir")


opcion = 0

while opcion != 3:

    mostrar_menu()

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:

        print("Hola usuario")

    elif opcion == 2:

        numero = int(input("Ingrese un numero: "))
        print(f"El numero ingresado es: {numero}")

    elif opcion == 3:

        print("Saliendo del programa...")

    else:

        print("Opcion invalida")

#---------------------------con match----------------------------------------

def mostrar_menu():

    print("\n----- MENU -----")
    print("1. Saludar")
    print("2. Mostrar numero")
    print("3. Salir")


opcion = 0

while opcion != 3:

    mostrar_menu()

    opcion = int(input("Ingrese una opcion: "))

    match opcion:

        case 1:

            print("Hola usuario")

        case 2:

            numero = int(input("Ingrese un numero: "))
            print(f"El numero ingresado es: {numero}")

        case 3:

            print("Saliendo del programa...")

        case _:

            print("Opcion invalida")