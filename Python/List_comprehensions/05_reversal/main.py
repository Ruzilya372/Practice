text = input("Введите строку: ")
start = text.index("h")
finish = text.rindex("h")

text_catalog = text[start + 1:finish]

reverse_text_catalog = text_catalog[::-1]

print("Развернутая последовательнсоть между первым и последним h:", reverse_text_catalog)