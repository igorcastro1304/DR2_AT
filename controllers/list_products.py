from controllers.list_soldout_products import list_souldout_products

def list_all_products(ProductController):
    order_by = input("Deseja ordenar o produto pela quantidade decrescentemente (S/N): ").upper()

    if order_by == "S":
        ProductController.sort_products(ascending = False)
        ProductController.list_products()
    else:
        ProductController.sort_products(ascending = True)
        ProductController.list_products()

def make_list_action(option, ProductController):
    if option == 1:
        list_all_products(ProductController)
    
    elif option == 2:
        list_souldout_products(ProductController)

def list_products(ProductController):
    print()
    print("1 - Listar todos os medicamentos;")
    print("2 - Listar medicamentos esgotados.")
    print()

    option = int(input("Selecione a opção desejada: "))

    make_list_action(option, ProductController)
    