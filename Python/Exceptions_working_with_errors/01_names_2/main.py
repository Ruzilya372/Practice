import os


count_charachter = 0
line_number = 0

print("Ответ консоли:")
with open(os.path.join('Module23', '01_names_2', 'people.txt'), 'r', encoding = 'utf-8') as file_people:
    for line in file_people:
        line_number += 1
        line = line.rstrip()

        try:
            if len(line) < 3:
                raise ValueError

        except ValueError:
            print("Ошибка: менее трёх символов в строке", line_number)

        for charachter in line:
            
            count_charachter += 1


print("Общее количество символов:", count_charachter)