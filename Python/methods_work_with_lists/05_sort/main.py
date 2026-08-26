def use_bubble_sort(number_catalog):
    elements = len(number_catalog)
    for i in range(elements - 1):
        for j in range(elements - 1 - i):
            if number_catalog[j] > number_catalog[j + 1]:
                number_catalog[j], number_catalog[j + 1] = number_catalog[j + 1], number_catalog[j]


numbers = [1, 4, -3, 0, 10]
print("Изначальный список:", numbers)
use_bubble_sort(numbers)
print("Отсортированный список:", numbers)