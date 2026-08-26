def get_character_dictionary(symbols):
    character_dictionary = dict()
    for character in symbols:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        else:
            character_dictionary[character] += 1

    return character_dictionary


def find_pallindrome(character_dictionary):
    odd_count = 0
    for quantity in character_dictionary.values():
        if quantity % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return True
    else:
        return False


text = input("Введите строку: ")

symbol_dictionary = get_character_dictionary(text)
is_pallindrome = find_pallindrome(symbol_dictionary)

if is_pallindrome:
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
