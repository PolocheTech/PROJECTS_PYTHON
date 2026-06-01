def numeros_par_impar():

    usuario = input("Ingresar numeros separados por coma: ").split(",")

    for i in usuario:
        try: 
            if int(i) % 2 == 0:
                print(f"El numero {i} es par")
            else:
                print(f"El numero {i} es impar")
        except ValueError:
            print("[Solo ingresa 'numeros' no ingreses letras]")

numeros_par_impar()