def saludo(nombre):
    print("¡Hola, {}, ¡Bienvenido!".format(nombre))
    print("Muchas gracias por participar.")
    print("Espero que la pases bien.")

    return None

nombre_usuario = input("Introduzca su nombre: ")

saludo(nombre_usuario)
