import os


def validate_line(full_line):
    parts = full_line.split()
    if len(parts) != 3:
        raise IndexError("Не введены значения всех трех полей")

    name, email, age = parts

    if not name.isalpha():
        raise NameError("Поле 'Имя' содержит не только буквы")

    if '@' not in email or '.' not in email:
        raise SyntaxError("Поле 'email' не содержит @ или . (точку)")

    if not (age.isdigit() and 10 <= int(age) <= 99):
        raise ValueError("Поле 'Возвраст' не является числом от 10 до 99")
    


with open(os.path.join('Module23', '03_registration', 'registrations.txt'), 'r', encoding = 'utf-8') as registration_file:
    for line in registration_file:
        line = line.strip()

        if not line:
            continue

        try:
            validate_line(line)

            with open(os.path.join('Module23', '03_registration', 'registrations_good.log'), 'a', encoding = 'utf-8') as good_registration:
                good_registration.write(line + '\n')

        except (IndexError, NameError, SyntaxError, ValueError) as user_error:
            with open(os.path.join('Module23', '03_registration', 'registrations_bad.log'), 'w', encoding = 'utf-8') as bad_registration:
                bad_registration.write(f"{line}\t{str(user_error)}")

print("Содержимое файла registrations_good.log:")
with open(os.path.join('Module23', '03_registration', 'registrations_good.log'), 'r', encoding = 'utf-8') as good_result:
    for line in good_result:
        print(line)


        

