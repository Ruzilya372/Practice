def extract_numbers(data):
    if isinstance(data, (int, float)):
        return data
    elif isinstance(data, list):
        number_summ = 0
        for element in data:
            number_summ += extract_numbers(element)
        return number_summ
    else:
        return 0


def custom_sum(*args):
    total = 0
    for argument in args:
        total += extract_numbers(argument)
    return total


# print(custom_sum([[1, 2, [3]], [1], 3]))