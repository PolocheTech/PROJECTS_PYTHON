def validar_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad\n>>> "))
            if edad < 0 or edad > 120:
                print("La edad es erronea")
            else:
                return edad
        except ValueError:
            print("Error: valor incorrecto intenta otra vez.")

def main():
    nombre = input("Ingresa tu nombre\n>>> ")
    edad_persona = validar_edad()

main()