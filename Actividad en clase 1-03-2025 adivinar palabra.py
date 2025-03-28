palabra = "caballo"

def adivinar_palabra():  
    palabra_usuario = input("ingresa una palabra: ").lower()
    if palabra_usuario == palabra:
        print("verdadera.")
    else:
        print("falso.")

adivinar_palabra()  
 
