import os


with open(os.path.join('Module22', '05_frequency_analysis', 'text.txt'), 'r', encoding = 'utf-8') as text_file:
    file_content = text_file.read()

english_letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
letter_counts = {}
total_letters = 0

for character in file_content:
    if character in english_letters:
        character = character.lower()
        letter_counts[character] = letter_counts.get(character, 0) + 1
        total_letters += 1

letter_proportions = []
for letter, count in letter_counts.items():
    letter_proportions.append([letter, count / total_letters])

    
def get_proportion(item):
    return item[1]


letter_proportions.sort(key=get_proportion, reverse = True)

for first_index in range(len(letter_proportions)):
    for second_index in range(first_index + 1, len(letter_proportions)):
        if letter_proportions[first_index][1] == letter_proportions[second_index][1]:
            letter_proportions[first_index], letter_proportions[second_index] = letter_proportions[second_index], letter_proportions[first_index]


with open(os.path.join('Module22', '05_frequency_analysis', 'analysis.txt'), 'w', encoding = 'utf-8') as analysis_file:
    for letter, proportion in letter_proportions:
        analysis_file.write(f"{letter} {proportion:.3f}\n")


print("Содержимое файла text.txt:")
print(file_content)

print("\nСодержимое файла analysis.txt:")
with open(os.path.join('Module22', '05_frequency_analysis', 'analysis.txt'), 'r', encoding = 'utf-8') as analysis_file:
    print(analysis_file.read())