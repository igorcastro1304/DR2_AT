def calc_estimated_profit(ProductController):
    total_profit = ProductController.calculate_estimated_profit()

    print(f"\nO lucro total estimado do estoque é R$ {total_profit:,.2f}\n")