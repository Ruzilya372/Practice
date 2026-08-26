array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# 1 задача
first_catalog = list()
for element in array_1:
    if element in array_2 and element in array_3:
        first_catalog.append(element)
print("1 задача без множеств:", first_catalog)


set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)

first_set_catalog = set_1 & set_2 & set_3
print("1 задача со множествами:", sorted(first_set_catalog))
# 2 задача
second_catalog = list()
for element in array_1:
    if not element in array_2 and not element in array_3:
        second_catalog.append(element)
print("\n2 задача без множеств:", second_catalog)


set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)

second_set_catalog = set_1 - set_2 - set_3
print("2 задача со множествами:", sorted(second_set_catalog))