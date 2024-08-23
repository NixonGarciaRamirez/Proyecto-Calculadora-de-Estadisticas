from Calculador_Estadistica import calcular_media, calcular_mediana
from excepciones import ListaVaciaError

if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]
    try:
        media = calcular_media(numeros)
        mediana = calcular_mediana(numeros)
        print(f"Media: {media}")
        print(f"Mediana: {mediana}")
    except ListaVaciaError as e:
        print(e)
