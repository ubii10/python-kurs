from infrastruktura_sklepu.orders import create_new_order


def run_shop():
    print("Witamy w sklepie")
    product_name = input("Co chcesz kupić? ")
    amount = int(input("W jakiej ilosci? "))

    result = create_new_order(product_name, amount)
    if result is not None:
        print(f"Łączny koszt to {result['total_price']} zl")


if __name__ == "__main__":
    run_shop()
