from producto import Producto


class Bebida(Producto):
    def __init__(self, nombre, precio, tamaño_bebida, gaseosa, refresco_natural):
        super().__init__(nombre, precio)
        self.tamaño = tamaño_bebida
        self.gaseosa = gaseosa
        self.refresco_natural = refresco_natural
