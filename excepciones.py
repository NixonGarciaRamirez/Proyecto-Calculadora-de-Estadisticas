class ErrorDeCalculo(Exception):
    """Excepción base para errores en la calculadora."""
    pass

class ListaVaciaError(ErrorDeCalculo):
    """Excepción cuando la lista de números está vacía."""
    def __init__(self):
        super().__init__("La lista de números no puede estar vacía.")
