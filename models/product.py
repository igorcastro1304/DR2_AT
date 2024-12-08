class Product:
    def __init__(self, id, description, quantity, price):
        self.id = id
        self.description = description
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.id} - {self.description}({self.quantity}, R$ {self.price})"