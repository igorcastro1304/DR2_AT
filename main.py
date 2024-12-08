import preload.product
import controllers.create_product
import controllers.product_controller

ProductController = controllers.product_controller.ProductController()

preload.product.initialize(ProductController)
controllers.create_product.create_product(ProductController)
print(ProductController.list_products())

