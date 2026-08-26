nice_catalog = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def flatten_catalog(old_catalog):
    new_catalog = []
    for element in old_catalog:
        if isinstance(element, int):
            new_catalog.append(element)
        elif isinstance(element, list):
            new_catalog.extend(flatten_catalog(element))
    return new_catalog


result = flatten_catalog(nice_catalog)
print(result)
