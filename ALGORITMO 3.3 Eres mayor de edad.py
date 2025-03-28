def edad_para_entrar():
    edad = int(input("¿Cuál es tu edad? "))

    if edad < 18:
        print("¡Lo siento, no puedes entrar!")
    elif 18 <= edad <= 21:
        print("Puedes entrar, pero sin bebidas alcohólicas")
    else:
        print("¡Bienvenido!")

def main():
    edad_para_entrar()

if __name__ == "__main__":
    main()