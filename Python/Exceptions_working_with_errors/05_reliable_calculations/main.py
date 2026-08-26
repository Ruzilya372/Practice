import math

def get_safe_sqrt(element):
    try:
        value = float(element)

        if value < 0:
            raise ValueError ("Число не может быть отрицательным")

        sqrt_element = math.sqrt(value)
        return round(sqrt_element, 2)
    
    except ValueError as value_error:
        print(f"Ошибка: {value_error}")
        return None
    except TypeError as type_error:
        print(f"Ошибка: {type_error}")
        return None


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_safe_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")