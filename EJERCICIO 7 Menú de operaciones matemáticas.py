op = input("Elige una operacion (+, -, *, /): ")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

match op:
    case "+":
        print("resultado:", a + b)
    case "-":
        print("resultado:", a - b)
    case "*":
        print("resultado:", a * b)
    case "/":
        print("resultado:", a / b if b != 0 else " no se puede dividir entre cero")
    case "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        print("resultado:", a / b)
    case _:
        print("operacion no valida.")
        
