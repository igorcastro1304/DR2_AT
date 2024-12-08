import controllers.product_controller
ProductController = controllers.product_controller.ProductController()

def stock_reader(products_str):
    products_list = products_str.split("#")

    for product in products_list:
        single_product = product.split(";")
        ProductController.add_product(single_product[1], single_product[0], single_product[2], single_product[3])
        
    initial_products = ProductController.list_products()
    return initial_products