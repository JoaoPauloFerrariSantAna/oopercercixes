from cliente import Cliente

class Pedido():
    def __init__(self, cliente: Cliente, lista_items: dict) -> None:
        self.cliente = cliente
        self.lista_items = lista_items
    
    def calculate_total(self) -> float:
        total = 0

        for k in self.lista_items:
            total += self.lista_items[k]

        return total