palabra = input("Escribe una frase: ")
contador = 0

for letra in palabra:
    if letra != " ":
        contador += 1

print("Numero de letras (sin espacios):", contador)
