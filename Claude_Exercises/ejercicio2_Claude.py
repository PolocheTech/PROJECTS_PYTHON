def contador_vocales():
    usuario = input("Ingresar frase: ").lower()
    contador = 0
    vocales = "aeiou"

    for i in usuario:
        if i in vocales:
            contador += 1

    if contador > 0:
        print(f"La palabra tiene {contador} vocales")
    else:
        print("La palabra no contiene vocales")

contador_vocales()