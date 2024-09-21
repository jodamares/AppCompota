#descuento.py
from producto import Producto

class Descuento:
    def __init__(self) -> None:
        self.producto = Producto()
        self.__cantidad = 0
        self.__descuento = 0
        self.__valorBruto = 0
        self.__total = 0
        self.__aplicarDesc = 0

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_descuento(self, descuento):
        self.__descuento = descuento

    def get_descuento(self):
        return self.__descuento

    def set_valorBruto(self, valorBruto):
        self.__valorBruto = valorBruto

    def get_valorBruto(self):
        return self.__valorBruto

    def set_aplicarDesc(self, aplicarDesc):
        self.__aplicarDesc = aplicarDesc

    def get_aplicarDesc(self):
        return self.__aplicarDesc

    def set_total(self, total):
        self.__total = total

    def get_total(self):
        return self.__total

    def calcular_descuento(self):
        # Condición de descuento
        if self.producto.get_marca() == "rostington":
            if self.get_cantidad() < 100:
                self.set_descuento(0.2)
            elif self.get_cantidad() <= 200:
                self.set_descuento(0.25)
            else:
                self.set_descuento(0.30)
        else:
            if self.get_cantidad() < 100:
                self.set_descuento(0.15)
            elif self.get_cantidad() <= 200:
                self.set_descuento(0.35)
            else:
                self.set_descuento(0.50)

    def aplicar_descuento(self):
        # Llamamos al método para actualizar el valor unitario basado en la marca
        self.producto.actualizar_valor()

        # Calcular el valor bruto
        valor_bruto = self.get_cantidad() * self.producto.get_valorUni()
        self.set_valorBruto(valor_bruto)

        # Aplicar descuento
        aplicar_desc = valor_bruto * self.get_descuento()
        self.set_aplicarDesc(aplicar_desc)

        # Calcular total
        total = valor_bruto - aplicar_desc
        self.set_total(total)
        print(f"Total a pagar: {self.get_total()}")


if __name__ == "__main__":
    descuento = Descuento()
    descuento.producto.set_marca("rostington")  # Se asigna la marca
    descuento.set_cantidad(20)  # Se asigna la cantidad
    descuento.calcular_descuento()  # Calcula el descuento
    descuento.aplicar_descuento()  # Aplica el descuento y calcula el total
