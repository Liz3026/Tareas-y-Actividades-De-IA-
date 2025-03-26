palabra = input("Escribe una frase: ")
contador = 0
for letra in palabra:
    if letra.isalpha():  # Solo cuenta letras
        contador += 1
print("Numero de letras:", contador)
