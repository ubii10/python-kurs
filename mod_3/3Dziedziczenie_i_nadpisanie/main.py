from shop.discount_policy import *
from shop.order_express import ExpressOrder
from shop.data_generator import generate_order_elements


def run_homework():
    first_name = "Kuba"
    last_name = "Olech"
    order_elements = generate_order_elements()
    express_order = ExpressOrder(first_name, last_name,
                                 order_elements=order_elements,
                                 discount_policy=default_policy,
                                 delivery_date="30.06.2022")
    print(express_order)


if __name__ == '__main__':
    run_homework()
