from models.product import Product

def create_product(ProductController):
    print("------CADASTRO DE NOVO MEDICAMENTO------")

    id = int(input("Digite o ID do novo medicamento: "))
    description = input("Digite o nome do novo medicamento: ")
    quantity = int(input("Digite a quantidade inicial em estoque do novo medicamento: "))
    price = float(input("Digite o preço do novo medicamento (ex: 39.99): "))
    print(price)

    ProductController.add_product(id, description, quantity, price)
    print(f"Novo produto ({Product(id, description, quantity, price)}) adicionado com sucesso!")
    