import random

def contar_chiste():
    chistes = [
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas",
        "¿Por qué el computador fue al doctor? Tenía un virus",
        "¿Por qué el perro fue al veterinario? Porque estaba sintiendo un poco raro",
        "¿Por qué el niño llevó una escalera a la escuela? Quería llegar a un nivel más alto",
        "¿Por qué el café fue al psicólogo? Porque estaba sintiendo un poco amargo"
    ]

    chiste_aleatorio = random.choice(chistes)
    print(chiste_aleatorio)

def main():
    print("Presiona ENTER para escuchar un chiste")
    input()
    contar_chiste()

if __name__ == "__main__":
    main()
