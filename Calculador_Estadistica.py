
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


### Para un CSV

import csv
from excepciones import ListaVaciaError

def leer_csv(archivo_csv):
    """Lee un archivo CSV y devuelve una lista de números."""
    try:
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            numeros = [float(row[0]) for row in reader if row]
        if not numeros:
            raise ListaVaciaError()
        return numeros
    except FileNotFoundError as e:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {archivo_csv}") from e
    except ValueError as e:
        raise ValueError(f"El archivo contiene valores no numéricos: {archivo_csv}") from e


def calcular_media_csv(archivo_csv):
    """Calcula la media de los números en un archivo CSV."""
    numeros = leer_csv(archivo_csv)
    return sum(numeros) / len(numeros)

def calcular_mediana_csv(archivo_csv):
    """Calcula la mediana de los números en un archivo CSV."""
    numeros = leer_csv(archivo_csv)
    numeros_ordenados = sorted(numeros)
    n = len(numeros)
    mitad = n // 2
    if n % 2 == 0:
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    else:
        return numeros_ordenados[mitad]


