
numero = int(input("Por favor, ingresa un número entero positivo: "))

if numero > 0:
    suma = 0  
    for i in range(1, numero + 1):
        suma += i  
    print(f"La suma de todos los números desde 1 hasta {numero} es: {suma}")
else:
    
    print("Error: Debes ingresar un número entero positivo.")
