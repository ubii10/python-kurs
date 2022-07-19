

class DiscountPolicy:

    def apply_discount(self, total):
        return total


class PercentageDiscount(DiscountPolicy):

    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total):
        return total * (1 - self.percentage)


class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total):
        if total < self.discount_amount:
            return 0
        return total - self.discount_amount
