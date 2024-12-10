def search_by_id(ProductController):
    id = int(input("Digite o ID do produto: "))
    product = ProductController.search_by_id(id)

    print(product)

def search_by_description(ProductController):
    description = input("Digite a descrição do produto: ")
    matched_products = ProductController.search_by_description(description)

    print(matched_products)

def make_search(option, ProductController):
    if option == 1:
        search_by_id(ProductController)
    elif option == 2:
        search_by_description(ProductController)

def search_product_menu(ProductController):
    option = -1

    while option != 0:
        print("------BUSCA DE MEDICAMENTO------")
        print()
        
        print("Use o teclado numérico para fazer a busca desejada.")
        print("1 - Buscar por ID;")
        print("2 - Buscar por descrição;")
        print("0 - Voltar.")
        print()

        option = int(input("Escolha a opção desejada: "))

        make_search(option, ProductController)

