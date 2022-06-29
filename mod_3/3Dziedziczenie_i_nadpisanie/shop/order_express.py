from shop.order import Order


class ExpressOrder(Order):

    DELIVERY_PAYMENT = 10

    def __init__(self, client_first_name, client_last_name, delivery_date, order_elements=None, discount_policy=None):
        super().__init__(client_first_name, client_last_name, order_elements, discount_policy)
        self.delivery_date = delivery_date

    def __str__(self):
        mark_line = "=" * 20
        order_details = f"Ekpresowe zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        delivery_date_details = f"Zaplanowana data dostawy eskpresowej: {self.delivery_date}"
        product_details = "Zamówione produkty: \n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details,delivery_date_details, product_details, mark_line])
        return result

    @property
    def total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.calculate_price()
        return self.discount_policy(total_price) + ExpressOrder.DELIVERY_PAYMENT

