import preload.product
import preload.services.menu
import controllers.create_product
import controllers.product_controller
import controllers.list_products

ProductController = controllers.product_controller.ProductController()
show_menu = preload.services.menu.show_menu

preload.product.initialize(ProductController)
show_menu(ProductController)

