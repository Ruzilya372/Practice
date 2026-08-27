import os
import random

class Lucky_error(Exception):
    pass


def play_lucky_game():
    sum_numbers = 0
    with open(os.path.join('Module23', '02_lucky_number', 'out_file.txt'), 'a', encoding = 'utf-8') as result_file:
        while sum_numbers < 777:
            try:
                number = int(input("Введите число: "))
            except ValueError:
                print("Пожалуйста, введите число!")
                continue

            sum_numbers += number
            result_file.write(str(number) + '\n')

            if random.randint(1,13) == 1:
                raise Lucky_error ("Вас постигла неудача!")


try:
    play_lucky_game()
    print("Вы успешно выполнили условие для выхода из порочного цикла!\n")

    print("Содержимое файла out_file.txt:")

    with open(os.path.join('Module23', '02_lucky_number', 'out_file.txt'), 'r', encoding = 'utf-8') as result:
        for line in result:
            print(line.strip())

except Lucky_error as user_error:
    print("Ошибка:", user_error)
