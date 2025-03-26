respuesta = ""
intentos = 0
max_intentos = 3
while respuesta != "python" and intentos < max_intentos:
    respuesta = input("¿Cuál es el mejor lenguaje de programación?: ")
    intentos += 1
if respuesta == "python":
    print("¡Correcto!")
else:
    print("Lo siento, has agotado tus intentos.")
