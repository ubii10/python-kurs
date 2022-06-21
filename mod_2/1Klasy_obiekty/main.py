class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == "__main__":
    big_apple = Apple()
    small_apple = Apple()

    sweet_potato = Potato()
    huge_potato = Potato()

    print(f"type big_apple: {type(big_apple)}")
    print(f"type small_apple: {type(small_apple)}")
    print(f"type sweet_potato: {type(sweet_potato)}")
    print(f"type huge_potato: {type(huge_potato)}")

    orders_list = [Order(), Order(), Order(), Order(), Order()]

    print(orders_list)

    product_description = {
        "apple": Product(),
        "potato": Product(),
        "tomato": Product(),
        "sausage": Product(),
        "bread": Product()
    }

    print(product_description)