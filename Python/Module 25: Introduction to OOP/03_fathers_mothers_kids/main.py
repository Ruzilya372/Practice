class Parent:
    def __init__(self, name, age, childrens):
        self.name = name
        self.age = age
        self.childrens = childrens

    def info(self):
        children_names = [child.name for child in self.childrens]
        return f"\nРодитель: {self.name}\nВозраст: {self.age}\n Мои дети: {','.join(children_names)}"

    def make_children_calm(self):
        for child in self.childrens:
            child.get_calm()
        print("Теперь малыш(и) успокоились :)")

    def feed_children(self):
        for child in self.childrens:
            child.get_food()
        print("Малыш(и) поел(и)!\n")


class Children:
    calm_states = {0: "спокоен", 1: "начинает волноваться", 2: "нервничает"}
    hunger_state = {0: "сыт", 1: "хочет перекусить", 2: "голоден"}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = 0
        self.hunger = 0

    def info(self):
        return f"Малыш: {self.name}\nВозраст: {self.age}\nСостояние: {self.calm_states[self.calm]}\nГолод: {self.hunger_state[self.hunger]}"

    def get_food(self):
        if self.hunger > 0:
            self.hunger = 0
        print(f"{self.name} поел! Теперь он {self.hunger_state[self.hunger]}")
    
    def get_calm(self):
        if self.calm > 0:
            self.calm = 0
        print(f"{self.name} успокоился. Теперь он {self.calm_states[self.calm]}")

    def change_hunger(self):
        self.hunger += 1
        print(f"Событие! Малыш {self.name} {self.hunger_state[self.hunger]}")

    def change_calm(self):
        self.calm += 1
        print(f"Событие! Малыш {self.name} {self.calm_states[self.calm]}")



def validate_child_age(age, parent_age):
    if age < 0:
        raise ValueError ("Возраст не может быть меньше 0!")
    if parent_age - age < 16:
        raise ValueError(f"Возраст малыша {age} должен быть младше Вас хотя бы на 16 лет!")
    return True
def get_child_age(parent_age):
    while True:
        try:
            kid_age = int(input("Введите возраст малыша: "))
            validate_child_age(kid_age, parent_age)

            return kid_age
        except ValueError as age_error:
            print(f"Ошибка: {age_error}")
            print("Попробуйте снова.\n")


print("Игра 'Дочки-Матери'! ")
print("Вы - Родитель. Вам предстоит ухаживать за малышом." \
"Не забывайте кормить и успокаивать своего малыша.")

username = input("\nВведите свое имя: ")
user_age = int(input("Введите свой возраст: "))

print("\nВведем информацию о малышах!")
children_catalog = []
children_quantity = int(input("Введите количество детей: "))

for kid in range(children_quantity):
    children_name = input(f"\nВведите имя {kid + 1} малыша: ")
    children_age = get_child_age(user_age)

    child = Children(children_name, children_age)
    children_catalog.append(child)

user = Parent(username, user_age, children_catalog)

step_counter = 0
print("\nСтарт игры!\n")
while True:
    step_counter += 1

    if step_counter % 2 == 0:
        print("\nВеликий рандом!")
        for child in children_catalog:
            child.change_hunger()

    if step_counter % 3 == 0:
        print("Великий рандом!")
        for child in children_catalog:
            child.change_calm()

    print("Действия:")
    print("1. Покормить детей")
    print("2. Успокоить детей")
    print("3. Посмотреть информацию о детях")
    print("4. Посмотреть инфомрацию о себе")
    print("5. Выйти из игры")

    try:
        choice = int(input("\nВаш Выбор: "))
    except ValueError:
        print("Пожалуйста, введите число от 1 до 5.")
        continue

    if choice == 1:
        user.feed_children()
    elif choice == 2:
        user.make_children_calm()
    elif choice == 3:
        for child in children_catalog:
            print(child.info())
    elif choice == 4:
        print(user.info())
    elif choice == 5:
        print("Игра завершена!")
        break
    else:
        print("Неверный формат. Попробуйте снова")



