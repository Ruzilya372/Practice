def count_max_people(roller_size, people_foot_size):
    roller_size.sort()
    people_foot_size.sort()

    people_count = 0
    roller_index = 0

    for foot_size in people_foot_size:
        while roller_index < len(roller_size):
            if roller_size[roller_index] >= foot_size:
                people_count+= 1
                roller_index += 1
                break
            else:
                roller_index += 1
        if roller_index >= len(roller_size):
            break
    return people_count


how_much_roller_skates = int(input("Кол-во коньков: "))
roller_skates_catalog = []
for roller_skates in range(1, how_much_roller_skates + 1):
    size_roller = int(input("Размер "+str(roller_skates)+"-й пары: "))
    roller_skates_catalog.append(size_roller)

how_much_people = int(input("\nКол-во людей: "))
people_catalog = []

for people in range(1, how_much_people + 1):
    size_foot_people = int(input("Размер ноги "+str(people)+"-го человека:"))
    people_catalog.append(size_foot_people)

max_people = count_max_people(roller_skates_catalog, people_catalog)

print("\nНаибольшее кол-во людей, которые могут взять ролики:" , max_people)