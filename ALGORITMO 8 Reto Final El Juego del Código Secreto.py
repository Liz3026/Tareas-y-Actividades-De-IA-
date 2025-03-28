import random
import operator

def generar_codigo_secreto():
    codigo_secreto = {}
    operadores = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '//': operator.floordiv,
        '%': operator.mod,
        '**': operator.pow
    }

    for _ in range(5):
        clave = random.randint(1, 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operador = random.choice(list(operadores.keys()))
        expresion = f"{num1} {operador} {num2}"
        resultado = operadores[operador](num1, num2)
        codigo_secreto[clave] = (expresion, resultado)

    return codigo_secreto

def desafio_usuario(codigo_secreto):
    aciertos = 0
    for clave, (expresion, resultado) in codigo_secreto.items():
        print(f"¿Cuál es el resultado de {expresion}?")
        respuesta = float(input("Ingrese su respuesta: "))
        if respuesta == resultado:
            print("Correcto!")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta correcta es {resultado}")

    return aciertos == len(codigo_secreto)

def main():
    codigo_secreto = generar_codigo_secreto()
    if desafio_usuario(codigo_secreto):
        print("Código Descifrado!")
    else:
        print("Acceso Denegado")

if __name__ == "__main__":
    main()