edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("Edad inválida. Por favor, introduce una edad positiva.")
elif edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad <= 30:
    print("Eres un adulto joven.")
elif edad < 60:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
    
