from bebida import Bebida


class refresco_natural(Bebida):
    def __init__(self, nombre, precio, tamaño, refresco_natural):
        super().__init__(
            nombre, precio, tamaño, gaseosa=False, refresco_natural=refresco_natural
        )

    def calcular_precio(self):
        return super().calcular_precio()
