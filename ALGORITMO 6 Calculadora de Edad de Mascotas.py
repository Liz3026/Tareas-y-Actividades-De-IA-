def edad_humana():
    print("Conversor de edad animal a humana")
    print("1. Perro")
    print("2. Gato")

    opcion = int(input("Ingrese su opción: "))

    edad_animal = int(input("Ingrese la edad de su mascota: "))

    if opcion == 1:
        edad_humana = edad_animal * 7
        print(f"La edad de su perro en años humanos es: {edad_humana} años")
    elif opcion == 2:
        edad_humana = edad_animal * 5
        print(f"La edad de su gato en años humanos es: {edad_humana} años")
    else:
        print("Opción inválida")

def main():
    edad_humana()

if __name__ == "__main__":
    main()