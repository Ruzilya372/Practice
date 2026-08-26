import os
import random

sum_numbers = 0
with open(os.path.join('Module23', '02_lucky_number', 'out_file.txt'), 'a', encoding = 'utf-8') as result_file:
    while sum_numbers < 777:
        number = int(input("Введите число: "))
        sum_numbers += number
        number = str(number)
        result_file.write(number + '\n')
        if random.randint(1,13) == 1:
            raise Exception ("Вас постигла неудача!")


print("Вы успешно выполнили условие для выхода из порочного цикла!\n")
print("Содержимое файла out_file.txt:")

with open(os.path.join('Module23', '02_lucky_number', 'out_file.txt'), 'r', encoding = 'utf-8') as result:
    for line in result:
        print(line.strip())