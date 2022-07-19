from shop.order import Order
from shop.data_generator import generate_order_elements


def run_homework():
    first_name = "Kuba"
    last_name = "Olech"
    order_elements = generate_order_elements()
    first_order = Order(first_name, last_name, order_elements=order_elements)
    print(first_order)


if __name__ == '__main__':
    run_homework()
