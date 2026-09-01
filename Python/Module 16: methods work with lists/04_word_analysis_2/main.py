word = input("Введите слово: ")

words = []
reverse_words = []

words.extend(word)

for letter in range(len(word) - 1, -1, -1):
    reverse_words.append(word[letter])

if words == reverse_words:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")