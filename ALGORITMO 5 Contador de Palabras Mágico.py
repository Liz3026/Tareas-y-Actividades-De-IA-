def contar_palabras():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()

    contador = 0
    for palabra in palabras:
        contador += 1

    print(f"La frase tiene {contador} palabras.")

def contar_palabras_alternativo():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()

    print(f"La frase tiene {len(palabras)} palabras.")

def main():
    print("Contador de palabras")
    print("1. Usando for")
    print("2. Usando len()")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        contar_palabras()
    elif opcion == 2:
        contar_palabras_alternativo()
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()