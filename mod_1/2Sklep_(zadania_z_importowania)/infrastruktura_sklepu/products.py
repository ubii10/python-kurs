available_products = {
    "Chleb": {
        "Quantity": 12,
        "Price": 6
    },
    "Jabłko": {
        "Quantity": 20,
        "Price": 3
    },
    "Chipsy": {
        "Quantity": 8,
        "Price": 7
    }
}


def update_quantity(product, amount):
    available_products[product]["Quantity"] -= amount
