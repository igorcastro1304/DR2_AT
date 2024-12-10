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
    
    def sort_products(self, ascending=True):
        self.stock.sort(key=lambda product: product.quantity, reverse=not ascending)

    def search_by_id(self, id):
        return next((product for product in self.stock if product.id == id), f"Nenhum medicamento com o ID ({id}) encontrado!")
    
    def search_by_description(self, description):
        matched_products =  [product for product in self.stock if description.lower() in product.description.lower()]

        if not matched_products:
            return f"Nenhum produto encontrado com a descrição ('{description}')."
        
        return "\n".join(str(product) for product in matched_products)
    
    def remove_product_by_id(self, id):
        for product in self.stock:
            if product.id == id:
                self.stock.remove(product)
                return f"Medicamento com o ID ({id}) removido com sucesso!"
            
        return f"Nenhum medicamento com o ID ({id}) encontrado!"
    
    def list_soldout_products(self):
        soldout_products = []

        for product in self.stock:
            if product.quantity == 0:
                soldout_products.append(product)

        return soldout_products