import random
from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order

MIN_PRODUCT_PRICE = 3
MIN_PRODUCT_QUANTITY = 1

MAX_PRODUCT_PRICE = 15
MAX_PRODUCT_QUANTITY = 10


def generate_order_elements(products_amount=None):
    order_elements = []
    if products_amount is None:
        products_amount = random.randint(1, Order.MAX_ELEMENTS)
    for product_number in range(products_amount):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_PRODUCT_PRICE, MAX_PRODUCT_PRICE)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(MIN_PRODUCT_QUANTITY, MAX_PRODUCT_QUANTITY)
        order_elements.append(OrderElement(product, quantity))
    return order_elements
