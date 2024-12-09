def list_all_products(ProductController):
    order_by = input("Deseja ordenar o produto pela quantidade decrescentemente (S/N): ").upper()

    if order_by == "S":
        ProductController.sort_products(ascending = False)
        ProductController.list_products()
    else:
        ProductController.sort_products(ascending = True)
        ProductController.list_products()