from shop.order import generate_order
from shop.product import Product


def run_homework():
    first_order = generate_order()
    print(first_order)

    cookie = Product("Ciastko", category_name="Przekąska", unit_price=3)
    first_order.add_product_to_order(cookie, quantity=5)
    print(first_order)


if __name__ == "__main__":
    run_homework()
