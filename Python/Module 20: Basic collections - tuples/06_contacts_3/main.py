def add_contact(contacts):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    number = int(input("Введите номер телефона: "))
    key = (name, surname)
    if key in contacts:
        return False
    else:
        contacts[key] = number
        return True


def find_contact(contacts):
    contact_surname = input("Введите Фамилию: ").lower()
    found = False
    for (name, surname), number in contacts.items():
        if surname.lower() == contact_surname:
            print(name, surname, number)
        else:
            print("Контактов с такой фамилией не найдено.")



contact_dictionary = dict()

while True:
    action = int(input("Введите номер действия: 1. Добавить контакт 2. Найти человека "))
    if action == 1:
        new_contact = add_contact(contact_dictionary)

        if new_contact == False:
            print("Такой контакт уже сущетсвует в телефонной книге!")
        else:
            print("Текущая база контактов:", contact_dictionary)
    elif action == 2:
        old_contact = find_contact(contact_dictionary)
    else:
        print("Такого действия не существует!")
