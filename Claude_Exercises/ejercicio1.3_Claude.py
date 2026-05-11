import random

def adivina_el_numero():
    
    numero_ganador = random.randint(0, 5)
    intentos = 7

    for intento in range(1, intentos + 1):
        jugador = int(input("Ingresar numero 0 - 5: "))
        if jugador == numero_ganador:
            print("Felicidades Ganaste")
            break
        elif jugador < numero_ganador:
            print ("Muy bajo")
        else:
            print("Muy alto")
    else:
        print("Se acabaron los intentos")
    
adivina_el_numero()