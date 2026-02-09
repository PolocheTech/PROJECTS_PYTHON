lista_numeros = [1,2,3,4,5,6,7,8]

def analizar_numeros(lista_numeros):
    numeros_pares = 0
    numeros_impares = 0
    promedio_numeros = 0
    numero_mayor = 0
    numero_menor = 1
    for i in (lista_numeros):
        if i % 2 == 0: numeros_pares += 1
        elif i % 2 == 1: numeros_impares += 1
        if i > numero_mayor: numero_mayor = i
        if i < numero_menor: numero_menor = i
        promedio_numeros += i
    return numeros_pares, numeros_impares, numero_mayor, numero_menor, promedio_numeros

print(analizar_numeros(lista_numeros))