def numeros_par_impar():

    usuario = input("Ingresar numero: ")
    numeros = "0123456789"

    for i in usuario: 
        if i in numeros:
            if int(i) % 2 == 0:
                print(f"El numero {i} es par")
            elif int(i) % 2 == 1:
                print(f"El numero {i} es impar")
            else:
                print("Valor incorrecto")

numeros_par_impar()