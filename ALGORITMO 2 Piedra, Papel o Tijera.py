import random

def juego_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)

    usuario = input("Escribe tu jugada (piedra, papel o tijera): ").lower()

    while usuario not in opciones:
        usuario = input("Jugada inválida. Escribe tu jugada (piedra, papel o tijera): ").lower()

    print(f"\nComputadora: {computadora}")
    print(f"Usuario: {usuario}\n")

    if usuario == computadora:
        print(f"Empate! Ambos eligieron {usuario}.")
    elif usuario == "piedra":
        if computadora == "tijera":
            print("Piedra aplasta tijera. ¡Ganaste!")
        else:
            print("Papel cubre piedra. ¡Perdiste!")
    elif usuario == "papel":
        if computadora == "piedra":
            print("Papel cubre piedra. ¡Ganaste!")
        else:
            print("Tijera corta papel. ¡Perdiste!")
    elif usuario == "tijera":
        if computadora == "papel":
            print("Tijera corta papel. ¡Ganaste!")
        else:
            print("Piedra aplasta tijera. ¡Perdiste!")

def main():
    jugar_de_nuevo = "s"
    while jugar_de_nuevo.lower() == "s":
        juego_piedra_papel_tijera()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    print("¡Hasta luego!")

if __name__ == "__main__":
    main()