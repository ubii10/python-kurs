from shop.discount_policy import DiscountPolicy
from shop.order_element import OrderElement


class Order:

    MAX_ELEMENTS = 5

    def __init__(self, client_first_name, client_last_name, order_elements=None, discount_policy=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ELEMENTS:
            order_elements = order_elements[:Order.MAX_ELEMENTS]
        self._order_elements = order_elements
        if discount_policy is None:
            discount_policy = DiscountPolicy()
        self.discount_policy = discount_policy

    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        product_details = "Zamówione produkty: \n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, mark_line])
        return result

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        same_elements = True
        for i in self._order_elements:
            if i not in other.order_elements:
                same_elements = False
        return (self.client_first_name == other.client_first_name and
                self.client_last_name == other.client_last_name and
                len(self._order_elements) == len(other.order_elements) and same_elements)

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, value):
        if len(value) < Order.MAX_ELEMENTS:
            self._order_elements = value
        else:
            self._order_elements = value[:Order.MAX_ELEMENTS]

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy.apply_discount(total_price)

    def add_product_to_order(self, product, quantity):
        if len(self._order_elements) < Order.MAX_ELEMENTS:
            self._order_elements.append(OrderElement(product, quantity))
        else:
            print("Przekroczono limit produktów")

    # @classmethod
    # def generate_order(cls, number_of_products):
    #     order_elements = []
    #     for product_number in range(number_of_products):
    #         product_name = f"Produkt-{product_number}"
    #         category_name = "Inne"
    #         unit_price = random.randint(1, 30)
    #         product = Product(product_name, category_name, unit_price)
    #         quantity = random.randint(1, 10)
    #         order_elements.append(OrderElement(product, quantity))
    #
    #     order = Order(client_first_name="Mikołaj", client_last_name="Lewandowski", order_elements=order_elements)
    #     return order
