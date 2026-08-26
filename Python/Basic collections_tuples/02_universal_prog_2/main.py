def is_prime(index):
    if index < 2:
        return False

    for number in range(2, index):
        if index % number == 0:
            return False

    return True


def crypto(iterable):
    index_catalog = list()
    for index, element in enumerate(iterable):
        if is_prime(index):
            index_catalog.append(element)

    return index_catalog

        
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
