def get_caesar_shifr(text, shift_number):
    alphabet_low = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    result = [
        alphabet_low[(alphabet_low.index(symbol) + shift_number) % len(alphabet_low)]
        if symbol in alphabet_low
        else alphabet_up[(alphabet_up.index(symbol) + shift_number) % len(alphabet_up)]
        if symbol in alphabet_up
        else symbol for symbol in text
    ]

    return "".join(result)

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

shifr_message = get_caesar_shifr(message, shift)
print("Зашифрованное сообщение:", shifr_message)