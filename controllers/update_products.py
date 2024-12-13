from models.product import Product

"""
    Função para aumentar a quantidade do produto no estoque
"""
def increase_quantity_on_update(ProductController):
    product_id = int(input("Digite o ID do medicamento recebido: "))
    product = ProductController.search_by_id(product_id)

    if isinstance(product, Product):
        print(str(product))
        print()

        quantity_to_increase = int(input("Digite quantas unidades foram recebidas: "))
        product_updated = ProductController.increase_quantity(product, quantity_to_increase)
        print(f"\nProduto atualizado! {product_updated}\n")
    else:
        print("\nNenhum produto encontrado")
        
"""
    Função para diminuir a quantidade do produto no estoque
"""
def decrease_quantity_on_update(ProductController):
    product_id = int(input("Digite o ID do medicamento retirado: "))
    product = ProductController.search_by_id(product_id)
    
    if isinstance(product, Product):
        print(str(product))
        print()

        quantity_to_decrease = int(input("Digite quantas unidades foram retiradas: "))
        product_updated = ProductController.decrease_quantity(product, quantity_to_decrease)

        if not isinstance(product, Product):
            print(product_updated)
        else:
            print(f"\nProduto atualizado! {product_updated}\n")
    else:
        print("\nNenhum produto encontrado")

"""
    Função para atualizar a quantidade mínima indicada do produto no estoque
"""
def update_minimum_limit(ProductController):
    product_id = int(input("Digite o ID do medicamento a ser atualizado: "))
    product = ProductController.search_by_id(product_id)
    
    if isinstance(product, Product):
        print(str(product))
        print()
        
        new_mininum_limit = int(input("Digite o novo limite mínimo de estoque: "))
        product_updated = ProductController.update_minimum_limit(product, new_mininum_limit)

        print(f"\nProduto atualizado! {product_updated}\n")
    else:
        print("\nNenhum produto encontrado")

"""
    Função para atualizar o preço do produto de acordo com as regras de negócio estabelecidas.
"""
def update_product_price(ProductController):
    product_id = int(input("Digite o ID do medicamento a ser atualizado: "))
    product = ProductController.search_by_id(product_id)
    
    if isinstance(product, Product):
        print(str(product))
        print()

        new_price = float(input("Digite o novo preço do produto: "))
        if new_price <= product.price:
            print("A mudança viola as políticas de preço da loja!")
        else:
            product_updated = ProductController.update_product_price(product, new_price)
            print(f"\nProduto atualizado! {product_updated}\n")
    else:
        print("\nNenhum produto encontrado")

"""
    Função para realizar a ação de atualização escolhida pelo usuário
"""
def make_update_action(option, ProductController):
    if option == 1:
        increase_quantity_on_update(ProductController)
    elif option == 2:
        decrease_quantity_on_update(ProductController)
    elif option == 3:
        update_minimum_limit(ProductController)
    elif option == 4:
        update_product_price(ProductController)

"""
    Função para exibir o menu interativo de atualização ao usuário
"""
def update_products_menu(ProductController):    
    option = -1
    
    print()
    print("------ATUALIZAÇÃO DE MEDICAMENTO------")
    print()

    while option != 0:
        print("1 - Aumentar estoque;")
        print("2 - Diminuir estoque;")
        print("3 - Atualizar limite mínimo;")
        print("4 - Atualizar preço;")
        print("0 - Sair.")
        print()

        option = int(input("Escolha uma opção:  "))
        make_update_action(option, ProductController)