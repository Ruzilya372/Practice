how_much_pairs = int(input("Введите количество пар слов: "))
pairs_dictionary = dict()

for number in range(1, how_much_pairs + 1):
    pair = input(f"{number} пара: ")

    word_first, word_second = pair.split(" - ")

    word_first = word_first.strip()
    word_second = word_second.strip()

    pairs_dictionary[word_first.lower()] = word_second
    pairs_dictionary[word_second.lower()] = word_first


while True:
    word = input("Введите слово: ").lower()

    if word in pairs_dictionary:
        print(f"Синоним: {pairs_dictionary[word]}")
        break
    else:
        print("Такого слова нет в словаре.")
