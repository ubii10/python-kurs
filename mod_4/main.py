import random


def update_set(set_of_numbers):
    number = random.randint(0, 10)
    print(number)
    return set_of_numbers.union({number})


variable_set = set()

while len(variable_set) < 11:
    print(variable_set)
    variable_set = update_set(variable_set)

print(variable_set)
