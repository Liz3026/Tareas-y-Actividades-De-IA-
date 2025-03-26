palabra = input("Escribe una frase: ")
contador = 0
vocales = "aeiouAEIOU"
for letra in palabra:
    if letra in vocales:
        contador += 1
print("Numero de vocales:", contador)
