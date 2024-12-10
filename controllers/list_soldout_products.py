def list_souldout_products(ProductController):
    soldout_products = ProductController.list_soldout_products()

    if not soldout_products:
        print("Nenhum medicamento está esgotado!")
    else:
        for product in soldout_products:
            print(str(product))