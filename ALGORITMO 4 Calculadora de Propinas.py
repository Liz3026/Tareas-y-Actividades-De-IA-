def calcular_propina():
    total_cuenta = float(input("¿Cuál es el total de su cuenta? $"))

    print("¿Cuánto propina quiere dejar?")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")

    opcion = int(input("Ingrese su opción (1, 2 o 3): "))

    if opcion == 1:
        propina = total_cuenta * 0.10
    elif opcion == 2:
        propina = total_cuenta * 0.15
    elif opcion == 3:
        propina = total_cuenta * 0.20
    else:
        print("Opción inválida. Se calculará una propina del 10%.")
        propina = total_cuenta * 0.10

    total_pagar = total_cuenta + propina

    print(f"La propina es: ${propina:.2f}")
    print(f"El total a pagar es: ${total_pagar:.2f}")

def main():
    calcular_propina()

if __name__ == "__main__":
    main()
