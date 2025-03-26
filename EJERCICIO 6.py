saldo = 1000
opcion = ""

while opcion != "salir":
    print("\n1. Consultar saldo\n2. Retirar\n3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Saldo actual:", saldo)
    elif opcion == "2":
        cantidad = int(input("¿Cuanto deseas retirar?: "))
        if cantidad <= saldo:
            saldo -= cantidad
            print("Retiro exitoso. Nuevo Saldo:", saldo)
        else:
            print("Fondos insuficientes.")
    elif opcion == "3":
        opcion = "salir"
    else:
        print("Opcion no valida.")
       

