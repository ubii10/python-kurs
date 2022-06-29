
class TaxCalculator:

    @staticmethod
    def calculate_tax(order_element):
        if order_element.product.category_name == "Owoce i warzywa":
            return order_element.product.unit_price * 0.05 * order_element.quantity
        elif order_element.product.category_name == "Jedzenie":
            return order_element.product.unit_price * 0.08 * order_element.quantity
        else:
            return order_element.product.unit_price * 0.2 * order_element.quantity
