from shop.order import Order
from shop.product import Product
from shop.order_element import OrderElement
from shop.discount_policy import default_policy, christmas_discount, long_term_client_discount
import random


def generate_order_elements():
    order_elements = []
    for product_number in range(5):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))
    return order_elements


def run_homework():
    first_name = "Kuba"
    last_name = "Olech"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements, default_policy)
    loyal_customer = Order(first_name, last_name, order_elements, long_term_client_discount)
    christmas_order = Order(first_name, last_name, order_elements, christmas_discount)

    print(normal_order)
    print(loyal_customer)
    print(christmas_order)


if __name__ == '__main__':
    run_homework()
