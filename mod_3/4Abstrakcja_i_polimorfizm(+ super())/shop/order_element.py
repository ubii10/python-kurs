from dataclasses import dataclass
from shop.product import Product


@dataclass
class OrderElement:
    product: Product
    quantity: int

    def __str__(self):
        result = f"{self.product}\n\t\t x {self.quantity}"
        return result

    def calculate_price(self):
        return self.product.unit_price * self.quantity
