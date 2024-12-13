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
    
    def increase_quantity(self, product, quantity_to_increase):
        product.quantity += quantity_to_increase

        return product

    def decrease_quantity(self, product, quantity_to_decrease):
        if product.quantity >= quantity_to_decrease:
            product.quantity -= quantity_to_decrease
        else:
            return f"Não há estoque suficiente para retirar {product.description}"
        
        return product

    def update_minimum_limit(self, product, new_minimum_limit):
        product.min_quantity = new_minimum_limit

        return product
    
    def list_below_minimum_products(self):
        below_minimum_products = [product for product in self.stock if product.quantity < product.min_quantity]

        if below_minimum_products:
            print("Produtos abaixo do limite mínimo:")
            for product in below_minimum_products:
                print(product)
        else:
            print("Todos os produtos estão com o estoque regular.")

    def update_product_price(self, product, new_price):
        product.price = new_price

        return 
    
    def calculate_total_stock_value(self):
        total_stock_value = sum(product.price * product.quantity for product in self.stock)

        return total_stock_value
    
    def calculate_estimated_profit(self):
        total_profit = 0.0

        for product in self.stock:
            if product.price < 500.00:
                cost_percentage = 0.25
            elif 500.01 <= product.price <= 700.00:
                cost_percentage = 0.20
            else:
                cost_percentage = 0.15
            
            cost = product.price * cost_percentage
            profit_per_item = product.price - cost
            total_profit += profit_per_item * product.quantity
        
        return total_profit
    
    def make_general_report(self):
        print()
        print("------RELATÓRIO GERAL------")
        print()
        print(f"{'ID':<5} {'Descrição':<20} {'Quantidade':<10} {'Preço Venda':<15} {'Custo Unitário':<15} {'Lucro Unitário':<15}")
        print("-" * 80)

        for product in self.stock:
            if product.price < 500.00:
                cost_percentage = 0.25
            elif 500.01 <= product.price <= 700.00:
                cost_percentage = 0.20
            else:
                cost_percentage = 0.15

            cost = product.price * cost_percentage
            profit_per_item = product.price - cost

            print(f"{product.id:<5} {product.description:<20} {product.quantity:<10} R$ {product.price:<12.2f} R$ {cost:<12.2f} R$ {profit_per_item:<12.2f}")

        total_stock_value = self.calculate_total_stock_value()
        total_estimated_profit = self.calculate_estimated_profit()

        print("\nResumo Geral:")
        print(f"Valor Total do Estoque: R$ {total_stock_value:.2f}")
        print(f"Lucro Presumido Total: R$ {total_estimated_profit:.2f}")

        