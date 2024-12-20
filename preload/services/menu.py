from controllers import create_product, list_products, search_product, remove_product, update_products, calc_stock_value, calc_estimated_profit, make_general_report

"""
    Função para realizar a ação escolhida pelo usuário.
"""
def make_action(option, ProductController):
    if option == 1:
        create_product.create_product(ProductController)

    elif option == 2:
        list_products.list_products(ProductController)
    
    elif option == 3:
        search_product.search_product_menu(ProductController)

    elif option == 4:
        update_products.update_products_menu(ProductController)

    elif option == 5:
        remove_product.remove_product(ProductController)

    elif option == 6:
        calc_stock_value.calculate_total_stock_value(ProductController)

    elif option == 7:
        calc_estimated_profit.calc_estimated_profit(ProductController)
    elif option == 0:
        make_general_report.make_general_report(ProductController)

"""
    Função para exibir o menu interativo ao usuário.
"""
def show_menu(ProductController):
    option = -1

    print("Olá, usuário! Seja muito bem-vindo ao sistema de gestão de medicamentos!")
    print()
    
    while option != 0:
        print("Utilize o teclado numérico para selecionar uma opção: ")
        print("1 - Adicionar novo medicamento;")
        print("2 - Listar medicamentos;")
        print("3 - Buscar medicamento(s);")
        print("4 - Atualizar estoque;")
        print("5 - Excluir medicamento;")
        print("6 - Calcular valor total do estoque;")
        print("7 - Calcular lucro estimado;")
        print("0 - Sair.")
        print()

        option = int(input("Escolha a opção desejada: "))
        make_action(option, ProductController)

        
