class Product:
    def __init__(self, id, description, quantity, price, min_quantity = 50):
        self.id = id
        self.description = description
        self.quantity = quantity
        self.price = price
        self.min_quantity = min_quantity

    def __str__(self):
        return f"{self.id} - {self.description}({self.quantity}, R$ {float(self.price):.2f}); Quantidade Mínima: {self.min_quantity} {"- repor estoque " if self.quantity < self.min_quantity else ""}"
    