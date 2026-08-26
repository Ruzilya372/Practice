import os

file_numbers = open((os.path.join('Module22', '01_nums_sum_2', 'numbers.txt')), 'r', encoding = 'utf-8')
total = 0
print("Содержимое файла numbers.txt")
for line in file_numbers:
    print(line, end = '')
    number = line.split()
    for element in number:
        total += int(element)

file_numbers.close()


file_answer = open('answer.txt', 'w', encoding = 'utf-8')
file_answer.write(str(total))
print("Содержимое файла answer.txt")
print(total)

file_answer.close()