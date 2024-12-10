def remove_product(ProductController):
    id_to_remove = int(input("Digite o ID do produto que deseja remover: "))

    removed_product = ProductController.remove_product_by_id(id_to_remove)
    print(removed_product)

    print()
    print("------LISTA ATUALIZADA------")
    print()
    ProductController.list_products()
