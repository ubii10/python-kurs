from .products import available_products, update_quantity

orders = []


def create_new_order(product, amount):
    while product not in available_products.keys():
        print("Nie mamy takiego towaru")
        product = input("Podaj nazwe produktu lub zrezygnuj z zakupów (X): ")
        if product == "X":
            return None

    while int(amount) > available_products[product]["Quantity"]:
        print("Nie mamy takiej ilości!")
        amount = int(input(f"Podaj mniejszą wartosc z przedziału 1-{available_products[product]['Quantity']}. Aby "
                           f"zakończyć zakupy wpisz 0: "))
        if amount == 0:
            return None

    total_price = amount * available_products[product]["Price"]
    new_order = {
        "product": product,
        "quantity": amount,
        "total_price": total_price
    }
    update_quantity(product, amount)
    orders.append(new_order)
    return new_order
