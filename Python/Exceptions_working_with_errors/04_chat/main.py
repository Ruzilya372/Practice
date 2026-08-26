import os

users_catalog = []

username = input("\nВведите свое имя: ")
if username in users_catalog:
    print(f"Добро пожаловать, {username}!")
else:
    users_catalog.append(username)
    print(f"Добро пожаловать, {username}! Рады видеть новых участников чата")


while True:

    try:
        choice = int(input("\nВыберите одно действие "
        "(1 - Посмотреть текущий текст чата;" \
        " 2 - Отправить сообщение): "))        
        if choice == 1:
            with open(os.path.join('Module23', '04_chat', 'chat.txt'), 'r', encoding = 'utf-8') as chat_file:
                print("История чата:")
                content = chat_file.read()
                if content:
                    print(content)
                else:
                    print("Чат пока пуст.")

        elif choice == 2:
            with open(os.path.join('Module23', '04_chat', 'chat.txt'), 'a', encoding = 'utf-8') as sent_message:
                message = input("Введите сообщение: ")
                sent_message.write(f"{username}: {message}\n")
        else:
            raise ValueError
        
    except ValueError:
        print("Неверный формат.")
    
