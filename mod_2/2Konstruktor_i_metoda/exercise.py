import random


class Product:

    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price

    def print_product(self):
        print(f"Nazwa: {self.name} | Kategoria: {self.category_name} | Cena: {self.unit_price}/szt")


class Order:

    def __init__(self, client_first_name, client_last_name, products=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price

    def print_order(self):
        print("=" * 20)
        print(f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}")
        print(f"O łącznej wartości: {self.total_price} PLN")
        print("Zamówione produkty:")
        for product in self.products:
            print("\t", end="")
            product.print_product(product)
        print("=" * 20)
        print()


class OrderElement:

    def __init__(self):


class Apple:

    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price

    def count_total(self, weight):
        return weight * self.price


class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


# def print_product(product):
#     print(f"Nazwa: {product.name} | Kategoria: {product.category_name} | Cena: {product.unit_price}/szt")


# def print_order(order):
#     print("=" * 20)
#     print(f"Zamówienie złożone przez: {order.client_first_name} {order.client_last_name}")
#     print(f"O łącznej wartości: {order.total_price} PLN")
#     print("Zamówione produkty:")
#     for product in order.products:
#         print("\t", end="")
#         print_product(product)
#     print("=" * 20)
#     print()


def generate_order():
    number_of_product = random.randint(1, 10)
    products = []
    for product_number in range(number_of_product):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        products.append(product)

    order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski", products=products)
    return order


def run_homework():
    first_order = generate_order()
    first_order.print_order()
    second_order = generate_order()
    second_order.print_order()


if __name__ == '__main__':
    run_homework()
