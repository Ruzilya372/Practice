import os

def get_count(item):
    return item[1]


text_file = open(os.path.join('Module22', '06_war_and_peace', 'voyna-i-mir.txt'), 'r', encoding = 'utf-8')
text = text_file.read()
text_file.close()

counts_letter = {}
for element in text:
    if element.isalpha():
        counts_letter[element] = counts_letter.get(element, 0) + 1

sorted_letters = sorted(counts_letter.items(), key = get_count, reverse=True)

for letter,counts_letter in sorted_letters:
    print(f"{letter}: {counts_letter}")