def list_below_minimum_products(ProductController):
    ProductController.list_below_minimum_products()

def list_souldout_products(ProductController):
    soldout_products = ProductController.list_soldout_products()

    if not soldout_products:
        print("Nenhum medicamento está esgotado!")
    else:
        for product in soldout_products:
            print(str(product))

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
        list_below_minimum_products(ProductController)

    elif option == 3:
        list_souldout_products(ProductController)

def list_products(ProductController):
    print()
    print("1 - Listar todos os medicamentos;")
    print("2 - Listar medicamentos com estoque baixo;")
    print("3 - Listar medicamentos esgotados.")
    print()

    option = int(input("Selecione a opção desejada: "))

    make_list_action(option, ProductController)
    