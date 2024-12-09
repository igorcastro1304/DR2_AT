from controllers import create_product, list_all_products


def make_action(option, ProductController):
    if option == 1:
        create_product.create_product(ProductController)

    elif option == 2:
        list_all_products.list_all_products(ProductController)

def show_menu(ProductController):
    option = -1

    print("Olá, usuário! Seja muito bem-vindo ao sistema de gestão de medicamentos!")
    print()
    
    while option != 0:
        print("Utilize o teclado numérico para selecionar uma opção: ")
        print("1 - Adicionar novo medicamento;")
        print("2 - Listar medicamento;")
        print("0 - Sair")
        print()

        option = int(input("Escolha a opção desejada: "))
        make_action(option, ProductController)

        
