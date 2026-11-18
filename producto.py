class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
class Plato(Producto):
    def __init__(dias_venta):
        super().__init__(nombre, precio)
        self.dias_venta = dias_venta      