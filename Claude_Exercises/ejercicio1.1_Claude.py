def calculadora_basica(numero1: float, operacion: str, numero2: float):

    if operacion == "+":
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "/":
        return numero1 / numero2
    elif operacion == "*":
        return numero1 * numero2
    else:
        return "Operacion no valida"
    
num1 = int(input("Ingresar numero1: "))
operacion = str(input("Operacion +, -, /, *: "))
num2 = int(input("Ingresar numero2: "))

print(f"resultado: {calculadora_basica(num1, operacion, num2)}")