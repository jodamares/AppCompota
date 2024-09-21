#producto.py
class Producto:
    def __init__(self) -> None:
        self._marca = None  # Inicializamos los atributos
        self._valorUni = 0.0  # Inicializamos con un valor numérico

    def set_marca(self, marca):
        self._marca = marca

    def get_marca(self):
        return self._marca

    def set_valorUni(self, valorUni):
        self._valorUni = valorUni

    def get_valorUni(self):
        return self._valorUni

    def actualizar_valor(self):
        if self.get_marca() == "rostington":
            self.set_valorUni(5000)
        else:
            self.set_valorUni(10000)
