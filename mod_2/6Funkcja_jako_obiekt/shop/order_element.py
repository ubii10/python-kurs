class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        result = f"{self.product}\n\t\t x {self.quantity}"
        return result

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity

    def calculate_price(self):
        return self.product.unit_price * self.quantity
