import random

def create_new_catalog(original):
    result = [(original[index], original[index + 1]) for index in range(0, len(original), 2)]
    return result

def create_new_zipping_catalog(original):
    result = list(zip(original[::2], original[1::2]))
    return result


original_catalog = [random.randint(0, 100) for _ in range(10)]
print("Оригинальный список:", original_catalog)

new_catalog = create_new_catalog(original_catalog)
print("Первый способ:", new_catalog)

new_catalog_zipping = create_new_zipping_catalog(original_catalog)
print("Второй способ (.zip()):", new_catalog_zipping)