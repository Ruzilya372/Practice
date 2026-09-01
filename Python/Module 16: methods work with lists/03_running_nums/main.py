def move_element(number, position):
    number_element = len(number)
    position = position % number_element
    return number[-position:] + number[:-position]


numbers = [1, 2, 3, 4, 5]
shift = int(input("Сдвиг: "))
print("Изначальный список:", numbers)
new_number = move_element(numbers, shift)

print("Сдвинутый список:", new_number)