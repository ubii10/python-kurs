import random


def create_text(*args):
    text = "-".join(args)
    return text


def how_was_i_created(**kwargs):
    arguments = []
    for key, value in kwargs.items():
        arguments.append(f"{key}={value}")
    return ", ".join(arguments)


def generate_two_lists():
    first_list = []
    for i in range(random.randint(1, 10)):
        first_list.append(random.randint(1, 100))
    print(first_list)

    second_list = []
    for i in range(random.randint(1, 5)):
        second_list.append(random.randint(10, 20))
    print(second_list)

    final_list = [*first_list, *second_list]
    return final_list


def example_4():
    first_dict = {
        "bułka": 5,
        "chleb": 3
    }

    second_dict = {
        "masło": 3,
        "czekolada": 10
    }

    final_dict = {**first_dict, **second_dict}
    print(final_dict)
    return how_was_i_created(**final_dict)


if __name__ == "__main__":
    print(create_text("test", "test2", "ulala"))
    print(how_was_i_created(matematyka=3, fizyka=6))
    print(generate_two_lists())
    print(example_4())
