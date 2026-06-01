def tabla_multiplicar_ciclo(numero_multiplicador: int):
    for i in range (1, 11):
        resultado = numero_multiplicador * i
        print(f"{numero_multiplicador} x {i} = {resultado}")

numero = int(input(f"Tabla del numero: "))
tabla_multiplicar_ciclo(numero)