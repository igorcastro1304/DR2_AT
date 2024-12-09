from models.product import Product

class ProductController:
    def __init__(self):
        self.stock = []

    def add_product(self, id, description, quantity, price):
        new_product = Product(id, description, quantity, price)
        self.stock.append(new_product)

    def list_products(self):
        for product in self.stock:
            print(product)
    
