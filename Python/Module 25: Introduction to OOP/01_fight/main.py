import random

class Warriors:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, other):
        other.health -= 20
        print(f"{self.name} атакует {other.name}.")
        print(f"у {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


first_warrior = Warriors("Воин 1")
second_warrior = Warriors("Воин 2")

while True:
    if random.randint(1,2) == 1:
        print(f"\n{first_warrior.name} атакует!")
        first_warrior.attack(second_warrior)
        if not second_warrior.is_alive():
            print(f"{second_warrior.name} погиб! Победитель - {first_warrior.name}")
            break
    else:
        print(f"{second_warrior.name} атакует!")
        second_warrior.attack(first_warrior)
        if not first_warrior.is_alive():
            print(f"{first_warrior.name} погиб! Победитель - {second_warrior.name}")
            break


