site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def find_max_depth():
    while True:
        answer = input("Хотите ввести максимальную глубину? Y/N: ").lower()
        if answer == "y":
            depth = int(input("Введите максимальную глубину: "))
            return depth
        elif answer == "n":
            return None
        else:
            print("Неверный папрметр. Введите y или n. Где y - да, n - нет.")


def find_key(dictionary, key, current_depth, max_depth):

    if max_depth is not None and current_depth > max_depth:
        return None

    if key in dictionary:
        return dictionary[key]

        
    for key_element, value_element in dictionary.items():
        if isinstance(value_element, dict):
            result = find_key(value_element, key, current_depth + 1, max_depth)
            if result is not None:
                return result

    return None


search_key = input("Введите искомый ключ: ").lower()
max_depth = find_max_depth()

result = find_key(site, search_key, 0, max_depth)

print(f"Значение ключа: '{search_key}': '{result}'")