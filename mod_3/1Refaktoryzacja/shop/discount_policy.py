def default_policy(total):
    return total


def long_term_client_discount(total):
    discount = 0.05
    return total * (1 - discount)


def christmas_discount(total):
    if total > 100:
        return total - 20
    return total
