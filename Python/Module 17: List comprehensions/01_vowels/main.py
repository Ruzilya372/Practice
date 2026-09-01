text = input("Введите текст: ")
vowels = ["у", "е", "а", "о", "э", "я", "и", "ю", "ы", "ё"]
vowels_catalog = [letter for letter in text if letter in vowels]
print("Список гласных букв:", vowels_catalog)
print("Длина гласных:", len(vowels_catalog))

