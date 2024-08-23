filtrar_pares = lambda numeros: [n for n in numeros if n % 2 == 0]

def es_multiplo_de(numeros, x):
    return [n for n in numeros if n % x == 0]
