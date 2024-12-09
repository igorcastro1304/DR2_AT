def stock_reader(products_str, ProductController):
    products_list = products_str.split("#")

    for product in products_list:
        single_product = product.split(";")
        ProductController.add_product(int(single_product[1]), single_product[0], int(single_product[2]), float(single_product[3]))
        
    ProductController.list_products()