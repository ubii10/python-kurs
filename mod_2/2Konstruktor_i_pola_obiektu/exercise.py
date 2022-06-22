import random


class Product:

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order:

    def __init__(self, first_name, last_name, products=None):
        self.first_name = first_name
        self.last_name = last_name

        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            if type(product) != str:
                total_price += product.price

        self.total_price = total_price


class Apple:

    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price


class Potato:

    def __init__(self, species, size, price):
        self.species = species
        self.size = size
        self.price = price


def generate_order(first_name, last_name):
    products = []
    for i in range(random.randint(1, 15)):
        products.append(f"Produkt-{i}")

    random_order = Order(first_name, last_name, products)
    return random_order


if __name__ == "__main__":
    order = generate_order("Kuba", "Olech")
    print(order.first_name, order.last_name, order.products, order.total_price)
    # bread = Product("Bread", "Baked goods", 5)
    # lollipop = Product("Lollipop", "Sweets", 3)
    #
    # first_order = Order("Jakub", "Olech")
    # second_order = Order("Marek", "Kowalski", [bread, lollipop])
    #
    # print(first_order.first_name, first_order.last_name, first_order.products)
    # print(second_order.first_name, second_order.last_name, second_order.products, second_order.total_price)
