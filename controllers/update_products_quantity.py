from models.product import Product

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

def make_update_action(option, ProductController):
    if option == 1:
        increase_quantity_on_update(ProductController)
    elif option == 2:
        decrease_quantity_on_update(ProductController)
    elif option == 3:
        update_minimum_limit(ProductController)

def update_products_menu(ProductController):
    
    option = -1
    
    print()
    print("------ATUALIZAÇÃO DE MEDICAMENTO------")
    print()

    while option != 0:
        print("1 - Aumentar estoque;")
        print("2 - Diminuir estoque;")
        print("3 - Atualizar limite mínimo;")
        print("0 - Sair.")
        print()

        option = int(input("Escolha uma opção:  "))
        make_update_action(option, ProductController)