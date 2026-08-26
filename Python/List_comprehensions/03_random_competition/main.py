import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [max(first_team[member], second_team[member]) for member in range(20)]

print("Превая команда:", first_team)
print("Вторая команда:", second_team)
print("Победители тура:", winners)