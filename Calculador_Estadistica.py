
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

import pandas as pd
from excepciones import ListaVaciaError
import os

#Identificar la ruta actual de nuestro directorio
def ruta_rel(ruta):
    d = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(d, ruta)

#Leer el archivo csv
def leer_csv(archivo_csv):
    """Lee un archivo CSV y retorna un DataFrame."""
            
    try:
        df = pd.read_csv(ruta_rel(archivo_csv))
        if df.empty:
            raise ListaVaciaError()
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {archivo_csv}") from e
    except pd.errors.EmptyDataError as e:
        raise ValueError(f"El archivo está vacío o es inválido: {archivo_csv}") from e
    except pd.errors.ParserError as e:
        raise ValueError(f"Error al analizar el archivo: {archivo_csv}") from e

# Identifica el tipo de columnas diferenciandolo entre categoricas y cuantitativas
def identificar_columnas(df):
    """Identifica y retorna las columnas numéricas y categóricas."""
    columnas_numericas = df.select_dtypes(include='number').columns.tolist()
    columnas_categoricas = df.select_dtypes(exclude='number').columns.tolist()
    
    if not columnas_numericas:
        raise ValueError("No se encontraron columnas numéricas en el archivo CSV.")
    
    return columnas_numericas, columnas_categoricas



def calcular_media_csv(archivo_csv):
    """Calcula la media de las columnas numéricas en un archivo CSV."""
    df = leer_csv(archivo_csv)
    columnas_numericas, _ = identificar_columnas(df)
    return df[columnas_numericas].mean()



def calcular_mediana_csv(archivo_csv):
    """Calcula la mediana de las columnas numéricas en un archivo CSV."""
    df = leer_csv(archivo_csv)
    columnas_numericas, _ = identificar_columnas(df)
    return df[columnas_numericas].median()



