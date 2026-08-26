def find_min_additions(elements):
    elements_long = len(elements)
    for element in range(elements_long):
        left = element
        right = elements_long - 1
        is_palindrome = True

        while left < right:
            if elements[left] != elements[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1

        if is_palindrome:
            numbers_to_add = elements[:element][::-1]
            return len(numbers_to_add), numbers_to_add
    return 0, []


how_much_numbers = int(input("Кол-во чисел: "))
catalog = []

for _ in range(how_much_numbers):
    number = int(input("Число: "))
    catalog.append(number)

print("Последовательность:", catalog)
count, numbers = find_min_additions(catalog)

print("Нужно приписать чисел:", count)
if count > 0:
    print("Сами числа:", numbers)