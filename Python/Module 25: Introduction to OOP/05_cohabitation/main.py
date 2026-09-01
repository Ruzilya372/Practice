import random

class Person:
    def __init__(self, name, home):
        self.name = name
        self.hunger = 50
        self.home = home
        self.is_alive = True

    def person_eat(self):
        if self.home.fridge >= 10:
            self.hunger += 10
            self.home.fridge -= 10
            print(f"{self.name} поел(а). Сытость: {self.hunger}. Еды в холодильнике: {self.home.fridge}")
        else:
            print(f"{self.name} хочет есть. Еды в холодильнике: {self.home.fridge}")


    def person_work(self):
        self.hunger -= 10
        self.home.money += 20
        print(f"{self.name} поработал(а)! Сытость: {self.hunger}. Деньги: {self.home.money}")


    def person_play(self):
        self.hunger -= 10
        print(f"{self.name} поиграл(а)! Сытость: {self.hunger}")


    def person_buy_food(self):
        if self.home.money >= 10:
            self.home.fridge += 10
            self.home.money -= 10
            print(f"{self.name} сходил(а) за продуктами! Теперь в холодильнике {self.home.fridge} еды, но осталось {self.home.money} руб.")
        else:
            print(f"{self.name} хочет купить еды, но денег: {self.home.money}")

  
    def person_live(self, day):
        if not self.is_alive:
            return

        print(f"День {day}. {self.name}")


        random_number = random.randint(1,6)


        if self.hunger < 20:
            self.person_eat()
        elif self.home.fridge < 10:
            self.person_buy_food()
        elif self.home.money < 50:
            self.person_work()
        elif random_number == 2:
            self.person_eat()
        elif random_number == 1:
            self.person_work()
        else:
            self.person_play()



        if self.hunger <= 0:
            self.is_alive = False
            print(f"{self.name} умер от голода! :( )")



class Home:
    def __init__(self):
        self.fridge = 50
        self.money = 0


home = Home()
people_male = Person("Артем", home)
people_female = Person("Аня", home)



for day in range(1, 366):
    if not people_female.is_alive and not people_male.is_alive:
        print("Оба человека погибли!")

    people_male.person_live(day)
    people_female.person_live(day)
