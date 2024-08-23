
# Idea: ademas de sacar las variables para un csv , la diea es que tambien las grafque 
# de forma automatica


def calcular_media(numeros):
    try:
        return sum(numeros) / len(numeros)
    except ZeroDivisionError as e:
        raise ValueError("La lista de números no puede estar vacía.") from e

def calcular_mediana(numeros):
    try:
        numeros_ordenados = sorted(numeros)
        n = len(numeros)
        mitad = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:
            return numeros_ordenados[mitad]
    except IndexError as e:
        raise ValueError("No se puede calcular la mediana de una lista vacía.") from e

def Moda(a):
    return None

def Desviacion_std(a):
    return None

def Varianza(a):
    return None

