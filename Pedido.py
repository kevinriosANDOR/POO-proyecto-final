class Pedido:
    def __init__(self, nombre, precio, estado, objetos, cliente):
        super().__init__(nombre, precio)
        self.estado = estado
        self.objetos = objetos
        self.cliente = cliente
    