def get_frequency_dictionary(message):
    frequency_dictionary = dict()
    for symbol in message:
        frequency_dictionary[symbol] = frequency_dictionary.get(symbol, 0) + 1

    return frequency_dictionary


def invert_frequency_dictionary(frequency_message):
    invert_dictionary = dict()

    for symbol, frequency in frequency_message.items():
        if frequency in invert_dictionary:
            invert_dictionary[frequency].append(symbol)
        else:
            invert_dictionary[frequency] = [symbol]

    return invert_dictionary


def print_frequency_dictionary(title, frequency_dictionary):
    print(title)
    for key, value in sorted(frequency_dictionary.items()):
        print(f"{key}: {value}")


text = input("Введите текст: ")

original_frequency = get_frequency_dictionary(text)

inverted_frequency = invert_frequency_dictionary(original_frequency)

print_frequency_dictionary("Оригинальный словарь частот: ",original_frequency)
print_frequency_dictionary("Инвертированный словарь частот: ", inverted_frequency)